*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Customer/CustomerListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Customer/CustomerOptionsPage.py
Library         Collections

Test Teardown   run keywords
...    user logouts and closes browser

*** Test Cases ***
1 - Able to view customer option
    [Documentation]    Able to view customer option
    [Tags]     distadm
    ${CUSTOMER}=    create dictionary
    ...     CD=CT0000004807
    Given user navigates to menu Master Data Management | Customer
    And user searches customer with code
    When user go to Options tab
    Then user validates options page info