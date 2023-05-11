*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/ModelInfo/Model/ModelPost.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/ModelInfo/Model/ModelDelete.py


*** Test Cases ***
1 - Able to delete model
    [Documentation]    Able to delete model
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user posts to model
    Then expected return status code 201
    When user deletes model
    Then expected return status code 200
