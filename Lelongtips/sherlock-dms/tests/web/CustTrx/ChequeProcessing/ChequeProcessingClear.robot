*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/ChequeProcessing/ChequeProcessingListPage.py

*** Test Cases ***

1 - Able to process cheque status as clear
    [Documentation]    Able to update collection cheque status as clear
    [Tags]    distadm    9.2
    ${cheque_details}=    create dictionary
    ...    collection_no=CO0000001952
    ...    cheque_no=UUIXEOXMUT
    set test variable     &{cheque_details}
    Given user navigates to menu Customer Transaction | Cheque Processing
    When user processes valid cheque as clear
    And user clicks on Save button
    Then validate cheque is processed successfully to clear

2 - Unable to process cheque status as clear
    [Documentation]    Unable to update collection cheque status as clear for invalid status
    [Tags]    distadm    9.2
    ${cheque_details}=    create dictionary
    ...    collection_no=CO0000002049
    ...    cheque_no=IGSGVRLDWI
    set test variable     &{cheque_details}
    Given user navigates to menu Customer Transaction | Cheque Processing
    When user processes invalid cheque as clear
    Then validate unable to process as clear