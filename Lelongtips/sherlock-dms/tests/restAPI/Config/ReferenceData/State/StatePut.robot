*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/State/StatePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/State/StateDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/State/StatePut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Country/CountryPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Country/CountryDelete.py

Test Setup     run keywords
...    user retrieves token access as ${user_role}
...    AND    user creates state as prerequisite

Test Teardown  user deletes created state as teardown

*** Test Cases ***
1 - Able to edit State with random data
    [Documentation]  To edit state with random generated data by passing in id via API
    [Tags]    sysimp     9.0
    When user edits state with random data
    Then expected return status code 200

2- Able to edit State with fixed data
    [Documentation]  To edit state with fixed data by passing in id via API
    [Tags]    sysimp     9.0
    ${state_details}=    create dictionary
    ...    STATE_CD=PHAhang
    ...    STATE_NAME=Pahang2
    set test variable   &{state_details}
    When user edits state with fixed data
    Then expected return status code 200

3- Able to create State and relate to Country
    [Documentation]  To edit valid state to link relationship with Country via API
    [Tags]     sysimp     9.0
    When user creates country with random data
    Then expected return status code 201
    When user edits state with created country data
    Then expected return status code 200
    When user deletes country with created data
    Then expected return status code 200

4 - Unable to edit State by using invalid id
    [Documentation]  Unable to edit country by passing in invalid ID via API
    [Tags]    sysimp     9.0
    set test variable     ${ID_TYPE}   Invalid
    When user edits state with random data by using invalid id
    Then expected return status code 404
