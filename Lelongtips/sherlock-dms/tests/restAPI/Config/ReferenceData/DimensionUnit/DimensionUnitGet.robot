*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/DimensionUnit/DimensionUnitPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/DimensionUnit/DimensionUnitGet.py

*** Test Cases ***
1 - Able to get all dimension unit
    [Documentation]    To retrieve all valid dimension unit
    [Tags]     sysimp    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves all dimension unit
    Then expected return status code 200

2 - Able to get dimension unit by ID
    [Documentation]    To retrieve an dimension unit by ID
    [Tags]     sysimp    9.2
    Given user retrieves token access as ${user_role}
    When user creates valid dimension unit with random data
    Then expected return status code 201
    When user retrieves dimension unit by ID
    Then expected return status code 200