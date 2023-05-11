*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/ChequeProcessing/ChequeProcessingListPage.py

*** Test Cases ***

1 - Able to process cheque status as cancel
    [Documentation]    Able to update collection cheque status as cancel
    [Tags]    distadm    9.2
    ${cheque_details}=    create dictionary
    ...    collection_no=CO0000002086
    ...    cheque_no=QXXKCPHJUE
    set test variable     &{cheque_details}
    Given user navigates to menu Customer Transaction | Cheque Processing
    When user processes valid cheque as cancel
    Then validate cheque is processed successfully to cancel

2 - Unable to process cheque status as bounce
    [Documentation]    Unable to update collection cheque status as cancel for invalid status
    [Tags]    distadm    9.2
    ${cheque_details}=    create dictionary
    ...    collection_no=CO0000002035
    ...    cheque_no=CPTYKHWUAG
    set test variable     &{cheque_details}
    Given user navigates to menu Customer Transaction | Cheque Processing
    When user processes invalid cheque as cancel
    Then validate unable to process as cancel