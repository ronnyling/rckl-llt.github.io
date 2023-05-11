*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/RouteActivity/RouteActivityListPage.py

*** Test Cases ***
1 - Validate buttons for HQ admin
    [Documentation]  To validate user able to view add and delete buttons
    [Tags]    hqadm    9.2
    Given user navigates to menu Merchandising | Merchandising Setup | Route Activity
    Then user validates buttons for hq admin

2 - Validate buttons for distributor login
    [Documentation]  To validate user unable to see add and delete buttons
    [Tags]    distadm    9.2
    Given user navigates to menu Merchandising | Merchandising Setup | Route Activity
    Then user validates buttons for distributor
