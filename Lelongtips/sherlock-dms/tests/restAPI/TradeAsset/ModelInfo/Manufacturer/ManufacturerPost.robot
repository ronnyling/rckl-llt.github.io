*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/ModelInfo/Manufacturer/ManufacturerPost.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/ModelInfo/Manufacturer/ManufacturerDelete.py


*** Test Cases ***
1 - Able to posts to manufacturer
    [Documentation]    Able to posts to manufacturer
    [Tags]    sysimp
    [Teardown]  user deletes manufacturer
    Given user retrieves token access as sysimp
    When user posts to manufacturer
    Then expected return status code 201
