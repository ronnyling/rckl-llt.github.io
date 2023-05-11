*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Teams/TeamsPost.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Teams/TeamsDelete.py

*** Test Cases ***
1 - Able to delete created team setup
    [Documentation]    Able to delete created team setup
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27090    NRSZUANQ-27089
    [Setup]    user retrieves token access as ${user_role}
    When user creates team setup using random data
    Then expected return status code 201
    When user deletes created team setup
    Then expected return status code 200

2- Unable to update team setup using distadm
    [Documentation]    This test is to ensure only hqadm and sysimp has the PUT access for team setup
    [Tags]    distadm    9.1    NRSZUANQ-27089
    [Setup]    user retrieves token access as hqadm
    When user creates team setup using random data
    Then expected return status code 201
    ${TeamSetupDetails}=    create dictionary
    ...    TEAM_NAME=TestingTeam
    set test variable    ${TeamSetupDetails}
    When user retrieves token access as ${user_role}
    And user deletes created team setup
    Then expected return status code 403
    When user retrieves token access as hqadm
    And user deletes created team setup
    Then expected return status code 200

