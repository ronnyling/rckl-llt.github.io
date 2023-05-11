*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/ChequeProcessing/ChequeProcessingListPage.py

*** Test Cases ***
1 - Able to load cheque based on collection date
    [Documentation]    To retrieve list of cheques based on collection date
    [Tags]     distadm    9.2
    Given user navigates to menu Customer Transaction | Cheque Processing
    When user enters cheque selection based on collection date
    Then record display in listing successfully

2 - Able to load cheque based on cheque date
    [Documentation]    To retrieve list of cheques based on cheque date
    [Tags]     distadm    9.2
    Given user navigates to menu Customer Transaction | Cheque Processing
    When user enters cheque selection based on cheque date
    Then record display in listing successfully

3 - Able to load cheque based on status
    [Documentation]    To retrieve list of cheques based on status
    [Tags]     distadm    9.2
    Given user navigates to menu Customer Transaction | Cheque Processing
    When user enters cheque selection based on status
    Then record display in listing successfully

4 - Able to load cheque based on route
    [Documentation]    To retrieve list of cheques based on route
    [Tags]     distadm    9.2
    ${cheque_details}=    create dictionary
    ...    route=route choon
    ...    status=All
    set test variable     &{cheque_details}
    Given user navigates to menu Customer Transaction | Cheque Processing
    When user enters cheque selection based on route
    Then record display in listing successfully