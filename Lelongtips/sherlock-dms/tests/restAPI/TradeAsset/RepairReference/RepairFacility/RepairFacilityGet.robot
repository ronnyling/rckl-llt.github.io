*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TradeAsset/RepairReference/RepairFacility/RepairFacilityGet.py


*** Test Cases ***
1 - Able to retrieve all repair facility
    [Documentation]    Able to retrieve all repair facility
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves repair facility listing
    Then expected return status code 200

2 - Able to retrieve details for repair facility
    [Documentation]    Able to retrieve details for repair facility
    [Tags]    sysimp
    Given user retrieves token access as sysimp
    When user retrieves repair facility details
    Then expected return status code 200
