*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Maintenance/ModuleSetup/ModuleSetupPost.py

*** Test Cases ***
1 - Able to create module setup using random data
    [Documentation]    Able to create module setup using random data
    [Tags]    sysimp    9.0
    Given user retrieves token access as ${user_role}
    When user creates module setup using random data
    Then expected return status code 201

2 - Able to create module setup using fixed data
    [Documentation]    Able to create module setup using fixed data
    [Tags]    sysimp    9.0
    Given user retrieves token access as ${user_role}
    ${ModuleSetupDetails}=    create dictionary
    ...    LOGICAL_ID=TestingGivenData
    set test variable    ${ModuleSetupDetails}
    When user creates module setup using fixed data
    Then expected return status code 201
