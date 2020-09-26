*** Settings ***
Documentation    Basic tests for lovelysite to verify the home page and shopping cart. Also includes one failing test at the end
Library             robotkeywords.SeleniumKeywords
Resource            ../../pages/homepage.robot
Resource            ../../pages/setupteardown.robot
Resource            ../../pages/productpage.robot
Resource            ../../pages/checkoutpage.robot

*** Test Cases ***


Home Page Should Be Displayed
    [Documentation]  Test to check if an element is displayed
    Verify Home Page Logo Is Displayed

Navigate To Shoes Product
    [Documentation]  Navigates to shoes product page
    Verify Home Page Logo Is Displayed
    Click On Shoes Product
    Verify Product Page Description   I'm a pair of shoes
    Click On Home Breadcrumb Link
    Verify Home Page Logo Is Displayed

Navigate To Lipstick Product
    [Documentation]  Navigates to Lipstick product page
    Verify Home Page Logo Is Displayed
    Click On Lipstick Product
    Verify Product Page Description   I'm Lipstick
    Click On Home Breadcrumb Link
    Verify Home Page Logo Is Displayed

Add Shoes Product to Cart
    [Documentation]  Navigates to shoes product page
    Verify Home Page Logo Is Displayed
    Click On Shoes Product
    Verify Product Page Description   I'm a pair of shoes
    ${product_price}  Get Product Price
    Click On Color Brown Checkbox
    Click On Add To Cart Button
    Verify Cart Popup Is Displayed
    Verify Item Added To Cart  Shoes
    Verify Cart Item Price  ${product_price}
    Click On View Cart Button
    Click On Checkout Button
    Verify Checkout Error Is Displayed

Failing Test with invalid verification
    [Documentation]  Just to show a failing tests!
    Verify Home Page Logo Is Displayed
    Click On Lipstick Product
    Verify Product Page Description   I'm A Lipstick  # this line will cause the test to fail
