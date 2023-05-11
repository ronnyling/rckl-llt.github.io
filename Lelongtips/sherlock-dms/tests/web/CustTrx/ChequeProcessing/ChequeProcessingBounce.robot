*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/ChequeProcessing/ChequeProcessingListPage.py

*** Test Cases ***

1 - Able to process cheque status as bounce
    [Documentation]    Able to update collection cheque status as bounce
    [Tags]    distadm    9.2
    ${cheque_details}=    create dictionary
    ...    collection_no=CO0000002020
    ...    cheque_no=TGDQPYJMKV
    set test variable     &{cheque_details}
    Given user navigates to menu Customer Transaction | Cheque Processing
    When user processes valid cheque as bounce
    Then validate cheque is processed successfully to bounce

2 - Unable to process cheque status as bounce
    [Documentation]    Unable to update collection cheque status as bounce for invalid status
    [Tags]    distadm    9.2
    ${cheque_details}=    create dictionary
    ...    collection_no=CO0000001897
    ...    cheque_no=DDOWRDQLUM
    set test variable     &{cheque_details}
    Given user navigates to menu Customer Transaction | Cheque Processing
    When user processes invalid cheque as bounce
    Then validate unable to process as bounce