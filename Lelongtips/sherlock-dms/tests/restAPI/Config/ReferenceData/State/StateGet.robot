*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/State/StatePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/State/StateGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/State/StateDelete.py

*** Test Cases ***
1 - Able to retrieve all State data
    [Documentation]  To retrieve all state record via API
    [Tags]    sysimp     9.0
    Given user retrieves token access as ${user_role}
    When user creates state with RandomData
    Then expected return status code 201
    When user gets all states data
    Then expected return status code 200
    When user deletes state with created data
    Then expected return status code 200

2 - Able to retrieve State by using id
    [Documentation]  To retrieve state by passing in ID via API
    [Tags]    sysimp     9.0
    Given user retrieves token access as ${user_role}
    When user creates state with RandomData
    Then expected return status code 201
    When user gets state by using id
    Then expected return status code 200
    When user deletes state with created data
    Then expected return status code 200
