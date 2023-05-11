*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Warehouse/WarehouseListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Warehouse/WarehouseAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

*** Test Cases ***
1 - Able to Filter Warehouse using given data
    [Documentation]    Able to filter warehouse using given data
    [Tags]     distadm  9.0
    [Teardown]  run keywords
    ...    user selects warehouse to delete
    ...    AND     warehouse deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Master Data Management | Warehouse
    When user creates unmanaged warehouse with random data
    Then warehouse created successfully with message 'Record created'
    When user filters warehouse using created data
    Then record display in listing successfully

2 - Able to filter Warehouse using principal field
    [Documentation]    Able to filter warehouse using principal field
    [Tags]     distadm    9.1    NRSZUANQ-28194
    [Setup]     run keywords
    ...    user open browser and logins using user role ${user_role}
    ...    AND    user switches On multi principal
    [Teardown]  run keywords
    ...    user selects warehouse to delete
    ...    AND     warehouse deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Master Data Management | Warehouse
    When user creates Non-Prime warehouse with random data
    Then warehouse created successfully with message 'Record created'
    When user filters warehouse using Non-Prime data
    Then record display in listing successfully

3 - Unable to view Non Prime Warehouse using HQ access
    [Documentation]    Unable to view principal column when access using other than distributor access
    [Tags]     hqadm     hquser   sysimp    9.1    NRSZUANQ-28201
    Given user navigates to menu Master Data Management | Warehouse
    When user validates principal column not visible in listing