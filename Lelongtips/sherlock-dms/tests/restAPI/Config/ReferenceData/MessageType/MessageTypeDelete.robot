*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/MessageType/MessageTypePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/MessageType/MessageTypeDelete.py


*** Test Cases ***
1 - Able to create Message Type with random data
    [Documentation]  To create Message Type with random data via api
    [Tags]    sysimp     9.1
    Given user retrieves token access as ${user_role}
    When user creates Message Type with random data
    Then expected return status code 201
    When user deletes message type with created data
    Then expected return status code 200