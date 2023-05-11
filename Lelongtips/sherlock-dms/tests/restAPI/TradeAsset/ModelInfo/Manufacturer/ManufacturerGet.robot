*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/ModelInfo/Manufacturer/ManufacturerGet.py


*** Test Cases ***
1 - Able to retrieve all manufacturer
    [Documentation]    Able to retrieve all manufacturer
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves manufacturer listing
    Then expected return status code 200

2 - Able to retrieve details for manufacturer
    [Documentation]    Able to retrieve details for manufacturer
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves manufacturer details
    Then expected return status code 200
