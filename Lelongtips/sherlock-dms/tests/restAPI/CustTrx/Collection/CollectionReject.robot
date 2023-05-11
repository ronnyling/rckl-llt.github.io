*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Collection/CollectionGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Collection/CollectionProcess.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Collection/CollectionPost.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Collection/CollectionReject.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesInvoice/SalesInvoicePost.py


*** Test Cases ***
1 - Able to reject Collection by id
    [Documentation]    Able to reject collection via API
    [Tags]      distadm
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'CNPD001' with uom 'EA:5'
    When user creates invoice with fixed data
    Then expected return status code 200
    When user creates collection with random data
    Then expected return status code 202
    When user rejects created collection by id
    Then expected return status code 200

2 - Unable to process Collection in rejected status
    [Documentation]    Unable to process collection in rejected status via API
    [Tags]      distadm
    Given user retrieves token access as ${user_role}
    When user retrieves collection by STATUS = C
    Then expected return status code 200
    When user processes processed collection by id
    Then expected return status code 400