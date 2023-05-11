*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RoutePost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RoutePut.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteMapping/RouteGeoMapping.py
Library           ${EXECDIR}${/}setup/yaml/YamlDataManipulator.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/FieldForcePut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py

Test Setup      run keywords
...    user creates prerequisite for Route
...    Given user retrieves token access as hqadm
...    user retrieves details of application setup
Test Teardown   user deletes prerequisite for Route

*** Test Cases ***
1 - Able to update Route using random data
    [Documentation]    To update route using random data via API
    [Tags]     distadm    9.0    NRSZUANQ-28417
    Given user retrieves token access as ${user_role}
    When user creates route with random data
    Then expected return status code 201
    When user maps route to Level=Area, Node=Dungun
    Then expected return status code 200
    When user updates route with random data
    Then expected return status code 200
    When user deletes route with created data
    Then expected return status code 200

2 - Unable to PUT Route by using Non Prime Warehouse in Main warehouse field
    [Documentation]    To update route using non prime warehouse in main warehouse field via API
    [Tags]     distadm    9.1    NRSZUANQ-28439
    Given user retrieves token access as ${user_role}
    When user creates route with random data
    Then expected return status code 201
    When user maps route to Level=Area, Node=Dungun
    Then expected return status code 200
    ${record}=     user retrieves data from yaml   1-RoutePre.yaml  Output
    ${route_wh}=   create dictionary
    ...    ID=${record['2_WarehousePost']['ID']}
    ${route_details}=   create dictionary
    ...   MAIN_WHSE=${route_wh}
    set test variable     &{route_details}
    When user updates route with fixed data
    Then expected return status code 404
    When user deletes route with created data
    Then expected return status code 200

3 - Unable to PUT Route by using Prime Warehouse in Non Prime Warehouse field
    [Documentation]    To update route using prime warehouse in non prime warehouse field via API
    [Tags]     distadm    9.1    NRSZUANQ-28441
    Given user retrieves token access as ${user_role}
    When user creates route with random data
    Then expected return status code 201
    When user maps route to Level=Area, Node=Dungun
    Then expected return status code 200
    ${record}=     user retrieves data from yaml   1-RoutePre.yaml  Output
    ${route_wh}=   create dictionary
    ...    ID=${record['1_WarehousePost']['ID']}
    ${route_details}=   create dictionary
    ...    NON_PRIME_WHS=${route_wh}
    set test variable     &{route_details}
    When user updates route with fixed data
    Then expected return status code 404
    When user deletes route with created data
    Then expected return status code 200

4. - Able to PUT TeleSales route when feature setup is turned on
    [Documentation]    To update TeleSales and HQ TeleSales route when feature setup is turned on via API
    [Tags]     distadm     9.3    NRSZUANQ-56390
    ${AppSetupDetails}=    create dictionary
    ...    TELE_SALES_CONTROL_BY=DIST
    ${route_details}=   create dictionary
    ...   OP_TYPE=T
    set test variable     &{route_details}
    Given User sets the feature setup for telesales to ON passing with 'telesales' value
    When user updates app setup field force details using fixed data
    And user retrieves token access as ${user_role}
    When user creates route with fixed data
    Then expected return status code 201
    When user maps route to Level=Area, Node=Dungun
    Then expected return status code 200
    When user updates route with random data
    Then expected return status code 200
    When user deletes route with created data
    Then expected return status code 200

5. - Able to PUT HQ TeleSales route when feature setup is turned on
    [Documentation]    To update TeleSales and HQ TeleSales route when feature setup is turned on via API
    [Tags]     hqadm     9.3    NRSZUANQ-56390
    ${AppSetupDetails}=    create dictionary
    ...    TELE_SALES_CONTROL_BY=HQ
    ${route_details}=   create dictionary
    ...   OP_TYPE=A
    set test variable     &{route_details}
    Given User sets the feature setup for telesales to ON passing with 'telesales' value
    When user updates app setup field force details using fixed data
    And user retrieves token access as hqadm
    When user creates route with fixed data
    Then expected return status code 201
    When user maps route to Level=Area, Node=Dungun
    Then expected return status code 200
    When user updates route with random data
    Then expected return status code 200
    When user deletes route with created data
    Then expected return status code 200

6. - Unable to PUT TeleSales route when feature setup is turned off
    [Documentation]    To update TeleSales and HQ TeleSales route when feature setup is turned off via API
    [Tags]     distadm     9.3    NRSZUANQ-56392
    ${AppSetupDetails}=    create dictionary
    ...    TELE_SALES_CONTROL_BY=DIST
    ${route_details}=   create dictionary
    ...   OP_TYPE=T
    set test variable     &{route_details}
    Given User sets the feature setup for telesales to ON passing with 'telesales' value
    When user updates app setup field force details using fixed data
    And user retrieves token access as ${user_role}
    When user creates route with fixed data
    Then expected return status code 201
    When user maps route to Level=Area, Node=Dungun
    Then expected return status code 200
    Given User sets the feature setup for telesales to OFF passing with 'telesales' value
    When user updates route with random data
    Then expected return status code 403
    When user deletes route with created data
    Then expected return status code 403

7. - Unable to PUT HQ TeleSales route when feature setup is turned off
    [Documentation]    To update TeleSales and HQ TeleSales route when feature setup is turned off via API
    [Tags]     hqadm     9.3    NRSZUANQ-56392
    ${AppSetupDetails}=    create dictionary
    ...    TELE_SALES_CONTROL_BY=HQ
    ${route_details}=   create dictionary
    ...   OP_TYPE=A
    set test variable     &{route_details}
    Given User sets the feature setup for telesales to ON passing with 'telesales' value
    When user updates app setup field force details using fixed data
    And user retrieves token access as hqadm
    When user creates route with fixed data
    Then expected return status code 201
    When user maps route to Level=Area, Node=Dungun
    Then expected return status code 200
    Given User sets the feature setup for telesales to OFF passing with 'telesales' value
    When user updates route with random data
    Then expected return status code 403
    When user deletes route with created data
    Then expected return status code 403

8 - Able to update Route transaction control setting
    [Documentation]    Able to update Route transaction control setting
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user creates route with random data
    Then expected return status code 201
    When user maps route to Level=Area, Node=Dungun
    Then expected return status code 200
    When user puts route transaction control setting
    Then expected return status code 200
    When user deletes route with created data
    Then expected return status code 200

