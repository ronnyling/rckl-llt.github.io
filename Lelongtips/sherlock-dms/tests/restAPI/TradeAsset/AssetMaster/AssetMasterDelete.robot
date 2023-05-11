*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetMaster/AssetMasterPost.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetMaster/AssetMasterDelete.py


*** Test Cases ***
1 - Able to delete asset master
    [Documentation]    Able to delete asset master
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user posts to asset master
    Then expected return status code 201
    When user deletes asset master
    Then expected return status code 200
