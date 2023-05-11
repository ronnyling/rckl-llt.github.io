*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/PurchaseOrder/PurchaseOrderGet.py


*** Test Cases ***
1 - Able to retrieve all purchase order
    [Documentation]  Able to retrieve all purchase order
    [Tags]    distadm   hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves all purchase order
    Then expected return status code 200

2 - Able to retrieve purchase order by id
    [Documentation]  Able to retrieve purchase order by id
    [Tags]    distadm   hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves all purchase order
    Then expected return status code 200
    When user retrieves purchase order by id
    Then expected return status code 200