*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/ExecutionResult/AuditResult/AuditResultPost.py

*** Test Cases ***
1 - Able to retrieve all audit result for Planogram
    [Documentation]  Able to retrieve all audit result for planogram
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user filters audit result for planogram
    Then expected return status code 200

2 - Able to retrieve audit result for Planogram based on Compliance = Yes
    [Documentation]  Able to retrieve audit result for planogram where Compliance = Yes
    [Tags]    hqadm    9.2
    ${result_details}=    create dictionary
    ...    compliance=T
    set test variable  &{result_details}
    Given user retrieves token access as hqadm
    When user filters audit result for planogram
    Then expected return status code 200

3 - Able to retrieve audit result for Planogram based on Compliance = No
    [Documentation]  Able to retrieve audit result for planogram where Compliance = No
    [Tags]    hqadm    9.2
    ${result_details}=    create dictionary
    ...    compliance=F
    set test variable  &{result_details}
    Given user retrieves token access as hqadm
    When user filters audit result for planogram
    Then expected return status code 200

