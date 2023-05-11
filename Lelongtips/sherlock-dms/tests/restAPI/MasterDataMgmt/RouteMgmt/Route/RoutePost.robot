*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RoutePost.py
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
1 - Able to create Route using random data
    [Documentation]    To create valid route using random data via API
    [Tags]     distadm    9.0   NRSZUANQ-28413     NRSZUANQ-29355    bug-ticket:NRSZUANQ-46046
    Given user retrieves token access as ${user_role}
    When user creates route with random data
    Then expected return status code 201
    When user maps route to Level=Area, Node=Dungun
    Then expected return status code 200
    And user deletes route with created data
    Then expected return status code 200

2 - Able to create route using given data
    [Documentation]    To create valid route using given data via API
    [Tags]     distadm    9.0     bug-ticket:NRSZUANQ-46046
    ${route_details}=   create dictionary
    ...   ROUTE_CD=TestR0117
    ...   ROUTE_NAME=TestRC117
    set test variable     &{route_details}
    Given user retrieves token access as ${user_role}
    When user creates route with fixed data
    Then expected return status code 201
    When user maps route to Level=Area, Node=Dungun
    Then expected return status code 200
    When user deletes route with created data
    Then expected return status code 200

3 - Able to POST Route by passing Null to Non Prime Warehouse
    [Documentation]    To create route using null in non prime warehouse via API
    [Tags]     distadm    9.1    NRSZUANQ-28431
    ${route_details}=   create dictionary
    ...   NON_PRIME_WHS=${null}
    set test variable     &{route_details}
    Given user retrieves token access as ${user_role}
    When user creates route with fixed data
    Then expected return status code 201
    When user maps route to Level=Area, Node=Dungun
    Then expected return status code 200
    When user deletes route with created data
    Then expected return status code 200

4 - Unable to POST Route by using Non Prime Warehouse in Main warehouse field
    [Documentation]    To create route using non prime warehouse in Main warehouse via API
    [Tags]     distadm    9.1    NRSZUANQ-28433
    ${record}=     user retrieves data from yaml   1-RoutePre.yaml  Output
    ${route_wh}=   create dictionary
    ...    ID=${record['2_WarehousePost']['ID']}
    ${route_details}=   create dictionary
    ...   MAIN_WHSE=${route_wh}
    set test variable     &{route_details}
    Given user retrieves token access as ${user_role}
    When user creates route with invalid data
    Then expected return status code 404

5 - Unable to POST Route by using Prime Warehouse in Non Prime Warehouse field
    [Documentation]    To create route using Prime warehouse in non prime warehouse via API
    [Tags]     distadm    9.1    NRSZUANQ-28437
    ${record}=     user retrieves data from yaml   1-RoutePre.yaml  Output
    ${route_wh}=   create dictionary
    ...    ID=${record['1_WarehousePost']['ID']}
    ${route_details}=   create dictionary
    ...    NON_PRIME_WHS=${route_wh}
    set test variable     &{route_details}
    Given user retrieves token access as ${user_role}
    When user creates route with invalid data
    Then expected return status code 404

6. - Able to POST TeleSales route at Sales office and below level
    [Documentation]    To create telesales route at Sales office and below level via API
    [Tags]     distadm    9.3       NRSZUANQ-56263
    ${AppSetupDetails}=    create dictionary
    ...    TELE_SALES_CONTROL_BY=DIST
    ${route_details}=   create dictionary
    ...   OP_TYPE=T
    set test variable     &{route_details}
    Given user sets the feature setup for telesales to ON passing with 'telesales' value
    When user updates app setup field force details using fixed data
    And user retrieves token access as ${user_role}
    When user creates route with fixed data
    Then expected return status code 201
    When user maps route to Level=Area, Node=Dungun
    Then expected return status code 200
    When user deletes route with created data
    Then expected return status code 200

7. - Unable to POST TeleSales route with GPS indicator on
    [Documentation]    To create TeleSales and HQ TeleSales route with GPS indicator on via API
    [Tags]     distadm     9.3     NRSZUANQ-56265
    ${AppSetupDetails}=    create dictionary
    ...    TELE_SALES_CONTROL_BY=DIST
    ${route_details}=   create dictionary
    ...   OP_TYPE=T
    ...   GPS_IND=${true}
    set test variable     &{route_details}
    Given user sets the feature setup for telesales to ON passing with 'telesales' value
    When user updates app setup field force details using fixed data
    And user retrieves token access as ${user_role}
    When user creates route with fixed data
    Then expected return status code 400

8. - Unable to POST HQ TeleSales route with GPS indicator on
    [Documentation]    To create TeleSales and HQ TeleSales route with GPS indicator on via API
    [Tags]     hqadm     9.3     NRSZUANQ-56265
    ${AppSetupDetails}=    create dictionary
    ...    TELE_SALES_CONTROL_BY=HQ
    ${route_details}=   create dictionary
    ...   OP_TYPE=A
    ...   GPS_IND=${true}
    set test variable     &{route_details}
    Given user sets the feature setup for telesales to ON passing with 'telesales' value
    When user updates app setup field force details using fixed data
    And user retrieves token access as hqadm
    When user creates route with fixed data
    Then expected return status code 400

