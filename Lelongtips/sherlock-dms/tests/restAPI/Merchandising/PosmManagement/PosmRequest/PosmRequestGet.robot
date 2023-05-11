*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/PosmManagement/PosmRequest/PosmRequestGet.py


*** Test Cases ***
1 - Able to retrieve posm request
    [Documentation]  Able to retrieve posm request approval
    [Tags]    distadm    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves posm request
    Then expected return status code 200