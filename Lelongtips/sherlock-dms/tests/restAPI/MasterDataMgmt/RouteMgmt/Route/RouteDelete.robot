*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RoutePost.py
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
1 - Able to delete Route using created data
    [Documentation]    To delete route using created data via API
    [Tags]     distadm    9.0    NRSZUANQ-28428
    Given user retrieves token access as ${user_role}
    When user creates route with random data
    Then expected return status code 201
    When user maps route to Level=Area, Node=Dungun
    Then expected return status code 200
    When user deletes route with created data
    Then expected return status code 200

2. - Able to DELETE HQ TeleSales route created by HQ using HQ access
    [Documentation]    To delete HQ TeleSales route created by HQ using HQ access via API
    [Tags]     hqadm    9.3     NRSZUANQ-56276
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
    When user deletes route with created data
    Then expected return status code 200

3. - Unable to DELETE HQ TeleSales route created by HQ using distributor access
    [Documentation]    To delete HQ TeleSales route created by HQ using distributor access via API
    [Tags]     distadm     9.3     NRSZUANQ-56277
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
    Given user retrieves token access as ${user_role}
    When user deletes route with created data
    Then expected return status code 400

4. - Able to DELETE TeleSales route created by Distributor using distributor access
    [Documentation]    To delete TeleSales route created by Distributor using Distributor access via API
    [Tags]     distadm    9.3     NRSZUANQ-56278
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
    When user deletes route with created data
    Then expected return status code 200

5. - Able to DELETE TeleSales route when feature setup is turned on
    [Documentation]    To delete TeleSales and HQ TeleSales route when feature setup is turned on via API
    [Tags]     distadm     9.3     NRSZUANQ-56391
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
    When user deletes route with created data
    Then expected return status code 200

6. - Able to DELETE HQ TeleSales route when feature setup is turned on
    [Documentation]    To delete TeleSales and HQ TeleSales route when feature setup is turned on via API
    [Tags]     hqadm     9.3     NRSZUANQ-56391
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
    When user deletes route with created data
    Then expected return status code 200

7. - Unable to DELETE TeleSales route when feature setup is turned off
    [Documentation]    To delete TeleSales and HQ TeleSales route when feature setup is turned off via API
    [Tags]     distadm     9.3     NRSZUANQ-56393
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
    When user updates app setup field force details using fixed data
    When user deletes route with created data
    Then expected return status code 403

8. - Unable to DELETE HQ TeleSales route when feature setup is turned off
    [Documentation]    To delete TeleSales and HQ TeleSales route when feature setup is turned off via API
    [Tags]     hqadm     9.3     NRSZUANQ-56393
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
    When user updates app setup field force details using fixed data
    When user deletes route with created data
    Then expected return status code 403
