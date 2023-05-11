*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/RepairReference/RepairReason/RepairReasonGet.py


*** Test Cases ***
1 - Able to retrieve all repair reason
    [Documentation]    Able to retrieve all repair reason
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves repair reason listing
    Then expected return status code 200

2 - Able to retrieve details for repair reason
    [Documentation]    Able to retrieve details for repair reason
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves repair reason details
    Then expected return status code 200
