*** Settings ***
Resource          ${EXECDIR}${/}tests/web/common.robot
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/web/Telesales/Summary/SummaryListPage.py

Test Teardown   run keywords
...    AND user logouts and closes browser

*** Test Cases ***
1 - Able to inline search summary
   [Documentation]    To test that user is able to inline search summary
   [Tags]    telesales   hqtelesales    9.3
   ${summary_details}=    create dictionary
    ...    CUST_NAME=adeT1
    ...    CUST_CD=CT0000001812
    set test variable     &{summary_details}
    Given user navigates to menu Telesales | Summary
    When user searches summary in listing
    Then record display in listing successfully

2 - Able to filter summary
   [Documentation]    To test that user is able to filter summary
   [Tags]    telesales    hqtelesales    9.3
   ${summary_details}=    create dictionary
    ...    CUST_NAME=adeT1
    ...    CUST_CD=CT0000001812
    set test variable     &{summary_details}
    Given user navigates to menu Telesales | Summary
    When user filters summary in listing
    Then record display in listing successfully

3- Validate summary columns displayed correctly
   [Documentation]    To validate the column display of summary listing
   [Tags]    telesales    hqtelesales    9.3
    Given user navigates to menu Telesales | Summary
    Then validate the column display for summary