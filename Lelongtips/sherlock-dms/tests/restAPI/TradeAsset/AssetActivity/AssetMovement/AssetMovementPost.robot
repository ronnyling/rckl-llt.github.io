*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetActivity/AssetMovement/AssetMovementPost.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetActivity/AssetMovement/AssetMovementDelete.py


*** Test Cases ***
1 - Able to posts to asset movement
    [Documentation]    Able to posts to asset movement
    [Tags]    sysimp
    [Teardown]  user deletes asset movement
    Given user retrieves token access as sysimp
    When user posts to asset movement
    Then expected return status code 201
