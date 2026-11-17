<?php
namespace WPEssential\CatalogPublishGuard\Core;

use WPEssential\CatalogPublishGuard\Contracts\Rule;

final class RuleEngine {
    /** @var Rule[] */
    private $rules;

    /** @param Rule[] $rules */
    public function __construct(array $rules) {
        foreach ($rules as $rule) {
            if (!$rule instanceof Rule) {
                throw new \InvalidArgumentException('Every rule must implement Rule.');
            }
        }
        $this->rules = $rules;
    }

    /** @return array<int,array<string,string>> */
    public function evaluate(\WC_Product $product): array {
        $issues = [];
        foreach ($this->rules as $rule) {
            $issue = $rule->evaluate($product);
            if ($issue !== null) {
                $issue['rule_id'] = $rule->id();
                $issues[] = $issue;
            }
        }
        return $issues;
    }

    public function blocksPublication(\WC_Product $product): bool {
        foreach ($this->evaluate($product) as $issue) {
            if ($issue['severity'] === 'block') {
                return true;
            }
        }
        return false;
    }
}
