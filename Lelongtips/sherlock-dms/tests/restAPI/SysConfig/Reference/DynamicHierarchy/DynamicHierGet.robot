*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot

Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Reference/DynamicHierarchy/DynamicHierGet.py


*** Test Cases ***
1 - Able to retrieve all dynamic hierarchy data
    [Documentation]  To retrieve all dynamic hierarchy record via API
    [Tags]    sysimp     9.0
    Given user retrieves token access as ${user_role}
    When user gets all dynamic hierarchy data
    Then expected return status code 200

