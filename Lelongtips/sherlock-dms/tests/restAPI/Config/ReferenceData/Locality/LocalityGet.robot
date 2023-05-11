*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Locality/LocalityPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Locality/LocalityGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Locality/LocalityDelete.py

*** Test Cases ***
1 - Able to retrieve all Localities data
    [Documentation]  To retrieve all localities record via API
    [Tags]    sysimp     9.0
    Given user retrieves token access as ${user_role}
    When user creates locality with RandomData
    Then expected return status code 201
    When user gets all localities data
    Then expected return status code 200
    When user deletes locality with created data
    Then expected return status code 200

2 - Able to retrieve Locality by using id
    [Documentation]  To retrieve locality by passing in ID via API
    [Tags]    sysimp     9.0
    Given user retrieves token access as ${user_role}
    When user creates locality with RandomData
    Then expected return status code 201
    When user gets locality by using id
    Then expected return status code 200
    When user deletes locality with created data
    Then expected return status code 200
