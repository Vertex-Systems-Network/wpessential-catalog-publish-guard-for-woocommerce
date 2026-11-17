<?php
/**
 * Plugin Name: WPEssential Catalog Publish Guard for WooCommerce
 * Description: Checks product readiness before publication.
 * Version: 0.1.0-dev
 * Requires PHP: 7.4
 * Requires Plugins: woocommerce
 * License: GPL-2.0-or-later
 * Text Domain: wpessential-catalog-publish-guard
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

define( 'WPCPG_FREE_VERSION', '0.1.0-dev' );

add_action( 'plugins_loaded', static function () {
    if ( ! class_exists( 'WooCommerce' ) ) {
        add_action( 'admin_notices', static function () {
            if ( current_user_can( 'activate_plugins' ) ) {
                echo '<div class="notice notice-error"><p>' . esc_html__( 'Catalog Publish Guard requires WooCommerce.', 'wpessential-catalog-publish-guard' ) . '</p></div>';
            }
        } );
        return;
    }
    $autoload = __DIR__ . '/vendor/autoload.php';
    if ( ! is_readable( $autoload ) ) {
        add_action( 'admin_notices', static function () {
            if ( current_user_can( 'activate_plugins' ) ) {
                echo '<div class="notice notice-error"><p>' . esc_html__( 'Catalog Publish Guard is missing its packaged dependencies.', 'wpessential-catalog-publish-guard' ) . '</p></div>';
            }
        } );
        return;
    }
    require_once $autoload;
    \WPEssential\CatalogPublishGuard\Core\Plugin::boot();
} );
