*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesInvoice/SalesInvoicePost.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Picklist/PickListGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Picklist/PickListPost.py

*** Test Cases ***
1 - Able to post prime picklist with confirmed invoice in Open status and return 201
    [Documentation]    Able to post prime Picklist in Open Status
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

2 - Able to post prime picklist with confirmed invoice in Confirmed status and return 201
    [Documentation]    Able to post prime Picklist in Confirmed status
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
    ...    STATUS=Confirmed
    ...    INV_ID=${res_bd_invoice_id}
    When user creates picklist with fixed data
    Then expected return status code 201

3 - Unable to post picklist using HQ access and return 403
    [Documentation]    Unable to post picklist using other than distributor user
    [Tags]    hqadm
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as distadm
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
    Given user retrieves token access as ${user_role}
    When user creates picklist with fixed data
    Then expected return status code 403

4 - Unable to post non-prime picklist with prime invoice and return 400
    [Documentation]    Unable to post non-prime picklist with prime invoie
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
    ...    PRIME_FLAG=NON_PRIME
    ...    WH_CD=NP-UWH
    ...    PICK_DOC_TYPE=Invoice
    ...    DOCUMENT_TYPE=Selling
    ...    DELIVERY_ROUTE_CD=KDEL01
    ...    VAN_CD=VANN01
    ...    STATUS=Open
    ...    INV_ID=${res_bd_invoice_id}
    When user creates picklist with fixed data
    Then expected return status code 400