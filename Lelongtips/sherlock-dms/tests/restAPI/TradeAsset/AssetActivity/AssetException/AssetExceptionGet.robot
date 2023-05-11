*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetActivity/AssetException/AssetExceptionGet.py


*** Test Cases ***
1 - Able to retrieve all asset exception
    [Documentation]    Able to retrieve all asset exception
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves asset exception listing
    Then expected return status code 200
