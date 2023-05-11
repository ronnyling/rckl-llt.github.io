*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/AssetReference/SpecialActivity/SpecialActivityGet.py


*** Test Cases ***
1 - Able to retrieve all special activity
    [Documentation]    Able to retrieve all special activity
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves special activity listing
    Then expected return status code 200

2 - Able to retrieve details for special activity
    [Documentation]    Able to retrieve details for special activity
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves special activity details
    Then expected return status code 200
