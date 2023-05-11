*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/ExecutionResult/AuditResult/AuditResultListPage.py

*** Test Cases ***
1 - Able to search for Facing Audit result
    [Documentation]  To validate user able to search and view facing audit result
    [Tags]    hqadm    9.2
    ${audit_details}=    create dictionary
    ...    TRANSACTION_NO=FAE2EPreSale0000000010
    ...    CUSTOMER_NAME=AB Grocer
    set test variable     &{audit_details}
    Given user navigates to menu Merchandising | Execution Result | Audit Result
    When user searches facing audit result
    When user selects result to view
    Then user is able to view the result successfully

2 - Able to filter for Facing Audit result
    [Documentation]  To validate user able to filter and view facing audit result
    [Tags]    hqadm    9.2
    ${audit_details}=    create dictionary
    ...    TRANSACTION_NO=FAE2EPreSale0000000010
    ...    CUSTOMER_NAME=AB Grocer
    set test variable     &{audit_details}
    Given user navigates to menu Merchandising | Execution Result | Audit Result
    When user filters facing audit result
    And user selects facing audit result to view
    Then user is able to view the result successfully

3 - Able to search for Price Audit result
    [Documentation]  To validate user able to search and view price audit result
    [Tags]    hqadm    9.2
    ${audit_details}=    create dictionary
    ...    TRANSACTION_NO=PANikeMerch0000000003
    ...    CUSTOMER_NAME=custcannot
    set test variable     &{audit_details}
    Given user navigates to menu Merchandising | Execution Result | Audit Result
    And user selects Price Audit tab
    When user searches price audit result
    And user selects result to view
    Then user is able to view the result successfully

4 - Able to filter for Price Audit result
    [Documentation]  To validate user able to filter and view price audit result
    [Tags]    hqadm    9.2
    ${audit_details}=    create dictionary
    ...    TRANSACTION_NO=PANikeMerch0000000003
    ...    CUSTOMER_NAME=custcannot
    set test variable     &{audit_details}
    Given user navigates to menu Merchandising | Execution Result | Audit Result
    And user selects Price Audit tab
    When user filters price audit result
    And user selects result to view
    Then user is able to view the result successfully

5 - Able to search for Distribution Check result
    [Documentation]  To validate user able to search and view distribution check result
    [Tags]    hqadm    9.2
    ${audit_details}=    create dictionary
    ...    TRANSACTION_NO=DCNikeMerch0000000004
    ...    CUSTOMER_NAME=custcannot
    set test variable     &{audit_details}
    Given user navigates to menu Merchandising | Execution Result | Audit Result
    And user selects Distribution Check tab
    When user searches distribution check result
    And user selects result to view
    Then user is able to view the result successfully

6 - Able to filter for Distribution Check result
    [Documentation]  To validate user able to filter and view distribution check result
    [Tags]    hqadm    9.2
    ${audit_details}=    create dictionary
    ...    TRANSACTION_NO=DCNikeMerch0000000004
    ...    CUSTOMER_NAME=custcannot
    set test variable     &{audit_details}
    Given user navigates to menu Merchandising | Execution Result | Audit Result
    And user selects Distribution Check tab
    And user filters distribution check result
    When user selects result to view
    Then user is able to view the result successfully

7 - Able to search for Promo Compliance result
    [Documentation]  To validate user able to search and view promo compliance result
    [Tags]    hqadm    9.2
    ${audit_details}=    create dictionary
    ...    TRANSACTION_NO=PRCNikeMerch0000000003
    ...    CUSTOMER_NAME=custcannot
    set test variable     &{audit_details}
    Given user navigates to menu Merchandising | Execution Result | Audit Result
    And user selects Promotion Compliance tab
    When user searches promo compliance result
    And user selects result to view
    Then user is able to view the result successfully

8 - Able to filter for Promo Compliance result
    [Documentation]  To validate user able to filter and view promo compliance result
    [Tags]    hqadm    9.2
    ${audit_details}=    create dictionary
    ...    TRANSACTION_NO=PRCNikeMerch0000000003
    ...    CUSTOMER_NAME=custcannot
    set test variable     &{audit_details}
    Given user navigates to menu Merchandising | Execution Result | Audit Result
    And user selects Promotion Compliance tab
    When user filters promo compliance result
    And user selects result to view
    Then user is able to view the result successfully

9 - Able to view for Planogram result
    [Documentation]  To validate user able to view planogram result
    [Tags]    hqadm    9.2
    Given user navigates to menu Merchandising | Execution Result | Audit Result
    When user selects Planogram tab
    Then user is able to view the compliance successfully