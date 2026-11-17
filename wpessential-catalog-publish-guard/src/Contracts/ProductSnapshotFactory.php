<?php
namespace WPEssential\CatalogPublishGuard\Contracts;

interface ProductSnapshotFactory {
    /** The caller must supply the fully assembled, unsaved or persisted WC product. */
    public function fromProduct(\WC_Product $product, string $source): ProductSnapshot;
}
