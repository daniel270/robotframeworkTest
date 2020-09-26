*** Variables ***

# Homepage
${HOMEPAGE-LOGO-IMAGE}     css-selector:[data-testid='mesh-container-content'] a[data-testid=linkElement]
${HOMEPAGE-SHOES-PRODUCT}     css-selector:div.slick-active img[alt='Shoes']
${HOMEPAGE-LIPSTICK-PRODUCT}     css-selector:div.slick-active img[alt='Lipstick']
${HOMEPAGE-SHIRT-PRODUCT}     css-selector:div.slick-active img[alt='Shirt']
${HOMEPAGE-WATCH-PRODUCT}     css-selector:div.slick-active img[alt='Watch']

#Product Page
${PRODUCT-PAGE-PRODUCT-DESC}     css-selector:div [data-hook='description'] p
${PRODUCT-PAGE-HOME-LINK}     css-selector:div [data-hook='breadcrumbs'] a
${PRODUCT-PAGE-PRODUCT-PRICE}     css-selector:div [data-hook='formatted-primary-price']
${PRODUCT-PAGE-ADD-TO-CART-BUTTON}     xpath://div/button/span[text()='Add to Cart']
${PRODUCT-PAGE-COLOR-BROWN-CHECKBOX}     xpath://input[@aria-label='Brown']/following-sibling::span
${PRODUCT-PAGE-CART-ITEM}     css-selector:div [data-hook='cart-widget-item'] .item-name
${CART-PRICE}     css-selector:div [data-hook='cart-widget-item-price']
${CART-LOCATOR}     css-selector:div.minicart.active
${CART-IFRAME-LOCATOR}     xpath://iframe[contains(@name,'tpapopup')]
${VIEW-CART}     css-selector:div a[data-hook='widget-view-cart-button']

# Checkout iframe
${CHECKOUTPAGE-IFRAME-LOCATOR}     xpath://iframe[@title='Cart Page']
${CHECKOUTPAGE-CHECKOUT-BUTTON}     css-selector:div [data-hook='checkout-button'] button
${CHECKOUTPAGE-CHECKOUT-ERROR}     css-selector:div [data-hook='error-component'] span[data-hook='error-title']
${CHECKOUTPAGE-POPUP-IFRAME-LOCATOR}     xpath://iframe[@title='Modal Dialog']
