*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Collection/CollectionGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Collection/CollectionProcess.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Collection/CollectionPost.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesInvoice/SalesInvoicePost.py


*** Test Cases ***
1 - Able to process Collection by id
    [Documentation]    Able to process collection via API
    [Tags]  distadm   9.2    NRSZUANQ-44093
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
    When user processes created collection by id
    Then expected return status code 202

2 - Unable to process Collection in processed status
    [Documentation]    Unable to process collection in processed status via API
    [Tags]      distadm   9.2    NRSZUANQ-44093
    Given user retrieves token access as ${user_role}
    When user retrieves collection by STATUS = Y
    Then expected return status code 200
    When user processes processed collection by id
    Then expected return status code 400