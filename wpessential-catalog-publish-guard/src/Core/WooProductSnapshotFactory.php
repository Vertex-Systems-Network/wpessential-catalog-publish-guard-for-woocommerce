<?php
namespace WPEssential\CatalogPublishGuard\Core;

use WPEssential\CatalogPublishGuard\Contracts\ProductSnapshot;
use WPEssential\CatalogPublishGuard\Contracts\ProductSnapshotFactory;

final class WooProductSnapshotFactory implements ProductSnapshotFactory {
    public function fromProduct(\WC_Product $product, string $source): ProductSnapshot {
        return new ProductSnapshot($product, $source);
    }
}
