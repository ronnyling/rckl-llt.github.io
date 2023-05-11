*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Customer/CustomerListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Customer/CustomerShipToPage.py
Library         Collections

Test Teardown   run keywords
...    user selects ship to address to delete
...    user logouts and closes browser

*** Test Cases ***
1 - Able to update ship to address with random data
    [Documentation]    Able to update ship to address with random data
    [Tags]     distadm
    ${CUSTOMER}=    create dictionary
    ...     CD=CT0000004653
    Given user navigates to menu Master Data Management | Customer
    And user searches customer with code
    And user go to Ship To Address tab
    And user creates a new ship to address
    And user selects ship to address to edit
    When user updates ship to address with random data
    Then ship to address updated successfully with message 'Record updated successfully'

2 - Able to create new ship to address with fixed data
    [Documentation]    Able to create new ship to address with fixed data
    [Tags]     distadm
    ${CUSTOMER}=    create dictionary
    ...     CD=CT0000004653
    ${SHIP_TO_UPDATE}=    create dictionary
    ...     Desc=Updated Description
    ...     Address1=Jalan Gemiling 1
    ...     Address2=Taman Desa Utama
    ...     Address3=Selangor
    ...     Postal=61200
    Given user navigates to menu Master Data Management | Customer
    And user searches customer with code
    And user go to Ship To Address tab
    And user creates a new ship to address
    And user selects ship to address to edit
    When user updates ship to address with fixed data
    Then ship to address updated successfully with message 'Record updated successfully'