*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/ExecutionResult/ChecklistResult/ChecklistResultListPage.py

*** Test Cases ***
1 - Able to search for checklist result by transaction number
    [Documentation]  To validate user able to search result by transaction number
    [Tags]    hqadm    9.2
    ${checklist_details}=    create dictionary
    ...    search_item=008
    ...    txn_no=CLMP0010000000008
    set test variable     &{checklist_details}
    Given user navigates to menu Merchandising | Execution Result | Checklist Result
    When user searches checklist result by Transaction No.
    And user selects checklist result to view
    Then user is able to view the result successfully

2 - Able to search for checklist result by distributor
    [Documentation]  To validate user able to search result by distributor
    [Tags]    hqadm    9.2
    ${checklist_details}=    create dictionary
    ...    search_item=Dist Titan
    ...    txn_no=CLMP0010
    set test variable     &{checklist_details}
    Given user navigates to menu Merchandising | Execution Result | Checklist Result
    When user searches checklist result by Distributor
    And user selects checklist result to view
    Then user is able to view the result successfully

3 - Able to search for checklist result by customer
    [Documentation]  To validate user able to search result by customer
    [Tags]    hqadm    9.2
    ${checklist_details}=    create dictionary
    ...    search_item=7eleven
    ...    txn_no=CLMP0010
    set test variable     &{checklist_details}
    Given user navigates to menu Merchandising | Execution Result | Checklist Result
    When user searches checklist result by Customer Name
    And user selects checklist result to view
    Then user is able to view the result successfully

4 - Able to search for checklist result by route
    [Documentation]  To validate user able to search result by route
    [Tags]    hqadm    9.2
    ${checklist_details}=    create dictionary
    ...    search_item=MP Route
    ...    txn_no=CLMP0010000000007
    set test variable     &{checklist_details}
    Given user navigates to menu Merchandising | Execution Result | Checklist Result
    When user searches checklist result by Route Name
    And user selects checklist result to view
    Then user is able to view the result successfully

5 - Able to filter for checklist result by transaction number
    [Documentation]  To validate user able to filter result by transaction number
    [Tags]    hqadm    9.2
    ${checklist_details}=    create dictionary
    ...    filter_item=008
    ...    txn_no=CLMP0010000000008
    set test variable     &{checklist_details}
    Given user navigates to menu Merchandising | Execution Result | Checklist Result
    When user filters checklist result by Transaction No.
    And user selects checklist result to view
    Then user is able to view the result successfully

6 - Able to filter for checklist result by distributor
    [Documentation]  To validate user able to filter result by distributor
    [Tags]    hqadm    9.2
    ${checklist_details}=    create dictionary
    ...    filter_item=Dist Titan
    ...    txn_no=CLMP0010
    set test variable     &{checklist_details}
    Given user navigates to menu Merchandising | Execution Result | Checklist Result
    When user filters checklist result by Distributor
    And user selects checklist result to view
    Then user is able to view the result successfully

7 - Able to filter for checklist result by customer
    [Documentation]  To validate user able to filter result by customer
    [Tags]    hqadm    9.2
    ${checklist_details}=    create dictionary
    ...    filter_item=7eleven
    ...    txn_no=CLMP0010
    set test variable     &{checklist_details}
    Given user navigates to menu Merchandising | Execution Result | Checklist Result
    When user filters checklist result by Customer Name
    And user selects checklist result to view
    Then user is able to view the result successfully

8 - Able to filter for checklist result by route
    [Documentation]  To validate user able to filter result by route
    [Tags]    hqadm    9.2
    ${checklist_details}=    create dictionary
    ...    filter_item=MP Route
    ...    txn_no=CLMP0010000000007
    set test variable     &{checklist_details}
    Given user navigates to menu Merchandising | Execution Result | Checklist Result
    When user filters checklist result by Route Name
    And user selects checklist result to view
    Then user is able to view the result successfully

