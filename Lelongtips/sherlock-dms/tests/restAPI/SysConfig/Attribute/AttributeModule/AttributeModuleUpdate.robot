*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Attribute/AttributeModule/AttributeModulePost.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Attribute/AttributeModule/AttributeModuleGet.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Attribute/AttributeModule/AttributeModuleDelete.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Attribute/AttributeModule/AttributeModulePut.py

*** Test Cases ***
1 - Able to update attribute module
    [Documentation]    To update created attribute module data
    [Tags]      sysimp    9.0
    Given user retrieves token access as ${user_role}
    When user creates attribute module using random data
    Then expected return status code 201
    When user retrieves created attribute module
    Then expected return status code 200
    &{amdetails_put}=    create dictionary
    ...    MODULE=Updated module Description
    set test variable   &{amdetails_put}
    When user update created attribute module
    Then expected return status code 200
    When user deletes created attribute module
    Then expected return status code 200
