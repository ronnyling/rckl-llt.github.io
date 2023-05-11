*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/RepairReference/SparePart/SparePartPost.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/RepairReference/SparePart/SparePartDelete.py


*** Test Cases ***
1 - Able to posts to spare part
    [Documentation]    Able to posts to spare part
    [Tags]    sysimp
    [Teardown]  user deletes spare part
    Given user retrieves token access as sysimp
    When user posts to spare part
    Then expected return status code 201
