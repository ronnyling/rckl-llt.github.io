*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetReference/AssetCondition/AssetConditionPost.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetReference/AssetCondition/AssetConditionPut.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetReference/AssetCondition/AssetConditionDelete.py


*** Test Cases ***
1 - Able to put to asset condition
    [Documentation]    Able to put to asset condition
    [Tags]    sysimp
    [Teardown]  user deletes asset condition
    Given user retrieves token access as sysimp
    When user posts to asset condition
    Then expected return status code 201
    When user puts to asset condition
    Then expected return status code 200
