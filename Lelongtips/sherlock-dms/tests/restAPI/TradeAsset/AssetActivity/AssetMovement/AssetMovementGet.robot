*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetActivity/AssetMovement/AssetMovementGet.py


*** Test Cases ***
1 - Able to retrieve all asset movement
    [Documentation]    Able to retrieve all asset movement
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves asset movement listing
    Then expected return status code 200

2 - Able to retrieve details for asset movement
    [Documentation]    Able to retrieve details for asset movement
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves asset movement details
    Then expected return status code 200
