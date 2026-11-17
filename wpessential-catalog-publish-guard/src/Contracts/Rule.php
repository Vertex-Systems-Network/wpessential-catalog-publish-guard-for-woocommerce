<?php
namespace WPEssential\CatalogPublishGuard\Contracts;

interface Rule {
    /** Stable registry ID, e.g. BAS-001. */
    public function id(): string;

    /** Return an issue array or null when the product passes. */
    public function evaluate(\WC_Product $product): ?array;
}
