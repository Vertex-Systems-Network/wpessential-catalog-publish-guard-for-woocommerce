<?php
/**
 * Plugin Name: WPEssential Catalog Publish Guard Pro for WooCommerce
 * Description: Advanced catalog publication workflows.
 * Version: 0.1.0-dev
 * Requires PHP: 7.4
 * Requires Plugins: wpessential-catalog-publish-guard
 * License: GPL-2.0-or-later
 * Text Domain: wpessential-catalog-publish-guard-pro
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

add_action( 'plugins_loaded', static function () {
    if ( ! defined( 'WPCPG_FREE_VERSION' ) || ! class_exists( '\\WPEssential\\CatalogPublishGuard\\Core\\Plugin' ) ) {
        add_action( 'admin_notices', static function () {
            if ( current_user_can( 'activate_plugins' ) ) {
                echo '<div class="notice notice-error"><p>' . esc_html__( 'Catalog Publish Guard Pro requires the active Free plugin.', 'wpessential-catalog-publish-guard-pro' ) . '</p></div>';
            }
        } );
        return;
    }
    $autoload = __DIR__ . '/vendor/autoload.php';
    if ( ! is_readable( $autoload ) ) {
        add_action( 'admin_notices', static function () {
            if ( current_user_can( 'activate_plugins' ) ) {
                echo '<div class="notice notice-error"><p>' . esc_html__( 'Catalog Publish Guard Pro is missing its packaged dependencies.', 'wpessential-catalog-publish-guard-pro' ) . '</p></div>';
            }
        } );
        return;
    }
    require_once $autoload;
    \WPEssential\CatalogPublishGuardPro\Core\Plugin::boot();
}, 20 );
