*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RoutePost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteMapping/RouteGeoMapping.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/FieldForcePut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py

Test Setup      run keywords
...    user creates prerequisite for Route
...    Given user retrieves token access as hqadm
...    user retrieves details of application setup
Test Teardown   user deletes prerequisite for Route

*** Test Cases ***
1 - Able to retrieve all Route
    [Documentation]    To retrieve all route via API
    [Tags]     distadm    9.0
    Given user retrieves token access as ${user_role}
    When user gets all route data
    Then expected return status code 200

2 - Able to retrieve specific route using id
    [Documentation]    To retrieve route using given id via API
    [Tags]     distadm    9.0     NRSZUANQ-28424
    Given user retrieves token access as ${user_role}
    When user creates route with given data
    Then expected return status code 201
    When user maps route to Level=Area, Node=Dungun
    Then expected return status code 200
    When user gets route by using id
    Then expected return status code 200
    When user deletes route with created data
    Then expected return status code 200

3 - Able to retrieve all Route using Hq access
    [Documentation]    To retrieve all route using HQ access via API
    [Tags]     hqadm    9.0    NRSZUANQ-28445
    Given user retrieves token access as hqadm
    When user gets all route data
    Then expected return status code 200

4. - Able to retrieve Telesales route using distributor access
    [Documentation]    To retrieve Telesales route using distributor access via API
    [Tags]     distadm    9.3
    ${AppSetupDetails}=    create dictionary
    ...    TELE_SALES_CONTROL_BY=DIST
    ${route_details}=   create dictionary
    ...   OP_TYPE=T
    set test variable     &{route_details}
    Given User sets the feature setup for telesales to ON passing with 'telesales' value
    When user updates app setup field force details using fixed data
    And user retrieves token access as ${user_role}
    When user creates route with given data
    Then expected return status code 201
    When user maps route to Level=Area, Node=Dungun
    Then expected return status code 200
    When user gets all route data
    Then expected return status code 200
    When user deletes route with created data
    Then expected return status code 200

5. - Able to retrieve HQ Telesales route using HQ access
    [Documentation]    To retrieve HQ Telesales route using HQ access via API
    [Tags]     hqadm    9.3
    ${AppSetupDetails}=    create dictionary
    ...    TELE_SALES_CONTROL_BY=HQ
    ${route_details}=   create dictionary
    ...   OP_TYPE=A
    set test variable     &{route_details}
    Given User sets the feature setup for telesales to ON passing with 'telesales' value
    When user updates app setup field force details using fixed data
    And user retrieves token access as hqadm
    When user creates route with given data
    Then expected return status code 201
    When user maps route to Level=Area, Node=Dungun
    Then expected return status code 200
    When user gets all route data
    Then expected return status code 200
    When user deletes route with created data
    Then expected return status code 200

6 - Able to retrieve all route details
    [Documentation]    Able to retrieve all route details
    [Tags]     huehue       distadm    9.5
    [Teardown]  run keywords
    ...     user deletes route with created data
    Given user retrieves token access as ${user_role}
    When user creates route as prerequisite
    And user maps route to Level=Area, Node=Dungun
    Then expected return status code 200
    When user gets route by using id
    Then expected return status code 200
    When user retrieve nodes to assign
    Then expected return status code 200
    When user retrieve nodes
    Then expected return status code 200
    When user retrieve route transaction control setting
    Then expected return either status code 200 or status code 204
    When user retrieve route calender view
    Then expected return either status code 200 or status code 204
    When user retrieve distributor geotree
    Then expected return status code 200
    When user retrieve customers assigned to routeplan
    Then expected return status code 200