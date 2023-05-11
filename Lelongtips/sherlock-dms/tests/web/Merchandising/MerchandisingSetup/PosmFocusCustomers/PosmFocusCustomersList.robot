*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/PosmFocusCustomers/PosmFocusCustomersListPage.py

*** Test Cases ***
1 - User validates hq admin able to view add and delete buttons
    [Documentation]  To validate hq admin able to view add and delete button
    [Tags]    hqadm    9.2
    Given user navigates to menu Merchandising | Merchandising Setup | POSM Focus Customers
    When user navigates to ChannelB19 tab
    And user validates buttons for hq admin

2 - User validates distributor admin unable to view add and delete buttons
    [Documentation]  To validate distributor admin unable to view add and delete button
    [Tags]    distadm    9.2
    Given user navigates to menu Merchandising | Merchandising Setup | POSM Focus Customers
    When user navigates to ChannelB19 tab
    And user validates buttons for distributor admin