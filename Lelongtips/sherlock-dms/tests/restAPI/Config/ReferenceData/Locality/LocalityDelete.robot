*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Locality/LocalityPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Locality/LocalityDelete.py

*** Test Cases ***
1 - Able to delete Locality with created data
    [Documentation]  To delete locality by passing in id via API
    [Tags]    sysimp     9.0
    Given user retrieves token access as ${user_role}
    When user creates locality with RandomData
    Then expected return status code 201
    When user deletes locality with created data
    Then expected return status code 200
