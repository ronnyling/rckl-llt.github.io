*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetReference/TransferReason/TransferReasonGet.py


*** Test Cases ***
1 - Able to retrieve all transfer reason
    [Documentation]    Able to retrieve all transfer reason
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves transfer reason listing
    Then expected return status code 200
