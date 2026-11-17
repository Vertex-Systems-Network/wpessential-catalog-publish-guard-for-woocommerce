<?php
/** Standalone contract checks; no WordPress database or integration claims. */
class WC_Product {
    private $name;
    private $price;
    private $type;
    public function __construct($name, $price, $type = 'simple') {
        $this->name = $name;
        $this->price = $price;
        $this->type = $type;
    }
    public function get_name($context = 'view') { return $this->name; }
    public function get_price($context = 'view') { return $this->price; }
    public function get_type() { return $this->type; }
}
function wp_strip_all_tags($value) { return strip_tags($value); }
function __($value, $domain) { return $value; }

require __DIR__ . '/../../src/Contracts/Rule.php';
require __DIR__ . '/../../src/Rules/TitleRequired.php';
require __DIR__ . '/../../src/Rules/RegularPriceRequired.php';
require __DIR__ . '/../../src/Core/RuleEngine.php';

use WPEssential\CatalogPublishGuard\Core\RuleEngine;
use WPEssential\CatalogPublishGuard\Rules\TitleRequired;
use WPEssential\CatalogPublishGuard\Rules\RegularPriceRequired;

$engine = new RuleEngine([new TitleRequired(), new RegularPriceRequired()]);
$cases = [
    ['blank title and price', new WC_Product('  ', ''), ['BAS-001', 'PRC-001']],
    ['zero price is set', new WC_Product('Product', '0'), []],
    ['normal price', new WC_Product('Product', '12.50'), []],
    ['missing simple price', new WC_Product('Product', ''), ['PRC-001']],
    ['variable parent price comes from children', new WC_Product('Parent', '', 'variable'), []],
    ['external product may omit price', new WC_Product('External', '', 'external'), []],
];
foreach ($cases as [$label, $product, $expected]) {
    $actual = array_column($engine->evaluate($product), 'rule_id');
    if ($actual !== $expected || $engine->blocksPublication($product) !== !empty($expected)) {
        fwrite(STDERR, "$label: expected " . json_encode($expected) . ', got ' . json_encode($actual) . PHP_EOL);
        exit(1);
    }
}
echo 'Rule engine contracts: 6 passed' . PHP_EOL;
