*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/VisionStore/ScoreCardSetup/ScoreCardSetupGet.py

*** Test Cases ***
1 - Able to retrieve score card setup listing
    [Documentation]    To retrieve score card setup listing
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieve score card setup listing
    Then expected return status code 200

2 - Able to retrieve score card setup details
    [Documentation]    To retrieve score card setup details
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieve score card setup details
    Then expected return status code 200
    When user retrieve vision store assignment
    Then expected return status code 200
