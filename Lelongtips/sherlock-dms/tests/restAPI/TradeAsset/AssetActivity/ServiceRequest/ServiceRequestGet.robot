*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetActivity/ServiceRequest/ServiceRequestGet.py



*** Test Cases ***
1 - Able to retrieve all service request
    [Documentation]    Able to retrieve all service request
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves service request listing
    Then expected return status code 200

2 - Able to retrieve details for service request
    [Documentation]    Able to retrieve details for service request
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves service request details
    Then expected return status code 200
