*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RoutePost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/RouteMapping/RouteGeoMapping.py
Library           ${EXECDIR}${/}setup/yaml/YamlDataManipulator.py
Library           ${EXECDIR}${/}resources/restAPI/CustTrx/RouteSettlement/RouteSettlementPost.py



*** Test Cases ***
1 - Able to create route settlement with random data
    [Documentation]    Able to create route settlement with random generated data via API
    [Tags]        distadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates route settlement with random data
    Then expected return status code 201