*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Maintenance/ModuleSetup/ModuleSetupPost.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Maintenance/ModuleSetup/ModuleSetupGet.py

*** Test Cases ***
1 - Able to retrieve all module setup
    [Documentation]    Able to retrieve all module setup
    ...    This is not applicable to distadm, hqadm
    [Tags]    sysimp    9.0
    Given user retrieves token access as ${user_role}
    When user retrieves all module setup
    Then expected return status code 200

2 - Able to retrieve created module setup
    [Documentation]    Able to retrieve created module setup
    ...    This is not applicable to distadm, hqadm
    [Tags]    sysimp    9.0
    Given user retrieves token access as ${user_role}
    When user creates module setup using random data
    Then expected return status code 201
    When user retrieves created module setup
    Then expected return status code 200