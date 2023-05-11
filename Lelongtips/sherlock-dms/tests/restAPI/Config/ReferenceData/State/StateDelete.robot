*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/State/StatePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/State/StateDelete.py

*** Test Cases ***
1 - Able to delete State with created data
    [Documentation]  To delete state by passing in id via API
    [Tags]    sysimp     9.0
    Given user retrieves token access as ${user_role}
    When user creates state with RandomData
    Then expected return status code 201
    When user deletes state with created data
    Then expected return status code 200
