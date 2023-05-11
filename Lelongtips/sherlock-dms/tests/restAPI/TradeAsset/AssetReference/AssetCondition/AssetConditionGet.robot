*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetReference/AssetCondition/AssetConditionGet.py


*** Test Cases ***
1 - Able to retrieve all asset condition
    [Documentation]    Able to retrieve all asset condition
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves asset condition listing
    Then expected return status code 200

2 - Able to retrieve details for asset condition
    [Documentation]    Able to retrieve details for asset condition
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves asset condition details
    Then expected return status code 200
