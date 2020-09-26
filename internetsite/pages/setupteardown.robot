*** Settings ***
Documentation       This file contains the setup and teardown keywords
Library             robotkeywords.SeleniumKeywords
Library             robotkeywords.FrameworkKeywords
Resource            environment.robot

*** Keywords ***

Setup Test Case
    [Documentation]  Sets up the overall test suite
    driver open url    ${HOMEPAGE-URL}
    window maximize window

Teardown Test Case
    [Documentation]  Tears down the overall test suite
    # check if test fails
    run keyword if test failed  run keyword and continue on failure  Capture Failure ScreenShot
    window switch to main window

Capture Failure ScreenShot
    [Documentation]  Captures a screenshot on test failure
    driver save screen shot  ${TEST NAME}