** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/StructureGet.py
Library           ${EXECDIR}${/}resources/restAPI/Telesales/MyStore/TelesalesSalesOrderPost.py

Test Setup        run keywords
     ...    user retrieves token access as distadm
     ...    user gets distributor by using code 'DistEgg'
     ...    user gets route by using code 'DSTELE10'
     ...    user retrieves cust by using name 'Tele Auto Mart'
     ...    user get hierarchy id by giving hierarchy structure name General Product Hierarchy
     ...    user retrieves product hierarchy structure with valid data
     ...    user retrieves Category hierarchy with Jam code

*** Test Cases ***
1 - Able to post sales order product list with fixed data
    [Documentation]    Able to post sales order product list with fixed data
    [Tags]    telesales   9.3       test
    Given user retrieves token access as ${user_role}
    When user post fixed valid sales order product list
    Then expected return status code 200

2 - Unable to post sales order product list with invalid fixed data
    [Documentation]    Unable to post sales order product list with invalid fixed data
    [Tags]    telesales   9.3
    Given user retrieves token access as ${user_role}
    When user post fixed invalid sales order product list
    Then expected return status code 400