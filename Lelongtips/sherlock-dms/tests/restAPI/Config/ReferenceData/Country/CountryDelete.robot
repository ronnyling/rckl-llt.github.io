*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Country/CountryPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Country/CountryDelete.py

*** Test Cases ***
1 - Able to delete country with created data
    [Documentation]  To delete country by passing in id via API
    [Tags]    sysimp     9.0
    Given user retrieves token access as ${user_role}
    When user creates country with RandomData
    Then expected return status code 201
    When user deletes country with created data
    Then expected return status code 200
