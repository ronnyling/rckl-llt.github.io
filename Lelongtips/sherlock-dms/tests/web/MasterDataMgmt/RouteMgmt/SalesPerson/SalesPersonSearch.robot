*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonListPage.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonPost.py
Library         ${EXEC_DIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonDelete.py
Test Setup  run keywords
...    user creates salesperson as prerequisite
...    AND    user open browser and logins using user role ${user_role}

Test Teardown  run keywords
...     user deletes created salesperson as teardown
...     AND    user logouts and closes browser

*** Test Cases ***
1 - Able to Search Salesperson using salesperson cd
    [Documentation]    Able to filter Salesperson using salesperson_cd
    [Tags]     distadm    9.0
    Given user navigates to menu Master Data Management | Route Management | Salesperson
    When user searches created salesperson in listing page
    Then record display in listing successfully
