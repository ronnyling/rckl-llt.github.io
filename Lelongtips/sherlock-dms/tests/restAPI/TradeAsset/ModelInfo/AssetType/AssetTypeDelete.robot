*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/ModelInfo/AssetType/AssetTypePost.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/ModelInfo/AssetType/AssetTypeDelete.py


*** Test Cases ***
1 - Able to delete asset type
    [Documentation]    Able to delete asset type
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user posts to trade asset type
    Then expected return status code 201
    When user deletes asset type
    Then expected return status code 200
