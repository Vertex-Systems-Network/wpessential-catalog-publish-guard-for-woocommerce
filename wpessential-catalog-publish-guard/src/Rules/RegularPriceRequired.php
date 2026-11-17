<?php
namespace WPEssential\CatalogPublishGuard\Rules;

use WPEssential\CatalogPublishGuard\Contracts\Rule;

final class RegularPriceRequired implements Rule {
    public function id(): string { return 'PRC-001'; }

    public function evaluate(\WC_Product $product): ?array {
        // Variable parents obtain prices from children. External and grouped products
        // may legitimately omit a WooCommerce price.
        if (!in_array($product->get_type(), ['simple', 'variation'], true)) {
            return null;
        }
        if ($product->get_price('edit') !== '') {
            return null; // The string "0" is an explicitly set price.
        }
        return [
            'severity' => 'block',
            'field_path' => 'regular_price',
            'explanation' => __('Set a price before publishing this product.', 'wpessential-catalog-publish-guard'),
        ];
    }
}
