*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesInvoice/SalesInvoicePost.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Picklist/PickListGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Picklist/PickListPost.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Picklist/PickListConfirm.py

*** Test Cases ***
1 - Able to confirm prime picklist with confirmed invoice and return 200
    [Documentation]    Able to confirm Picklist
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
    When user confirms picklist
    Then expected return status code 201

