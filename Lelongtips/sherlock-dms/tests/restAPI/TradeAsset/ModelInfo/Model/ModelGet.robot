*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/ModelInfo/Model/ModelGet.py


*** Test Cases ***
1 - Able to retrieve all model
    [Documentation]    Able to retrieve all model
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves model listing
    Then expected return status code 200

2 - Able to retrieve details for model
    [Documentation]    Able to retrieve details for model
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves model details
    Then expected return status code 200
