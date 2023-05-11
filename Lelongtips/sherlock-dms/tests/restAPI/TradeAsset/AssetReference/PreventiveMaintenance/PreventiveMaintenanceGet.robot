*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetReference/PreventiveMaintenance/PreventiveMaintenanceGet.py


*** Test Cases ***
1 - Able to retrieve all preventive maintenance
    [Documentation]    Able to retrieve all preventive maintenance
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves preventive maintenance listing
    Then expected return status code 200

2 - Able to retrieve details for preventive maintenance
    [Documentation]    Able to retrieve details for preventive maintenance
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves preventive maintenance details
    Then expected return status code 200
