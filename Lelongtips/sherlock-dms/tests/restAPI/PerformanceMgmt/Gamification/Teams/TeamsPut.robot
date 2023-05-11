*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Teams/TeamsPost.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Teams/TeamsPut.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Teams/TeamsDelete.py

*** Test Cases ***
1- Unable to edit Team Code once it is created
    [Documentation]    This test is to ensure Team Code is non-editable once it is created
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27094
    [Teardown]    user deletes created team setup
    Given user retrieves token access as ${user_role}
    ${TeamSetupDetails}=    create dictionary
    ...    TEAM_CD=TestingEditableCode
    set test variable    ${TeamSetupDetails}
    When user creates team setup using fixed data
    Then expected return status code 201
    ${TeamSetupDetails}=    create dictionary
    ...    TEAM_CD=Uneditable
    set test variable    ${TeamSetupDetails}
    When user updates created team setup using fixed data
    Then expected return status code 400

2 - Able to update created team setup
    [Documentation]    Able to update created team setup
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27090    NRSZUANQ-27089
    [Setup]    user retrieves token access as ${user_role}
    [Teardown]    user deletes created team setup
    When user creates team setup using random data
    Then expected return status code 201
    ${TeamSetupDetails}=    create dictionary
    ...    TEAM_NAME=TestingTeamName
    set test variable    ${TeamSetupDetails}
    When user updates created team setup using fixed data
    Then expected return status code 200

3- Unable to update team setup using distadm
    [Documentation]    This test is to ensure only hqadm and sysimp has the PUT access for team setup
    [Tags]    distadm    9.1    NRSZUANQ-27089
    [Setup]    user retrieves token access as hqadm
    When user creates team setup using random data
    Then expected return status code 201
    ${TeamSetupDetails}=    create dictionary
    ...    TEAM_NAME=TestingTeam
    set test variable    ${TeamSetupDetails}
    When user retrieves token access as ${user_role}
    And user updates created team setup using fixed data
    Then expected return status code 403
    When user retrieves token access as hqadm
    And user deletes created team setup
    Then expected return status code 200
