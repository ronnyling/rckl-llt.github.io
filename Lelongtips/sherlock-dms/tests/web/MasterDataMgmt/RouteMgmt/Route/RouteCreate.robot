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
...    AND user selects route to delete
...    AND route deleted successfully with message 'Record deleted'
...    AND user logouts and closes browser

*** Test Cases ***
1 - Able to Create Route with random data
    [Documentation]    Able to create Route with random data
    [Tags]     distadm    9.0
    Given user navigates to menu Master Data Management | Route Management | Route
    When user creates route using random data
    And user assigns geo value using random data
    Then route created successfully with message 'Record created'

2 - Able to Create Route with fixed data
    [Documentation]    Able to create Route with given data
    [Tags]     distadm    9.0
    ${RouteDetails}=    create dictionary
    ...    routeCode=Auto001
    ...    routeName=RN 123 Test
    set test variable     &{RouteDetails}
    Given user navigates to menu Master Data Management | Route Management | Route
    When user creates route using fixed data
    And user assigns geo value using random data
    Then route created successfully with message 'Record created'

3 - Able to Create Route with non prime warehouse
    [Documentation]    Able to create Route with non prime warehouse chosen
    [Tags]     distadm    9.1    NRSZUANQ-28279
    Given user switches On multi principal
    And user navigates to menu Master Data Management | Route Management | Route
    When user creates route using random data
    And user assigns geo value using random data
    Then route created successfully with message 'Record created'

4 - Unable to view Non Prime warehouse in Route when Multi Principal = No in Distributor Configuration
    [Documentation]    Unable to view non prime warehouse in route when multi principal = off
    [Tags]     distadm    9.1    NRSZUANQ-28383
    Given user switches Off multi principal
    And user navigates to menu Master Data Management | Route Management | Route
    When user creates route using random data
    And user assigns geo value using random data
    Then route created successfully with message 'Record created'
    And user switches On multi principal

5 - Able to create Telesales route using distributor access
    [Documentation]    Able to create Telesales route using distributor access
    [Tags]     distadm    9.3   NRSZUANQ-56303
    [Setup]     run keywords
    ...    user sets the feature setup for telesales to ON passing with 'telesales' value
    ...    user retrieves token access as hqadm
    ...    user retrieves details of application setup
    ...    user updates app setup to TELE_SALES_CONTROL_BY : DIST
    ...    user open browser and logins using user role ${user_role}
    ${RouteDetails}=    create dictionary
    ...    OP_TYPE=Telesales
    set test variable     &{RouteDetails}
    Given user switches Off multi principal
    Given user navigates to menu Master Data Management | Route Management | Route
    When user creates route using fixed data
    And user assigns geo value using random data
    Then route created successfully with message 'Record created'

6 - Able to create HQ Telesales route using HQ access
    [Documentation]    Able to create HQ Telesales route using HQ access
    [Tags]     hqadm    9.3     NRSZUANQ-56481
    [Setup]     run keywords
    ...    user sets the feature setup for telesales to ON passing with 'telesales' value
    ...    user retrieves token access as hqadm
    ...    user retrieves details of application setup
    ...    user updates app setup to TELE_SALES_CONTROL_BY : HQ
    ...    user open browser and logins using user role ${user_role}
    ${RouteDetails}=    create dictionary
    ...    OP_TYPE=HQ Telesales
    set test variable     &{RouteDetails}
    Given user switches Off multi principal
    Given user navigates to menu Master Data Management | Route Management | Route
    When user creates route using fixed data
    And user assigns geo value using random data
    Then route created successfully with message 'Record created'


