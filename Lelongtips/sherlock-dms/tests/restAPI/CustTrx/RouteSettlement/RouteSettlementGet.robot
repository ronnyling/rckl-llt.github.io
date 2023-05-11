*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RoutePost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteMapping/RouteGeoMapping.py
Library           ${EXECDIR}${/}setup/yaml/YamlDataManipulator.py
Library           ${EXECDIR}${/}resources/restAPI/CustTrx/RouteSettlement/RouteSettlementGet.py

#Test Setup      user creates prerequisite for Route
#Test Teardown   user deletes prerequisite for Route


*** Test Cases ***
1 - Able to retrieve route settlement listing
    [Documentation]    Able to retrieve route settlement listing
    [Tags]      checkagain      build       distadm    9.5
    Given user retrieves token access as ${user_role}
    When user retrieves all route settlement
    Then expected return status code 200

2 - Able to retreive random route settlement details
    [Documentation]    Able to retrieve random route settlement details by id
    [Tags]      checkagain      build       distadm    9.5
    Given user retrieves token access as ${user_role}
    When user retrieves random route settlement details by id
    Then expected return status code 200

3 - Able to retreive transactions for route settlement
    [Documentation]    Able to retrieve transactions for route settlement by route
    [Tags]      build       distadm    9.5
    Given user retrieves token access as ${user_role}
    When user retrieves transactions for route settlement
    Then expected return status code 200