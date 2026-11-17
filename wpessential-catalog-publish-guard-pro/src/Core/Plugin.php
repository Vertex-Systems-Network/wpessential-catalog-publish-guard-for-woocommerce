<?php
namespace WPEssential\CatalogPublishGuardPro\Core;

final class Plugin {
    public static function boot(): void {
        do_action( 'wpcpg_pro_loaded' );
    }
}
