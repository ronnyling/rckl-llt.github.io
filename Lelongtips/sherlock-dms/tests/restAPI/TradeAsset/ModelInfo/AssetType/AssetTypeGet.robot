*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/ModelInfo/AssetType/AssetTypeGet.py


*** Test Cases ***
1 - Able to retrieve all asset type
    [Documentation]    Able to retrieve all asset type
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves trade asset type listing
    Then expected return status code 200

2 - Able to retrieve details for asset type
    [Documentation]    Able to retrieve details for asset type
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves trade asset type details
    Then expected return status code 200
