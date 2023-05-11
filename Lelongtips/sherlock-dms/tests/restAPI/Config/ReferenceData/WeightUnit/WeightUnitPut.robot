*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/WeightUnit/WeightUnitPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/WeightUnit/WeightUnitGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/WeightUnit/WeightUnitPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/WeightUnit/WeightUnitDelete.py

*** Test Cases ***
1 - Able to update weight unit via API
    [Documentation]    To update a created weight unit
    [Tags]     sysimp    9.2
    ${weight_unit_details_put}=    create dictionary
    ...    WEIGHT_DESC=Weight Description by given data PUT
    set test variable   &{weight_unit_details_put}
    Given user retrieves token access as ${user_role}
    When user creates valid weight unit with random data
    Then expected return status code 201
    When user updates the created weight unit
    Then expected return status code 200
    When user deletes weight unit with created data
    Then expected return status code 200