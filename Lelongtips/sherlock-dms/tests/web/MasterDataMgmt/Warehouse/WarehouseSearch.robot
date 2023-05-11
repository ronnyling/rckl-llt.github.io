*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Warehouse/WarehouseListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Warehouse/WarehouseAddPage.py

Test Teardown  run keywords
...    user selects warehouse to delete
...    AND     warehouse deleted successfully with message 'Record deleted'
...    AND     user logouts and closes browser

*** Test Cases ***
1 - Able to Create Warehouse using given data
    [Documentation]    Able to create warehouse using given data
    [Tags]     distadm  9.0   9.1   NRSZUANQ-28195
    Given user navigates to menu Master Data Management | Warehouse
    When user creates unmanaged warehouse with random data
    Then warehouse created successfully with message 'Record created'
    When user searches warehouse using created data
    Then record display in listing successfully
