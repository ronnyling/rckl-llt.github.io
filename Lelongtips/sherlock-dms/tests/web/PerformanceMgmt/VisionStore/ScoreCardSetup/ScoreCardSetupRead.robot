*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/VisionStore/ScoreCardSetupListPage.py

*** Test Cases ***
1 - Able to retrieve all vs score card
    [Documentation]    Able to retrieve all vs score card
    [Tags]    sysimp    hqadm    distadm    9.1    NRSZUANQ-28613
    When user navigates to menu Performance Management | Vision Store | Score Card Setup
    Then user retrieved all vs score card