9. - Unable to POST TeleSales route with HHT user flag on
    [Documentation]    To create TeleSales and HQ TeleSales route with HHT user flag on via API
    [Tags]     distadm     9.3     NRSZUANQ-56268
    ${AppSetupDetails}=    create dictionary
    ...    TELE_SALES_CONTROL_BY=DIST
    ${route_details}=   create dictionary
    ...   OP_TYPE=T
    ...   HHT_USRFLG=YES
    set test variable     &{route_details}
    Given user sets the feature setup for telesales to ON passing with 'telesales' value
    When user updates app setup field force details using fixed data
    And user retrieves token access as ${user_role}
    When user creates route with fixed data
    Then expected return status code 400

10. - Unable to POST HQ TeleSales route with HHT user flag on
    [Documentation]    To create TeleSales and HQ TeleSales route with HHT user flag on via API
    [Tags]     hqadm     9.3     NRSZUANQ-56268
    ${AppSetupDetails}=    create dictionary
    ...    TELE_SALES_CONTROL_BY=HQ
    ${route_details}=   create dictionary
    ...   OP_TYPE=A
    ...   HHT_USRFLG=YES
    set test variable     &{route_details}
    Given user sets the feature setup for telesales to ON passing with 'telesales' value
    When user updates app setup field force details using fixed data
    And user retrieves token access as hqadm
    When user creates route with fixed data
    Then expected return status code 400

11. - Unable to POST TeleSales route with Van
    [Documentation]    To create TeleSales and HQ TeleSales route with Van via API
    [Tags]     distadm     9.3     NRSZUANQ-56269
    ${AppSetupDetails}=    create dictionary
    ...    TELE_SALES_CONTROL_BY=DIST
    ${route_details}=   create dictionary
    ...   OP_TYPE=T
    ...   VAN_CD=VANKY
    set test variable     &{route_details}
    Given user sets the feature setup for telesales to ON passing with 'telesales' value
    When user updates app setup field force details using fixed data
    And user retrieves token access as ${user_role}
    When user creates route with fixed data
    Then expected return status code 400

12. - Unable to POST HQ TeleSales route with Van
    [Documentation]    To create TeleSales and HQ TeleSales route with Van via API
    [Tags]     hqadm     9.3     NRSZUANQ-56269
    ${AppSetupDetails}=    create dictionary
    ...    TELE_SALES_CONTROL_BY=HQ
    ${route_details}=   create dictionary
    ...   OP_TYPE=A
    ...   VAN_CD=VANKY
    set test variable     &{route_details}
    Given user sets the feature setup for telesales to ON passing with 'telesales' value
    When user updates app setup field force details using fixed data
    And user retrieves token access as hqadm
    When user creates route with fixed data
    Then expected return status code 400

13. - Able to POST TeleSales route with Warehouse Mapping in General Info
    [Documentation]    To create TeleSales route with Warehouse Mapping in General Info via API
    [Tags]     distadm    9.3     NRSZUANQ-56270
    ${AppSetupDetails}=    create dictionary
    ...    TELE_SALES_CONTROL_BY=DIST
    ${route_details}=   create dictionary
    ...   OP_TYPE=T
    set test variable     &{route_details}
    Given user sets the feature setup for telesales to ON passing with 'telesales' value
    When user updates app setup field force details using fixed data
    And user retrieves token access as ${user_role}
    When user creates route with fixed data
    Then expected return status code 201
    When user maps route to Level=Area, Node=Dungun
    Then expected return status code 200
    When user deletes route with created data
    Then expected return status code 200

14. - Able to POST Telesales route when feature setup is turned on
     [Documentation]    To create Telesales or HQ Telesales route when feature setup is turned on via API
     [Tags]     distadm     9.3     NRSZUANQ-56382
     ${AppSetupDetails}=    create dictionary
     ...    TELE_SALES_CONTROL_BY=DIST
    ${route_details}=   create dictionary
    ...   OP_TYPE=T
    set test variable     &{route_details}
     Given user sets the feature setup for telesales to ON passing with 'telesales' value
     When user updates app setup field force details using fixed data
     And user retrieves token access as ${user_role}
     When user creates route with fixed data
     Then expected return status code 201
     When user maps route to Level=Area, Node=Dungun
     Then expected return status code 200
     When user deletes route with created data
     Then expected return status code 200

15. - Able to POST HQ Telesales route when feature setup is turned on
     [Documentation]    To create Telesales or HQ Telesales route when feature setup is turned on via API
     [Tags]     hqadm     9.3     NRSZUANQ-56382
     ${AppSetupDetails}=    create dictionary
     ...    TELE_SALES_CONTROL_BY=HQ
    ${route_details}=   create dictionary
    ...   OP_TYPE=A
    set test variable     &{route_details}
     Given user sets the feature setup for telesales to ON passing with 'telesales' value
     When user updates app setup field force details using fixed data
     And user retrieves token access as hqadm
     When user creates route with fixed data
     Then expected return status code 201
     When user maps route to Level=Area, Node=Dungun
     Then expected return status code 200
     When user deletes route with created data
     Then expected return status code 200

