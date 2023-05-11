*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetReference/TransferReason/TransferReasonPost.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetReference/TransferReason/TransferReasonDelete.py


*** Test Cases ***
1 - Able to delete transfer reason
    [Documentation]    Able to delete transfer reason
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user posts to transfer reason
    Then expected return status code 201
    When user deletes transfer reason
    Then expected return status code 200
