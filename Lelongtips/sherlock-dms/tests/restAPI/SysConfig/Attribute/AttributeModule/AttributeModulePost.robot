*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Attribute/AttributeModule/AttributeModulePost.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Attribute/AttributeModule/AttributeModuleGet.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Attribute/AttributeModule/AttributeModuleDelete.py

*** Test Cases ***
1 - Able to create attribute module using random data
    [Documentation]    To create attribute module using random data
    [Tags]      sysimp    9.0
    Given user retrieves token access as ${user_role}
    When user creates attribute module using random data
    Then expected return status code 201
     When user deletes created attribute module
    Then expected return status code 200

2 - Able to create attribute module using given data
    [Documentation]    To create attribute module using given data
    [Tags]     sysimp    9.0
    ${AMdetails}=   create dictionary
    ...    amCode=1234TestCD
    ...    amUsage=Test Module Field
    set test variable     &{AMdetails}
    Given user retrieves token access as ${user_role}
    When user creates attribute module using given data
    Then expected return status code 201
    When user deletes created attribute module
    Then expected return status code 200