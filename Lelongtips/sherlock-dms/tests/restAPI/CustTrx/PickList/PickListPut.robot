*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Picklist/PickListGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Picklist/PickListPost.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Picklist/PickListPut.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesInvoice/SalesInvoicePost.py

*** Test Cases ***
1 - Able to update prime picklist and return 200
    [Documentation]    Able to update Picklist
    [Tags]    distadm
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'AdeCP001' with uom 'EA:2'
    When user creates invoice with fixed data
    Then expected return status code 200
    ${pl_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    WH_CD=CCCC
    ...    PICK_DOC_TYPE=Invoice
    ...    DOCUMENT_TYPE=Selling
    ...    DELIVERY_ROUTE_CD=drronnyxhh
    ...    VAN_CD=vanDR_wo_hht
    ...    STATUS=Open
    ...    INV_ID=${res_bd_invoice_id}
    When user creates picklist with fixed data
    Then expected return status code 201
    When user updates picklist with valid data
    Then expected return status code 200
    When user retrieves picklist by id
    Then expected return status code 200

2 - Unable to update picklist with past actual delivery date and return 400
    [Documentation]    Unable to update picklist with past actual delivery date
    [Tags]    distadm
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'AdeCP001' with uom 'EA:2'
    When user creates invoice with fixed data
    Then expected return status code 200
    ${pl_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    WH_CD=CCCC
    ...    PICK_DOC_TYPE=Invoice
    ...    DOCUMENT_TYPE=Selling
    ...    DELIVERY_ROUTE_CD=drronnyxhh
    ...    VAN_CD=vanDR_wo_hht
    ...    STATUS=Open
    ...    INV_ID=${res_bd_invoice_id}
    When user creates picklist with fixed data
    Then expected return status code 201
    When user updates picklist with invalid data
    Then expected return status code 400