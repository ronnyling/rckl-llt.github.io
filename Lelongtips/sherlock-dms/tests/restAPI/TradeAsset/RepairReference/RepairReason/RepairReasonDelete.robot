*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/RepairReference/RepairReason/RepairReasonPost.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/RepairReference/RepairReason/RepairReasonDelete.py


*** Test Cases ***
1 - Able to delete repair reason
    [Documentation]    Able to delete repair reason
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user posts to repair reason
    Then expected return status code 201
    When user deletes repair reason
    Then expected return status code 200
