*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetMaster/AssetMasterPost.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetMaster/AssetMasterDelete.py


*** Test Cases ***
1 - Able to posts to asset master
    [Documentation]    Able to posts to asset master
    [Tags]    sysimp
    [Teardown]  user deletes asset master
    Given user retrieves token access as sysimp
    When user posts to asset master
    Then expected return status code 201
