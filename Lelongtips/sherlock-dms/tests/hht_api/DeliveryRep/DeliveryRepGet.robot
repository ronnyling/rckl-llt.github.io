*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/DeliveryRep/DeliveryRepGet.py


*** Test Cases ***
1 - Able to retrieve picklist
    [Documentation]    Able to retrieve picklist from Back Office
    [Tags]    salespersondev    DeliveryRep    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves picklist
    Then expected return status code 204

2 - Able to retrieve message
    [Documentation]    Able to retrieve message from Back Office
    [Tags]    salespersondev    DeliveryRep    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves message
    Then expected return status code 200

3 - Able to retrieve picklist-cust-invoice
    [Documentation]    Able to retrieve picklist-cust-invoice from Back Office
    [Tags]    salespersondev    DeliveryRep    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves picklist cust invoice
    Then expected return status code 204

4 - Able to retrieve picklist-invoice
    [Documentation]    Able to retrieve picklist-invoice from Back Office
    [Tags]    salespersondev    DeliveryRep    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves picklist invoice
    Then expected return status code 204

5 - Able to retrieve picklist-delivery-sheet
    [Documentation]    Able to retrieve picklist-delivery-sheet from Back Office
    [Tags]    salespersondev    DeliveryRep    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves picklist delivery sheet
    Then expected return status code 200

6 - Able to retrieve step of call
    [Documentation]    Able to retrieve step of call from Back Office
    [Tags]    salespersondev    DeliveryRep    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves step of call
    Then expected return status code 204

