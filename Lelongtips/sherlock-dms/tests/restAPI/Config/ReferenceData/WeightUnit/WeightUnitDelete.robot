*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/WeightUnit/WeightUnitPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/WeightUnit/WeightUnitDelete.py

*** Test Cases ***
1 - Able to delete an weight unit
    [Documentation]    To Delete the weight unit
    [Tags]     sysimp    9.2
    Given user retrieves token access as ${user_role}
    When user creates valid weight unit with random data
    Then expected return status code 201
    When user deletes weight unit with created data
    Then expected return status code 200