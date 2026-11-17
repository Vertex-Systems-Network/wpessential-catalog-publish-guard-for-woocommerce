#!/usr/bin/env python3
"""Offline shape/ordering lint only. This is not live Blueprint schema validation."""
from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[1] / 'playground' / 'blueprints'
for label, count in [('base', 0), ('free', 1), ('pro', 2)]:
    b = json.loads((ROOT / label / 'blueprint.json').read_text())
    assert b['$schema'] == 'https://playground.wordpress.net/blueprint-schema.json'
    steps = b['steps']
    assert steps[0]['step'] == 'login'
    installs = [x for x in steps if x['step'] == 'installPlugin']
    assert installs[0]['pluginData'] == {'resource': 'wordpress.org/plugins', 'slug': 'woocommerce'}
    local = [x['pluginData']['path'] for x in installs if x['pluginData']['resource'] == 'bundled']
    assert local == ['/wpessential-catalog-publish-guard.zip',
                     '/wpessential-catalog-publish-guard-pro.zip'][:count]
    print(label, 'JSON + structural order valid; LIVE PLAYGROUND NOT RUN')
