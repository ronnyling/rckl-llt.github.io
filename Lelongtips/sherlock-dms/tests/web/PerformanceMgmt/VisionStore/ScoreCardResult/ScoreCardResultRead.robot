*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/VisionStore/ScoreCardResult/ScoreCardResultListing.py

*** Test Cases ***
1 - Able to retrieve all vs score card result
    [Documentation]    Able to retrieve all vs score card result
    [Tags]    sysimp    hqadm    distadm
    When user navigates to menu Performance Management | Vision Store | Score Card Result
    Then user retrieved all vs score card result
