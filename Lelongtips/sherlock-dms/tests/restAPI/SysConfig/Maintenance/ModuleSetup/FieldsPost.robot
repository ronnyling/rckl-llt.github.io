*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Maintenance/ModuleSetup/FieldsPost.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Maintenance/ModuleSetup/ModuleSetupPost.py

*** Test Cases ***
1 - Able to create fields in module setup using random data
    [Documentation]    Able to create fields in module setup using random data
    ...    This is not applicable to distadm, hqadm
    [Tags]    sysimp    9.0
    Given user retrieves token access as ${user_role}
    When user creates module setup using random data
    Then expected return status code 201
    When user creates fields in module setup using random data
    Then expected return status code 201

2 - Able to create fields in module setup using fixed data
    [Documentation]    Able to create fields in module setup using fixed data
    ...    This is not applicable to distadm, hqadm
    [Tags]    sysimp    9.0
    Given user retrieves token access as ${user_role}
    When user creates module setup using random data
    Then expected return status code 201
    ${FieldsDetails}=    create dictionary
    ...    LABEL=test_field
    ...    DESCRIPTION=test_field
    ...    FIELD=TEST_FIELD
    ...    TYPE=text
    ...    DISPLAY_TYPE=textfield
    set test variable    ${FieldsDetails}
    When user creates fields in module setup using fixed data
    Then expected return status code 201
