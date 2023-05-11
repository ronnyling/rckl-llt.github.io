*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorShipToGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorPost.py

*** Test Cases ***

1 - Able to retrieve first ship to ID record for Distributor
    [Documentation]    Able to retrieve shipto details for current distributor
    [Tags]    distadm    9.0
    Given user retrieves token access as ${user_role}
    When user retrieves all distributors list
    Then expected return status code 200
    When user retrieves shipto details
    Then expected return status code 200

2 - Able to retrieve ship to details
    [Documentation]    Able to retrieve shipto details for current distributor
    [Tags]    distadm    9.5
    Given user retrieves token access as ${user_role}
    When user retrieves all distributors list
    And user retrieves shipto details
    Then expected return status code 200
    When user retrieves shipto details by id
    Then expected return status code 200
