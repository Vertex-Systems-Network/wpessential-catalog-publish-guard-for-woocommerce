<?php
namespace WPEssential\CatalogPublishGuard\Core;

final class Plugin {
    public static function boot(): void {
        // Registration of source-specific adapters follows verified Woo lifecycle tests.
        do_action( 'wpcpg_free_loaded', WPCPG_FREE_VERSION );
    }
}
