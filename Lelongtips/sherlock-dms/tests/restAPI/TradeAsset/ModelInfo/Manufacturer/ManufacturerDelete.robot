*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/ModelInfo/Manufacturer/ManufacturerPost.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/ModelInfo/Manufacturer/ManufacturerDelete.py


*** Test Cases ***
1 - Able to delete manufacturer
    [Documentation]    Able to delete manufacturer
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user posts to manufacturer
    Then expected return status code 201
    When user deletes manufacturer
    Then expected return status code 200
