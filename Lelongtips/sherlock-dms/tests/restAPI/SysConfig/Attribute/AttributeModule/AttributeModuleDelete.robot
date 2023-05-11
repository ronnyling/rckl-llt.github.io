*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Attribute/AttributeModule/AttributeModulePost.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Attribute/AttributeModule/AttributeModuleGet.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Attribute/AttributeModule/AttributeModuleDelete.py


*** Test Cases ***
1 - Able to delete attribute module
    [Documentation]    To delete attribute module using random data
    [Tags]      sysimp    9.0
    Given user retrieves token access as ${user_role}
    When user creates attribute module using random data
    Then expected return status code 201
    When user retrieves created attribute module
    Then expected return status code 200
    When user deletes created attribute module
    Then expected return status code 200
