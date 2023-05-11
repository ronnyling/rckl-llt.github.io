*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/RouteMgmt/Route/RouteListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/RouteMgmt/Route/RouteAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/RouteMgmt/Route/RouteEditPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RoutePost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteDelete.py
Library         ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py
Library         ${EXECDIR}${/}resources/restAPI/Config/AppSetup/FieldForcePut.py
Library         ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py

Test Setup    run keywords
...    user open browser and logins using user role ${user_role}
Test Teardown   run keywords
...    user selects route to delete
...    route deleted successfully with message 'Record deleted'
...    user logouts and closes browser

*** Test Cases ***
1 - Able to Update Telesales Route
    [Documentation]    Able to Update Telesales Route
    [Tags]     distadm    9.3    NRSZUANQ-56304
    [Setup]     run keywords
    ...    user sets the feature setup for telesales to ON passing with 'telesales' value
    ...    user retrieves token access as hqadm
    ...    user retrieves details of application setup
    ...    user updates app setup to TELE_SALES_CONTROL_BY : DIST
    ...    user open browser and logins using user role ${user_role}
    ${RouteDetails}=    create dictionary
    ...    OP_TYPE=Telesales
    Given user switches Off multi principal
    And user navigates to menu Master Data Management | Route Management | Route
    When user creates route using fixed data
    And user assigns geo value using random data
    Then route created successfully with message 'Record created'
    When user selects route to edit
    And user updates route with random data
    Then route updated successfully with message 'Record updated'

2 - Able to Update HQ Telesales Route
    [Documentation]    Able to Update HQ Telesales Route
    [Tags]     hqadm    9.3    NRSZUANQ-56482
        [Setup]     run keywords
    ...    user sets the feature setup for telesales to ON passing with 'telesales' value
    ...    user retrieves token access as hqadm
    ...    user retrieves details of application setup
    ...    user updates app setup to TELE_SALES_CONTROL_BY : HQ
    ...    user open browser and logins using user role ${user_role}
    ${RouteDetails}=    create dictionary
    ...    OP_TYPE=HQ Telesales
    Given user switches Off multi principal
    And user navigates to menu Master Data Management | Route Management | Route
    When user creates route using fixed data
    And user assigns geo value using random data
    Then route created successfully with message 'Record created'
    When user selects route to edit
    And user updates route with random data
    Then route updated successfully with message 'Record updated'