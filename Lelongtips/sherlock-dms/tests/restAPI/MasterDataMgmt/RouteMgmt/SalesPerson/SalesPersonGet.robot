*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonGet.py



*** Test Cases ***
1 - Able to get salesperson via API and return 200
    [Documentation]    Able to Get ALl Sales Person via API
    [Tags]     distadm    9.0     BUG-NRSZUANQ-38510     BUG-NRSZUANQ-45099
    Given user retrieves token access as ${user_role}
    When user gets route salesperson info
    Then expected return status code 200

2 - Able to get salesperson by ID via API and return 200
    [Documentation]    Able to Get a Sales Person by ID via API
    [Tags]     distadm    9.0     BUG-NRSZUANQ-38510     BUG-NRSZUANQ-45099
    Given user retrieves token access as ${user_role}
    When user gets route salesperson info by id
    Then expected return status code 400

3 - Able to get telesales salesperson via API and return 200
    [Documentation]    Able to get telesales salesperson via API and return 200
    [Tags]     distadm    9.3
    set prerequisites for salesperson
    Given user retrieves token access as ${user_role}
    And user creates telesales salesperson with random data
    When user gets route salesperson info by id
    Then expected return status code 200

