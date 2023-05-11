*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/MessageType/MessageTypePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/MessageType/MessageTypeGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/MessageType/MessageTypeDelete.py

*** Test Cases ***
1 - Able to retrieve all Message Type data
    [Documentation]  To retrieve all Message Type via API
    [Tags]    sysimp     9.0
    Given user retrieves token access as ${user_role}
    When user creates Message Type with random data
    Then expected return status code 201
    When user gets all message type data
    Then expected return status code 200
    When user deletes message type with created data
    Then expected return status code 200

2 - Able to retrieve Message Type by using id
    [Documentation]  To retrieve Message Type by ID via API
    [Tags]    sysimp     9.0
    Given user retrieves token access as ${user_role}
    When user creates Message Type with random data
    Then expected return status code 201
    When user gets message type by using id
    Then expected return status code 200
    When user deletes message type with created data
    Then expected return status code 200