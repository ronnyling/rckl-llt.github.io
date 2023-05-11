*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetReference/TransferReason/TransferReasonPost.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetReference/TransferReason/TransferReasonPut.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetReference/TransferReason/TransferReasonDelete.py


*** Test Cases ***
1 - Able to put to transfer reason
    [Documentation]    Able to put to transfer reason
    [Tags]    sysimp
    [Teardown]  user deletes transfer reason
    Given user retrieves token access as sysimp
    When user posts to transfer reason
    Then expected return status code 201
    When user puts to transfer reason
    Then expected return status code 200
