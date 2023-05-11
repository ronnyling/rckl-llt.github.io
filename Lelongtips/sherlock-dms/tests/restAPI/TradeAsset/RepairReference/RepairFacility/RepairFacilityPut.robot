*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/RepairReference/RepairFacility/RepairFacilityPost.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/RepairReference/RepairFacility/RepairFacilityPut.py
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/RepairReference/RepairFacility/RepairFacilityDelete.py


*** Test Cases ***
1 - Able to put to repair facility
    [Documentation]    Able to put to repair facility
    [Tags]    sysimp
    [Teardown]  user deletes repair facility
    Given user retrieves token access as sysimp
    When user posts to repair facility
    Then expected return status code 201
    When user puts to repair facility
    Then expected return status code 200
