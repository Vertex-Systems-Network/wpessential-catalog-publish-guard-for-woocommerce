<?php
namespace WPEssential\CatalogPublishGuard\Rules;

use WPEssential\CatalogPublishGuard\Contracts\Rule;

final class TitleRequired implements Rule {
    public function id(): string { return 'BAS-001'; }

    public function evaluate(\WC_Product $product): ?array {
        if (trim(wp_strip_all_tags($product->get_name('edit'))) !== '') {
            return null;
        }
        return [
            'severity' => 'block',
            'field_path' => 'name',
            'explanation' => __('Enter a product title before publishing.', 'wpessential-catalog-publish-guard'),
        ];
    }
}
