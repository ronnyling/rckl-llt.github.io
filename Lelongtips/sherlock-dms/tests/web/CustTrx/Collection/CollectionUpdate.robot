*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/Collection/CollectionListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/Collection/CollectionAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/CustTrx/Collection/CollectionPost.py
Library         ${EXECDIR}${/}resources/restAPI/CustTrx/SalesInvoice/SalesInvoicePost.py


*** Test Cases ***
1 - Able to update Collection with random data
    [Documentation]    To update Collection with random data
    [Tags]     distadm    9.2
    Given user navigates to menu Customer Transaction | Collection
    When user selects collection to update
    And user updates collection with random data
    Then collection created successfully with message 'Record updated successfully'

2 - Able to update Collection with fixed data
    [Documentation]    To update Collection with fixed data
    [Tags]     distadm    9.2
    ${ColDetails}=    create dictionary
    ...    collectionNo=CO0000000895
    ...    cashAmount=${4}
    ...    paymentMode=Cheque
    ...    paymentAmount=${10}
    ...    referenceNo=bran
    ...    date=today
    ...    bank=MAYBANK1
    set test variable     &{ColDetails}
    Given user navigates to menu Customer Transaction | Collection
    When user selects collection to update
    And user updates collection with fixed data
    Then collection created successfully with message 'Record updated successfully'

3 - Able to add newly generated invoice in edit mode
    [Documentation]    To add newly generated invoice in created Collection
    [Tags]     distadm    9.2    NRSZUANQ-44084
    ${ColDetails}=    create dictionary
    ...    collectionNo=CO0000000895
    ...    cashAmount=${4}
    set test variable     &{ColDetails}
    Given user navigates to menu Customer Transaction | Collection
    When user selects collection to update
    Then user validates new generated invoice added

4 - Able to add newly generated debit note in edit mode
    [Documentation]    To add newly generated debit note in created Collection
    [Tags]     distadm    9.2    NRSZUANQ-44084
    ${ColDetails}=    create dictionary
    ...    collectionNo=CO0000000895
    ...    cashAmount=${4}
    set test variable     &{ColDetails}
    Given user navigates to menu Customer Transaction | Collection
    When user selects collection to update
    Then user validates new generated debit note added

5 - Validates open item displayed following FIFO logic
    [Documentation]    Validates open item displayed following FIFO logic
    [Tags]     distadm    9.2    NRSZUANQ-44084
    ${ColDetails}=    create dictionary
    ...    collectionNo=CO0000000895
    ...    cashAmount=${4}
    set test variable     &{ColDetails}
    Given user navigates to menu Customer Transaction | Collection
    When user selects collection to update
    Then user validates open item list

6 - Able to select/deselect Adjustment in Edit mode
    [Documentation]    Able to select/deselect Adjustment in Edit mode
    [Tags]     distadm    9.2    NRSZUANQ-44085
    ${ColDetails}=    create dictionary
    ...    collectionNo=CO0000000895
    ...    cashAmount=${4}
    set test variable     &{ColDetails}
    Given user navigates to menu Customer Transaction | Collection
    When user selects collection to update
    Then user validates adjustment in edit mode

7 - Able to reallocate amount to next invoice
    [Documentation]    Able to reallocate amount to next invoice
    [Tags]     distadm    9.2    NRSZUANQ-44085
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    ${collection_details}=    create dictionary
    ...     CASH_AMT=${3}
    ...     OTHER_PYMTS=[]
    ...     ADJUSTMENT=${True}
    set test variable   &{collection_details}
    ${ColDetails}=    create dictionary
    ...    route=route choon
    ...    customer=Customer B02
    ...    amount=${10}
    set test variable     &{ColDetails}
    Given user retrieves token access as distadm
    And user intends to insert product 'CNPD001' with uom 'EA:5'
    And user creates invoice with fixed data
    And user creates collection with fixed data
    When user navigates to menu Customer Transaction | Collection
    And user selects collection to update
    Then user validates update amount reallocate

