*** Settings ***
Resource        ${EXECDIR}/tests/hht/common.robot
Resource        ${EXECDIR}${/}tests/hht/common.robot
Library         ${EXECDIR}${/}resources/hht/CustomerInfo/POSMInventory/POSMInventoryRead.py
Library         ${EXECDIR}${/}resources/hht/MyStores/TodayVisit/TodayVisitRead.py
Library         ${EXECDIR}${/}resources/hht_api/POSMInstallation/POSMInstallationPost.py

Test Setup    user creates prerequisite for Customer Inventory

*** Test Cases ***
1-Able to view customer POSM details
    [Documentation]    To test that user is able to view POSM details of customer
    [Tags]    salesperson     9.1    TODO
    Given user navigates to Task Bar | My Stores
    When choose randomly from MyStore listing
    And user navigates to customer details
    And user selects customer posm tab
    And user selects a customer posm: random
    Then user verify posm details
