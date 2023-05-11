*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot

Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Attribute/AttributeUsage/AttributeUsageGet.py


*** Test Cases ***
1 - Able to get all attribute usage data
    [Documentation]    To get all attribute usage
    [Tags]      sysimp    9.0
    Given user retrieves token access as ${user_role}
    When user retrieves all attribute usage
    Then expected return status code 200



