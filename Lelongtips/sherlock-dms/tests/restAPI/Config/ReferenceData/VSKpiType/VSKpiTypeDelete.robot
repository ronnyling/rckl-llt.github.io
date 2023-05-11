*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/VSKpiType/VSKpiTypeDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/VSKpiType/VSKpiTypePost.py
*** Test Cases ***
1 - Able to delete kpi type by valid id
    [Documentation]    Able to delete kpi type with valid id
    [Tags]    sysimp    9.2
    Given user retrieves token access as ${user_role}
    When user creates kpi type using random data
    Then expected return status code 201
    When user deletes kpi type with valid ID
    Then expected return status code 200

2 - Unable to delete kpi type by with invalid ID
    [Documentation]    Unable to delete kpi type with invalid id
    [Tags]     sysimp   9.2
    Given user retrieves token access as ${user_role}
    When user creates kpi type using random data
    Then expected return status code 201
    When user deletes kpi type with invalid ID
    Then expected return status code 404

