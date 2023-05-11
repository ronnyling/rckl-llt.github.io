*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetReference/SpecialActivity/SpecialActivityPost.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetReference/SpecialActivity/SpecialActivityDelete.py


*** Test Cases ***
1 - Able to posts to special activity
    [Documentation]    Able to posts to special activity
    [Tags]    sysimp
    [Teardown]  user deletes special activity
    Given user retrieves token access as sysimp
    When user posts to special activity
    Then expected return status code 201
