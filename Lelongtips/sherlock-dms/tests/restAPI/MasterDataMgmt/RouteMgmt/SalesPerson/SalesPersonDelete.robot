*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonDelete.py



*** Test Cases ***
1 - Able to delete telesales salesperson
    [Documentation]    Able to delete telesales salesperson
    [Tags]     distadm    9.3
    set prerequisites for salesperson
    Given user retrieves token access as ${user_role}
    And user creates telesales salesperson with random data
    When user deletes created salesperson
    Then expected return status code 200