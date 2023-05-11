*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/RepairReference/RepairReason/RepairReasonPost.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/RepairReference/RepairReason/RepairReasonPut.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/RepairReference/RepairReason/RepairReasonDelete.py


*** Test Cases ***
1 - Able to put to repair reason
    [Documentation]    Able to put to repair reason
    [Tags]    sysimp
    [Teardown]  user deletes repair reason
    Given user retrieves token access as sysimp
    When user posts to repair reason
    Then expected return status code 201
    When user puts to repair reason
    Then expected return status code 200
