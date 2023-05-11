*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/ChequeProcessing/ChequeProcessingPost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonTypeGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesInvoice/SalesInvoicePost.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Collection/CollectionPost.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Collection/CollectionProcess.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Collection/CollectionGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesInvoice/SalesInvoicePost.py
Library          ${EXECDIR}${/}resources/TransactionFormula.py

Test Setup        run keywords
...               user retrieves token access as distadm
...               AND    user gets distributor by using code 'DistEgg'
...               AND    user retrieves reason type 'Cheque Processing'
...               AND    user retrieves all reasons

*** Test Cases ***
1 - Able to POST cheque filter to retrieve cheque by distributor using fixed collection period
    [Documentation]    Able to retrieve cheque by distributor based on filter
    [Tags]    distadm    9.2
    ${filter_details}=    create dictionary
    ...    COLLECTION_FROM_DATE=2021-04-01
    ...    COLLECTION_TO_DATE=2021-04-27
    ...    STATUS=All
    Given user retrieves token access as ${user_role}
    When user retrieves cheque by distributor
    Then expected return status code 200

2 - Able to POST cheque filter to retrieve cheque by distributor based on today collection
    [Documentation]    Able to retrieve cheque by distributor for today's collection
    [Tags]    fixlah        distadm    9.2
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'CNPD001' with uom 'EA:5'
    When user creates invoice with fixed data
    Then expected return status code 200
    ${payment_details}=    create dictionary
    ...     OTHER_PYMT_METHOD=Q
    ...     CHEQUE_AMT=${100}
    ...     DRAWEE_BANK_ID=D860BF7A:A58172FE-1187-4004-A857-6776084B872C
    set test variable   &{payment_details}
    When user creates collection with random data
    Then expected return status code 202
    When user processes created collection by id
    Then expected return status code 202
    When user retrieves cheque by distributor
    Then expected return status code 200

3 - Unable to POST cheque filter to retrieve cheque by distributor using hqadm
    [Documentation]    Unable to retrieve cheque by distributor using hqadm access
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user retrieves cheque by distributor
    Then expected return status code 403

4 - Able to POST collection cheque status as Clear
    [Documentation]    Able to update collection cheque status as clear
    [Tags]    distadm    9.2     test
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'CNPD001' with uom 'EA:5'
    When user creates invoice with fixed data
    Then expected return status code 200
    ${payment_details}=    create dictionary
    ...     OTHER_PYMT_METHOD=Q
    ...     CHEQUE_AMT=${100}
    ...     DRAWEE_BANK_ID=D860BF7A:A58172FE-1187-4004-A857-6776084B872C
    set test variable   &{payment_details}
    When user creates collection with random data
    Then expected return status code 202
    When user processes created collection by id
    Then expected return status code 202
    When user retrieves cheque by distributor
    Then expected return status code 200
    When user processes cheque as clear
    Then expected return status code 200

5 - Unable to POST collection cheque status as Clear for future dated cheque
    [Documentation]    Unable to update collection cheque status as clear for future dated cheque
    [Tags]       distadm    9.2
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'CNPD001' with uom 'EA:5'
    When user creates invoice with fixed data
    Then expected return status code 200
    ${payment_details}=    create dictionary
    ...     OTHER_PYMT_METHOD=Q
    ...     CHEQUE_AMT=${100}
    ...     DRAWEE_BANK_ID=D860BF7A:A58172FE-1187-4004-A857-6776084B872C
    ...     CHEQUE_DATE=2022-01-12
    set test variable   &{payment_details}
    When user creates collection with future data
    Then expected return status code 202
    When user processes created collection by id
    Then expected return status code 202
    When user retrieves cheque by distributor
    Then expected return status code 200
    When user processes cheque as clear
    Then expected return status code 400

6 - Able to POST collection cheque status as Bounce
    [Documentation]    Able to update collection cheque status as bounce
    [Tags]    distadm    9.2
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'CNPD001' with uom 'EA:5'
    When user creates invoice with fixed data
    Then expected return status code 200
    ${payment_details}=    create dictionary
    ...     OTHER_PYMT_METHOD=Q
    ...     CHEQUE_AMT=${100}
    ...     DRAWEE_BANK_ID=D860BF7A:A58172FE-1187-4004-A857-6776084B872C
    set test variable   &{payment_details}
    When user creates collection with random data
    Then expected return status code 202
    When user processes created collection by id
    Then expected return status code 202
    When user retrieves cheque by distributor
    Then expected return status code 200
    When user processes cheque as bounce
    Then expected return status code 200

