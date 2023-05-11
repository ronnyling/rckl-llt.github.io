*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/RepairReference/SparePart/SparePartGet.py


*** Test Cases ***
1 - Able to retrieve all spare part
    [Documentation]    Able to retrieve all spare part
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves spare part listing
    Then expected return status code 200

2 - Able to retrieve details for spare part
    [Documentation]    Able to retrieve details for spare part
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves spare part details
    Then expected return status code 200
