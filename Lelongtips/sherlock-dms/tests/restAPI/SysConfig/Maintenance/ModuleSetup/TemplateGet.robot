*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Maintenance/ModuleSetup/FieldsPost.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Maintenance/ModuleSetup/TemplatePost.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Maintenance/ModuleSetup/TemplateGet.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Maintenance/ModuleSetup/ModuleSetupPost.py

*** Test Cases ***
1 - Able to retrieve all template in created module setup
    [Documentation]    Able to retrieve all fields in module setup
    ...    This is not applicable to distadm, hqadm
    [Tags]    sysimp    9.0
    Given user retrieves token access as ${user_role}
    When user creates module setup using random data
    Then expected return status code 201
    When user creates fields in module setup using random data
    Then expected return status code 201
    When user creates template in module setup using random data
    Then expected return status code 201
    When user retrieves all template in module setup
    Then expected return status code 200

2 - Able to retrieve created template in module setup
    [Documentation]    Able to retrieve created template in module setup
    ...    This is not applicable to distadm, hqadm
    [Tags]    sysimp    9.0
    Given user retrieves token access as ${user_role}
    When user creates module setup using random data
    Then expected return status code 201
    When user creates fields in module setup using random data
    Then expected return status code 201
    When user creates template in module setup using random data
    Then expected return status code 201
    When user retrieves created template in module setup
    Then expected return status code 200
