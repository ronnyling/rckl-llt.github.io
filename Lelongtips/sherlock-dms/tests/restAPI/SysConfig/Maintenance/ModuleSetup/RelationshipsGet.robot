*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Maintenance/ModuleSetup/RelationshipsPost.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Maintenance/ModuleSetup/RelationshipsGet.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Maintenance/ModuleSetup/ModuleSetupPost.py

*** Test Cases ***
1 - Able to retrieve all relationships in created module setup
    [Documentation]    Able to retrieve all relationships in module setup
    ...    This is not applicable to distadm, hqadm
    [Tags]    sysimp    9.0
    Given user retrieves token access as ${user_role}
    When user creates total 2 module setup using random data
    Then expected return status code 201
    When user creates relationships in 1st module setup using random data
    Then expected return status code 201
    When user retrieves all relationships in 1st module setup
    Then expected return status code 200

2 - Able to retrieve created relationships in module setup
    [Documentation]    Able to retrieve created relationships in module setup
    ...    This is not applicable to distadm, hqadm
    [Tags]    sysimp    9.0
    Given user retrieves token access as ${user_role}
    When user creates total 2 module setup using random data
    Then expected return status code 201
    When user creates relationships in 1st module setup using random data
    Then expected return status code 201
    When user retrieves created relationships in 1st module setup
    Then expected return status code 200
