*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Customer/CustomerListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Customer/CustomerOptionsPage.py
Library         Collections

Test Teardown   run keywords
...    user logouts and closes browser

*** Test Cases ***
1 - Able to update customer option with random data
    [Documentation]    Able to update customer option with random data
    [Tags]     distadm
    ${CUSTOMER}=    create dictionary
    ...     CD=CT0000004807
    Given user navigates to menu Master Data Management | Customer
    And user searches customer with code
    And user go to Options tab
    When user updates customer options with random data
    Then customer options updated successfully with message 'Record updated successfully'

2 - Able to update customer option with fixed data
    [Documentation]    Able to update customer option with fixed data
    [Tags]     distadm
    ${CUSTOMER}=    create dictionary
    ...     CD=CT0000004807
    ${CUSTOMER_OPTIONS}=    create dictionary
    ...     BackOrder=Yes
    ...     CreditCheck=No
    ...     PartialFulfilment=Yes
    ...     Mandatory=No
    ...     OverDue=Yes
    Given user navigates to menu Master Data Management | Customer
    And user searches customer with code
    And user go to Options tab
    When user updates customer options with fixed data
    Then customer options updated successfully with message 'Record updated successfully'