*** Settings ***
Documentation  This file models the product page
Library     robotkeywords.SeleniumKeywords
Resource    objectmap.robot

*** Keywords ***

Verify Product Page Description
    [Documentation]  Verifies the product page description
    [Arguments]  ${expected_text}
    ${actual_text}  element get text  ${PRODUCT-PAGE-PRODUCT-DESC}
    should contain   ${actual_text}  ${expected_text}

Click On Home Breadcrumb Link
    [Documentation]  Clicks on home link
    element left click  ${PRODUCT-PAGE-HOME-LINK}

Get Product Price
    [Documentation]  Gets the product price
    ${price}  element get text  ${PRODUCT-PAGE-PRODUCT-PRICE}
    [Return]  ${price}

Click On Add To Cart Button
    [Documentation]  Clicks add to cart button
    element left click  ${PRODUCT-PAGE-ADD-TO-CART-BUTTON}

Click On Color Brown Checkbox
    [Documentation]  Clicks on the color brown checkbox
    check box check   ${PRODUCT-PAGE-COLOR-BROWN-CHECKBOX}

Verify Cart Popup Is Displayed
    [Documentation]  Verifies the cart popup window
    iframe switch to default content
    iframe switch to by locator  ${CART-IFRAME-LOCATOR}
    element should be displayed  ${CART-LOCATOR}

Verify Item Added To Cart
    [Documentation]  Verifies the item is in the cart
    [Arguments]  ${expected_text}
    iframe switch to default content
    iframe switch to by locator  ${CART-IFRAME-LOCATOR}
    ${actual_text}  element get text  ${PRODUCT-PAGE-CART-ITEM}
    should contain   ${actual_text}  ${expected_text}

Verify Cart Item Price
    [Documentation]  Verifies the cart price
    [Arguments]  ${expected_text}
    iframe switch to default content
    iframe switch to by locator  ${CART-IFRAME-LOCATOR}
    ${actual_text}  element get text  ${CART-PRICE}
    should contain   ${actual_text}  ${expected_text}

Click On View Cart Button
    [Documentation]  Clicks on the view cart
    iframe switch to default content
    iframe switch to by locator  ${CART-IFRAME-LOCATOR}
    element left click  ${VIEW-CART}
