*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/ModelInfo/Model/ModelPost.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/ModelInfo/Model/ModelDelete.py


*** Test Cases ***
1 - Able to posts to model
    [Documentation]    Able to posts to model
    [Tags]    sysimp
    [Teardown]  user deletes model
    Given user retrieves token access as sysimp
    When user posts to model
    Then expected return status code 201
