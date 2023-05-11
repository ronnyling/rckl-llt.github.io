*** Settings ***
Resource          ${EXECDIR}${/}tests/web/common.robot
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerShipToPost.py
Library           ${EXECDIR}${/}resources/web/MasterDataMgmt/Customer/CustomerApproval.py
Library           ${EXECDIR}${/}resources/web/MasterDataMgmt/Customer/CustomerListPage.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py

Library           Collections

Test Teardown   run keywords
...    set customer teardown
...    user logouts and closes browser

*** Test Cases ***
1 - Able to approve created customer
    [Documentation]    Able to approve created customer
    [Tags]    hqadm
    [Setup]  run keywords
    ...   user creates customer as prerequisite
    ...   user open browser and logins using user role hqadm
    Given user navigates to menu Master Data Management | Customer
    And user retrieve customer code
    ${CUSTOMER}=    create dictionary
    ...     CD=${CUSTOMER_CD}
    set test variable  &{CUSTOMER}
    And user searches customer with code
    When user Approve created customer
    Then customer updated successfully with message 'Record updated successfully'

2 - Able to reject created customer
    [Documentation]    Able to reject created customer
    [Tags]    hqadm
    [Setup]  run keywords
    ...   user creates customer as prerequisite
    ...   user open browser and logins using user role hqadm
    Given user navigates to menu Master Data Management | Customer
    And user retrieve customer code
    ${CUSTOMER}=    create dictionary
    ...     CD=${CUSTOMER_CD}
    set test variable  &{CUSTOMER}
    And user searches customer with code
    When user Reject created customer
    Then customer updated successfully with message 'Record updated successfully'
