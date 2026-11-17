<?php
namespace WPEssential\CatalogPublishGuard\Contracts;

/** Immutable validation input assembled from WooCommerce CRUD objects. */
final class ProductSnapshot {
    /** @var \WC_Product */
    private $product;
    /** @var string */
    private $source;

    public function __construct(\WC_Product $product, string $source) {
        if ($source === '') {
            throw new \InvalidArgumentException('Validation source must be named.');
        }
        $this->product = clone $product;
        $this->source = $source;
    }

    public function product(): \WC_Product { return clone $this->product; }
    public function source(): string { return $this->source; }
    public function productId(): int { return (int) $this->product->get_id(); }
}