7 - Unable to POST collection cheque status as Bounce for future dated cheque
    [Documentation]    Able to update collection cheque status as bounce
    [Tags]       distadm    9.2
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'CNPD001' with uom 'EA:5'
    When user creates invoice with fixed data
    Then expected return status code 200
    ${payment_details}=    create dictionary
    ...     OTHER_PYMT_METHOD=Q
    ...     CHEQUE_AMT=${300}
    ...     CHEQUE_DATE=2022-01-12
    ...     DRAWEE_BANK_ID=D860BF7A:A58172FE-1187-4004-A857-6776084B872C
    set test variable   &{payment_details}
    When user creates collection with future data
    Then expected return status code 202
    When user processes created collection by id
    Then expected return status code 202
    When user retrieves cheque by distributor
    Then expected return status code 200
    When user processes cheque as bounce
    Then expected return status code 400

8 - Unable to POST collection cheque status as Cancel for today's cheque
    [Documentation]    Able to update collection cheque status as cancel
    [Tags]    distadm    9.2
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'CNPD001' with uom 'EA:5'
    When user creates invoice with fixed data
    Then expected return status code 200
    ${payment_details}=    create dictionary
    ...     OTHER_PYMT_METHOD=Q
    ...     CHEQUE_AMT=${300}
    ...     DRAWEE_BANK_ID=D860BF7A:A58172FE-1187-4004-A857-6776084B872C
    set test variable   &{payment_details}
    When user creates collection with random data
    Then expected return status code 202
    When user processes created collection by id
    Then expected return status code 202
    When user retrieves cheque by distributor
    Then expected return status code 200
    When user processes cheque as cancel
    Then expected return status code 400

9 - Able to POST collection cheque status as Cancel for future dated cheque
    [Documentation]    Able to update collection cheque status as cancel
    [Tags]       distadm    9.2
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'CNPD001' with uom 'EA:5'
    When user creates invoice with fixed data
    Then expected return status code 200
    ${payment_details}=    create dictionary
    ...     OTHER_PYMT_METHOD=Q
    ...     CHEQUE_AMT=${300}
    ...     CHEQUE_DATE=2022-01-12
    ...     DRAWEE_BANK_ID=D860BF7A:A58172FE-1187-4004-A857-6776084B872C
    set test variable   &{payment_details}
    When user creates collection with future data
    Then expected return status code 202
    When user processes created collection by id
    Then expected return status code 202
    When user retrieves cheque by distributor
    Then expected return status code 200
    When user processes cheque as cancel
    Then expected return status code 200

10 - Unable to POST collection cancelled cheque status as clear
    [Documentation]    Unable to process cancelled cheque as clear
    [Tags]    distadm    9.2
    Given user retrieves token access as ${user_role}
    ${cheque_details}=    create dictionary
    ...     ID=7B366DF1:C3B81EFF-E1A4-423E-8E20-6626A76E1FD0
    ...     COLLECTION_ID=5C9697DD:2432B14E-7AD8-4134-8FE2-592B8ABABCD2
    ...     CHEQUE_NO=IGSGVRLDWI
    ...     STATUS=CL
    set test variable   &{cheque_details}
    When user processes cheque as clear
    Then expected return status code 400

11 - Unable to POST collection bounced cheque status as clear
    [Documentation]    Unable to process bounced cheque as clear
    [Tags]    distadm    9.2
    Given user retrieves token access as ${user_role}
    ${cheque_details}=    create dictionary
    ...     ID=7B366DF1:6A42EFD7-5BF5-4084-9B63-F95881B5FC4A
    ...     COLLECTION_ID=5C9697DD:D22F0DF3-0A6C-431A-BB69-DCEBB23510F2
    ...     CHEQUE_NO=CK500
    ...     STATUS=CL
    set test variable   &{cheque_details}
    When user processes cheque as clear
    Then expected return status code 400

12 - Unable to POST collection cheque status using hqadm
    [Documentation]    Unable to update collection cheque status using hqadm
    [Tags]     hqadm    9.2
    Given user retrieves token access as hqadm
    ${cheque_details}=    create dictionary
    ...     ID=7B366DF1:06C74544-E773-44A8-9984-990C35312912
    ...     COLLECTION_ID=5C9697DD:8A0B3C08-9ACB-4302-91F9-64EDA408C8DB
    ...     CHEQUE_NO=JZDNFIJDLJ
    ...     STATUS=CL
    set test variable   &{cheque_details}
    When user processes cheque as clear
    Then expected return status code 403