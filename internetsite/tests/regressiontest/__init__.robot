*** Settings ***
Test Setup          Setup Test Case
Test Teardown       Teardown Test Case
Suite Setup         Setup Test Suite
Suite Teardown      Teardown Test Suite
Resource            ../../pages/setupteardown.robot
Library             robotkeywords.FrameworkKeywords


*** Keywords ***

Setup Test Suite
    [Documentation]  Sets up the test suite
    setup framework
    driver open browser

Teardown Test Suite
    [Documentation]  Sets up the test suite
    driver close browser
    close framework
