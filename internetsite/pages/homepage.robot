*** Settings ***
Documentation  This file models the lovelytests homepage
Library     robotkeywords.SeleniumKeywords
Resource    objectmap.robot

*** Keywords ***

Verify Home Page Logo Is Displayed
    [Documentation]  Verifies the home page logo is displayed
    element should be displayed  ${HOMEPAGE-LOGO-IMAGE}

Click On Shoes Product
    [Documentation]  Clicks on shoes product
    element left click  ${HOMEPAGE-SHOES-PRODUCT}

Click On Lipstick Product
    [Documentation]  Clicks on lipstick product
    element left click  ${HOMEPAGE-LIPSTICK-PRODUCT}

Click On Shirt Product
    [Documentation]  Clicks on shirt product
    element left click  ${HOMEPAGE-SHIRT-PRODUCT}

Click On Whatch Product
    [Documentation]  Clicks on whatch product
    element left click  ${HOMEPAGE-SHIRT-PRODUCT}
