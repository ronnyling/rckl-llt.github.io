*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetReference/SpecialActivity/SpecialActivityPost.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetReference/SpecialActivity/SpecialActivityDelete.py


*** Test Cases ***
1 - Able to delete special activity
    [Documentation]    Able to delete special activity
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user posts to special activity
    Then expected return status code 201
    When user deletes special activity
    Then expected return status code 200
