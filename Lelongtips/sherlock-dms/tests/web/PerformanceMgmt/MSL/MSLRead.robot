*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/MSL/MSLListPage.py

*** Test Cases ***
1 - Able to retrieve all msl
    [Documentation]    Able to retrieve all msl
    [Tags]    sysimp    hqadm    distadm    9.1    NRSZUANQ-28613
    When user navigates to menu Performance Management | Must Sell List
    Then user retrieved all msl
