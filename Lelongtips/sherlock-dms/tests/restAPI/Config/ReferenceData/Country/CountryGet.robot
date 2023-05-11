*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Country/CountryPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Country/CountryGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Country/CountryDelete.py

*** Test Cases ***
1 - Able to retrieve all Country data
    [Documentation]  To retrieve all country record via API
    [Tags]    sysimp     9.0
    Given user retrieves token access as ${user_role}
    When user creates country with RandomData
    Then expected return status code 201
    When user gets all countries data
    Then expected return status code 200
    When user deletes country with created data
    Then expected return status code 200

2 - Able to retrieve Country by using id
    [Documentation]  To retrieve country by passing in ID via API
    [Tags]    sysimp     9.0
    Given user retrieves token access as ${user_role}
    When user creates country with RandomData
    Then expected return status code 201
    When user gets country by using id
    Then expected return status code 200
    When user deletes country with created data
    Then expected return status code 200
