*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/ModelInfo/AssetType/AssetTypePost.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/ModelInfo/AssetType/AssetTypePut.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/ModelInfo/AssetType/AssetTypeDelete.py


*** Test Cases ***
1 - Able to put to asset type
    [Documentation]    Able to put to asset type
    [Tags]    sysimp
    [Teardown]  user deletes asset type
    Given user retrieves token access as sysimp
    When user posts to trade asset type
    Then expected return status code 201
    When user puts to trade asset type
    Then expected return status code 200
