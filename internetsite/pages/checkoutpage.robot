*** Settings ***
Documentation  This file models the checkout page
Library     robotkeywords.SeleniumKeywords
Resource    objectmap.robot

*** Keywords ***


Verify Checkout Error Is Displayed
    [Documentation]  Verifies checkout error
    iframe switch to default content
    iframe switch to by locator  ${CHECKOUTPAGE-POPUP-IFRAME-LOCATOR}
    element should be displayed  ${CHECKOUTPAGE-CHECKOUT-ERROR}

Click On Checkout Button
    [Documentation]  Clicks on the view cart
    iframe switch to default content
    iframe switch to by locator  ${CHECKOUTPAGE-IFRAME-LOCATOR}
    element wait to be displayed  ${CHECKOUTPAGE-CHECKOUT-BUTTON}
    element left click  ${CHECKOUTPAGE-CHECKOUT-BUTTON}
