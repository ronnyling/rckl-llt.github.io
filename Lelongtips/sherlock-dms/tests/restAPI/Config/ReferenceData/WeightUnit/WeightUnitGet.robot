*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/WeightUnit/WeightUnitPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/WeightUnit/WeightUnitGet.py

*** Test Cases ***
1 - Able to get all weight unit
    [Documentation]    To retrieve all valid weight unit
    [Tags]     sysimp    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves all weight unit
    Then expected return status code 200

2 - Able to get weight unit by ID
    [Documentation]    To retrieve an weight unit by ID
    [Tags]     sysimp    9.2
    Given user retrieves token access as ${user_role}
    When user creates valid weight unit with random data
    Then expected return status code 201
    When user retrieves weight unit by ID
    Then expected return status code 200