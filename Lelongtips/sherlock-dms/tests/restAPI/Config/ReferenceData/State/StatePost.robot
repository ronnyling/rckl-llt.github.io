*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/State/StatePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/State/StateDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Country/CountryPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Country/CountryDelete.py

*** Test Cases ***
1 - Able to create State with random data
    [Documentation]  To create valid state with random generated data via API
    [Tags]    sysimp     9.0
    Given user retrieves token access as ${user_role}
    When user creates state with random data
    Then expected return status code 201
    When user deletes state with created data
    Then expected return status code 200

2- Able to create State with fixed data
    [Documentation]  To create valid state with fixed data via API
    [Tags]    sysimp     9.0
    ${state_details}=    create dictionary
    ...    STATE_NAME=AutoTest
    set test variable   &{state_details}
    Given user retrieves token access as ${user_role}
    When user creates state with fixed data
    Then expected return status code 201
    When user deletes state with created data
    Then expected return status code 200

3- Able to create State and relate to Country
    [Documentation]  To create valid state and link relationship with Country via API
    [Tags]     sysimp     9.0
    Given user retrieves token access as ${user_role}
    When user creates country with random data
    Then expected return status code 201
    When user creates state with random data
    Then expected return status code 201
    When user deletes state with created data
    Then expected return status code 200
    When user deletes country with created data
    Then expected return status code 200
