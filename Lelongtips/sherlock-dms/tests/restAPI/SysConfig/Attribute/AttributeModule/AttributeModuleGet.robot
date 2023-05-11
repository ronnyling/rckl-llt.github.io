*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Attribute/AttributeModule/AttributeModulePost.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Attribute/AttributeModule/AttributeModuleGet.py


*** Test Cases ***
1 - Able to get all attribute module data
    [Documentation]    To get all attribute module
    [Tags]      sysimp    9.0
    Given user retrieves token access as ${user_role}
    When user retrieves all attribute module
    Then expected return status code 200

2 - Able to get attribute module data by id
    [Documentation]    To get attribute module using  id
    [Tags]     sysimp    9.0
    Given user retrieves token access as ${user_role}
    When user creates attribute module using random data
    Then expected return status code 201
    When user retrieves created attribute module
    Then expected return status code 200

