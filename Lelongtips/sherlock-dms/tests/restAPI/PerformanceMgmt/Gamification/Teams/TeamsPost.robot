*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Teams/TeamsPost.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Teams/TeamsDelete.py

*** Test Cases ***
1- Validate value for status
    [Documentation]    This test is to ensure only Active and Inactive value selection for status radio button
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1
    [Template]    Validate value for status
    #status    #expected_status
    A          201
    I          201
    AI         400

2- Verify data type length for Team Code and Team Name
    [Documentation]    This test is to ensure Team Code and Team Name has correct length
    [Tags]    hqadm    sysimp    9.1
    [Template]    Verify data length for team code and team name
    #team_code_length    #team_name_length    #expected_status
    ${20}                   ${50}                    201
    ${19}                   ${49}                    201
    ${21}                   ${51}                    400

3- Verify Team Code is unique
    [Documentation]    This test is to ensure Team Code is unique across the system
    [Tags]    hqadm    sysimp    9.1
    [Teardown]    user deletes created team setup
    Given user retrieves token access as ${user_role}
    ${TeamSetupDetails}=    create dictionary
    ...    TEAM_CD=TESTINGCODENO
    set test variable    ${TeamSetupDetails}
    When user creates team setup using fixed data
    Then expected return status code 201
    When user creates team setup using fixed data
    Then expected return status code 409

4 - Validate mandatory fields for team setup
    [Documentation]    Validate mandatory fields for team setup
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1
    [Template]    Validate mandatory fields for team setup
    #key             #value         #expected_result
    TEAM_CD          ${empty}          400
    TEAM_NAME        ${empty}          400
    STATUS           ${empty}          400

5- Able to create team setup using random data
    [Documentation]    This test is to create team setup using random data
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1
    [Teardown]    user deletes created team setup
    Given user retrieves token access as ${user_role}
    When user creates team setup using random data
    Then expected return status code 201

6- Unable to create team setup using distadm
    [Documentation]    This test is to ensure only hqadm and sysimp has the POST access for team setup
    [Tags]    distadm    9.1
    Given user retrieves token access as ${user_role}
    When user creates team setup using random data
    Then expected return status code 403

7- Unable to create team setup without assignment part
    [Documentation]    This test is to ensure assignment part is filled with data
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1
    Given user retrieves token access as ${user_role}
    ${TeamSetupDetails}=    create dictionary
    ...    ASSIGNMENTS=[]
    set test variable    ${TeamSetupDetails}
    When user creates team setup using fixed data
    Then expected return status code 400