16. - Unable to POST Telesales route when feature setup is turned off
    [Documentation]    To create Telesales or HQ Telesales route when feature setup is turned off via API
    [Tags]     distadm     9.3     NRSZUANQ-56386
    ${AppSetupDetails}=    create dictionary
    ...    TELE_SALES_CONTROL_BY=DIST
    ${route_details}=   create dictionary
    ...   OP_TYPE=T
    set test variable     &{route_details}
    Given user sets the feature setup for telesales to OFF passing with 'telesales' value
    When user updates app setup field force details using fixed data
    And user retrieves token access as ${user_role}
    When user creates route with fixed data
    Then expected return status code 400

17. - Unable to POST HQ Telesales route when feature setup is turned off
    [Documentation]    To create Telesales or HQ Telesales route when feature setup is turned off via API
    [Tags]     hqadm     9.3     NRSZUANQ-56386
    ${AppSetupDetails}=    create dictionary
    ...    TELE_SALES_CONTROL_BY=HQ
    ${route_details}=   create dictionary
    ...   OP_TYPE=A
    set test variable     &{route_details}
    Given user sets the feature setup for telesales to OFF passing with 'telesales' value
    When user updates app setup field force details using fixed data
    And user retrieves token access as hqadm
    When user creates route with fixed data
    Then expected return status code 400

18. - Able to POST Telesales route when Telesales is controlled by Distributor
    [Documentation]    To create Telesales route when Telesales is controlled by Distributor via API
    [Tags]     distadm    9.3     NRSZUANQ-56388
    ${AppSetupDetails}=    create dictionary
    ...    TELE_SALES_CONTROL_BY=DIST
    ${route_details}=   create dictionary
    ...   OP_TYPE=T
    set test variable     &{route_details}
    Given user sets the feature setup for telesales to ON passing with 'telesales' value
    When user updates app setup field force details using fixed data
    And user retrieves token access as ${user_role}
    When user creates route with fixed data
    Then expected return status code 201
    When user maps route to Level=Area, Node=Dungun
    Then expected return status code 200
    When user deletes route with created data
    Then expected return status code 200

19. - Able to POST HQ Telesales route when Telesales is controlled by HQ
    [Documentation]    To create HQ Telesales route when Telesales is controlled by HQ via API
    [Tags]     hqadm    9.3     NRSZUANQ-56387
    ${AppSetupDetails}=    create dictionary
    ...    TELE_SALES_CONTROL_BY=HQ
    ${route_details}=   create dictionary
    ...   OP_TYPE=A
    set test variable     &{route_details}
    Given user sets the feature setup for telesales to ON passing with 'telesales' value
    When user updates app setup field force details using fixed data
    And user retrieves token access as hqadm
    When user creates route with fixed data
    Then expected return status code 201
    When user maps route to Level=Area, Node=Dungun
    Then expected return status code 200
    When user deletes route with created data
    Then expected return status code 200

20. - Unable to POST TeleSales route when TeleSales Control by HQ
    [Documentation]    To create TeleSales route when TeleSales Control by HQ via API
    [Tags]     distadm    9.3     NRSZUANQ-56427
    ${AppSetupDetails}=    create dictionary
    ...    TELE_SALES_CONTROL_BY=HQ
    ${route_details}=   create dictionary
    ...   OP_TYPE=T
    set test variable     &{route_details}
    Given user sets the feature setup for telesales to ON passing with 'telesales' value
    When user updates app setup field force details using fixed data
    And user retrieves token access as ${user_role}
    When user creates route with fixed data
    Then expected return status code 400

21. - Unable to POST HQ TeleSales route when TeleSales Control by Distributor
    [Documentation]    To create HQ TeleSales route when TeleSales Control by Distributor via API
    [Tags]     hqadm    9.3     NRSZUANQ-56428
    ${AppSetupDetails}=    create dictionary
    ...    TELE_SALES_CONTROL_BY=DIST
    ${route_details}=   create dictionary
    ...   OP_TYPE=A
    set test variable     &{route_details}
    Given user sets the feature setup for telesales to ON passing with 'telesales' value
    When user updates app setup field force details using fixed data
    And user retrieves token access as hqadm
    When user creates route with fixed data
    Then expected return status code 400

22. - Able to POST HQ TeleSales route at equal to or below his level
    [Documentation]    To create HQ TeleSales route at equal to or below his level via API
    [Tags]     hqadm    9.3     NRSZUANQ-56455
    ${AppSetupDetails}=    create dictionary
    ...    TELE_SALES_CONTROL_BY=HQ
    ${route_details}=   create dictionary
    ...   OP_TYPE=A
    set test variable     &{route_details}
    Given user sets the feature setup for telesales to ON passing with 'telesales' value
    When user updates app setup field force details using fixed data
    And user retrieves token access as hqadm
    When user creates route with fixed data
    Then expected return status code 201
    When user maps route to Level=Area, Node=Dungun
    Then expected return status code 200
    When user deletes route with created data
    Then expected return status code 200
