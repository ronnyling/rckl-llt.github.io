*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/RouteActivity/RouteActivityListPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/RouteActivity/RouteActivityAddPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/RouteActivity/RouteActivityUpdatePage.py

*** Test Cases ***
1 - User able to delete route activity
    [Documentation]  To validate user able to delete route activity
    [Tags]    hqadm   9.2
    Given user navigates to menu Merchandising | Merchandising Setup | Route Activity
    When user creates route activity using random data
    Then route activity created successfully with message 'Record added'
    When user selects route activity to delete
    Then route activity deleted successfully with message 'Record deleted'