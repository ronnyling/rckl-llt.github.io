*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetMaster/AssetMasterGet.py


*** Test Cases ***
1 - Able to retrieve all asset master
    [Documentation]    Able to retrieve all asset master
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves asset master listing
    Then expected return status code 200

2 - Able to retrieve details for asset master
    [Documentation]    Able to retrieve details for asset master
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves asset master details
    Then expected return status code 200
