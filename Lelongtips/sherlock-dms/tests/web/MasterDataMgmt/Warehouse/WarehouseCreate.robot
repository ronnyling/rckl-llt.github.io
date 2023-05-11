*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Warehouse/WarehouseListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Warehouse/WarehouseAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Van/VanPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Van/VanDelete.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py

*** Test Cases ***
1 - Able to Create Warehouse using given data
    [Documentation]    Able to create warehouse using given data
    [Tags]     distadm  9.0
    [Teardown]  run keywords
    ...    user selects warehouse to delete
    ...    AND     warehouse deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    ${WarehouseDetails}=    create dictionary
    ...    WH_Code=WHA001
    ...    WH_Desc=WHAuto 123
    set test variable     &{WarehouseDetails}
    Given user navigates to menu Master Data Management | Warehouse
    When user creates Unmanaged warehouse with fixed data
    Then warehouse created successfully with message 'Record created'

2 - Able to Create Managed Warehouse
    [Documentation]    Able to create managed warehouse
    [Tags]     distadm  9.0
    [Teardown]  run keywords
    ...    user selects warehouse to delete
    ...    AND     warehouse deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Master Data Management | Warehouse
    When user creates Managed warehouse with random data
    Then warehouse created successfully with message 'Record created'

3 - Able to Create Semi-Managed Warehouse
    [Documentation]    Able to create semi-managed warehouse
    [Tags]     distadm  9.0
    [Teardown]  run keywords
    ...    user selects warehouse to delete
    ...    AND     warehouse deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Master Data Management | Warehouse
    When user creates Semi-managed warehouse with random data
    Then warehouse created successfully with message 'Record created'

4 - Able to Create Unmanaged Warehouse
    [Documentation]    Able to create semi-managed warehouse
    [Tags]     distadm  9.0
    [Teardown]  run keywords
    ...    user selects warehouse to delete
    ...    AND     warehouse deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Master Data Management | Warehouse
    When user creates Unmanaged warehouse with random data
    Then warehouse created successfully with message 'Record created'

5 - Able to Create Van Warehouse
    [Documentation]    Able to create van warehouse
    [Tags]     distadm  9.0
    [Setup]     run keywords
    ...    user open browser and logins using user role ${user_role}
    ...    AND    user retrieves token access as hqadm
    ...    AND    user gets distributor by using code 'DistEgg'
    ...    AND    user retrieves token access as ${user_role}
    ...    AND    user creates van with random data
    ...    AND    expected return status code 201
    [Teardown]  run keywords
    ...    user selects warehouse to delete
    ...    AND     warehouse deleted successfully with message 'Record deleted'
    ...    AND     user deletes van with created data
    ...    AND     expected return status code 200
    ...    AND     user logouts and closes browser
    Given user navigates to menu Master Data Management | Warehouse
    When user creates Van warehouse with random data
    Then warehouse created successfully with message 'Record created'

6 - Able to Create Damage Warehouse
    [Documentation]    Able to create damaged warehouse
    [Tags]     distadm  9.0
    [Teardown]  run keywords
    ...    user selects warehouse to delete
    ...    AND     warehouse deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Master Data Management | Warehouse
    When user creates Damaged warehouse with random data
    Then warehouse created successfully with message 'Record created'

7 - Able to Create Prime Warehouse
    [Documentation]    Able to create prime warehouse
    [Tags]     distadm    9.1    NRSZUANQ-28193   NRSZUANQ-28197
    [Teardown]  run keywords
    ...    user selects warehouse to delete
    ...    AND     warehouse deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user switches On multi principal
    And user navigates to menu Master Data Management | Warehouse
    When user creates Prime warehouse with random data
    Then warehouse created successfully with message 'Record created'

8 - Able to Create Non-Prime Warehouse
    [Documentation]    Able to create non prime warehouse
    [Tags]     distadm    9.1    NRSZUANQ-28191   NRSZUANQ-28198
    [Teardown]  run keywords
    ...    user selects warehouse to delete
    ...    AND     warehouse deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user switches On multi principal
    And user navigates to menu Master Data Management | Warehouse
    When user creates Non-Prime warehouse with random data
    Then warehouse created successfully with message 'Record created'

9 - Unable to edit principal flag in Warehouse in edit screen
    [Documentation]    Unable to edit principal field in edit screen
    [Tags]     distadm    9.1    NRSZUANQ-28203
    [Teardown]  run keywords
    ...    user selects warehouse to delete
    ...    AND     warehouse deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user switches On multi principal
    And user navigates to menu Master Data Management | Warehouse
    When user creates Prime warehouse with random data
    Then warehouse created successfully with message 'Record created'
    When user selects warehouse to edit
    Then user validates Principal field is disabled
    And user cancels warehouse details screen

10 - Unable to view principal flag in Warehouse when Multi Principal = No in Distributor Configuration
    [Documentation]    Unable to view principal field when multi principal = No
    [Tags]     distadm    9.1    NRSZUANQ-28219
    Given user switches Off multi principal
    And user navigates to menu Master Data Management | Warehouse
    When user validates Principal field is not visible
    And user cancels warehouse details screen
    Then user switches On multi principal

11 - Verify "Is Warehouse Blocked" is not visible in Warehouse
    [Documentation]    Unable to view "Is Warehouse Blocked" in warehouse screen
    [Tags]     distadm    9.1    NRSZUANQ-28200
    Given user navigates to menu Master Data Management | Warehouse
    When user validates Is Warehouse Blocked field is not visible
    Then user cancels warehouse details screen
