*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/PosmManagement/PosmApproval/PosmApprovalGet.py


*** Test Cases ***
1 - Able to retrieve posm request approval
    [Documentation]  Able to retrieve posm request approval
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user retrieves posm request approval
    Then expected return status code 200