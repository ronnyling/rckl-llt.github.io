*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Customer/CustomerListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Customer/CustomerShipToPage.py
Library         Collections

Test Teardown   run keywords
...    user logouts and closes browser

*** Test Cases ***
1 - Able to delete ship to address
    [Documentation]    Able to delete ship to address
    [Tags]     distadm
    ${CUSTOMER}=    create dictionary
    ...     CD=CT0000004653
    Given user navigates to menu Master Data Management | Customer
    And user searches customer with code
    And user go to Ship To Address tab
    And user creates a new ship to address
    When user selects ship to address to delete
    Then ship to address created successfully with message 'Record deleted'