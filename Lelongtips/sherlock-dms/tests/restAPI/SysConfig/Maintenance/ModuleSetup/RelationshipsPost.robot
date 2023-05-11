*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Maintenance/ModuleSetup/RelationshipsPost.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Maintenance/ModuleSetup/ModuleSetupPost.py

*** Test Cases ***
1 - Able to create relationships in module setup using random data
    [Documentation]    Able to create relationships in module setup using random data
    ...    This is not applicable to distadm, hqadm
    [Tags]    sysimp    9.0
    Given user retrieves token access as ${user_role}
    When user creates total 2 module setup using random data
    Then expected return status code 201
    When user creates relationships in 1st module setup using random data
    Then expected return status code 201

2 - Able to create relationships in module setup using fixed data
    [Documentation]    Able to create relationships in module setup using fixed data
    ...    This is not applicable to distadm, hqadm
    [Tags]    sysimp    9.0
    Given user retrieves token access as ${user_role}
    When user creates total 2 module setup using random data
    Then expected return status code 201
    ${RelationshipsDetails}=    create dictionary
    ...    TYPE=1
    ...    ORDER_SEQ=${1}
    set test variable    ${RelationshipsDetails}
    And user verified relationships in 1st module setup is created
