*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/MessageType/MessageTypeAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/MessageType/MessageTypeListPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/MessageType/MessageTypeEditPage.py

*** Test Cases ***
1-Able to search created message type
    [Documentation]    To test user is able to search created message type
    [Tags]     hqadm     9.2
    [Teardown]    run keywords
    ...    user selects message type to delete
    ...    AND     message type deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Reference Data | Message Type
    When user creates message type with random data
    Then message type created successfully with message 'Record created successfully'
    When user searches created message type
    Then record display in listing successfully

2-Able to filter created message type
    [Documentation]       To test user is able to filter created message type
    [Tags]      hqadm     9.2
    [Teardown]    run keywords
    ...    user selects message type to delete
    ...    AND     message type deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Reference Data | Message Type
    When user creates message type with random data
    Then message type created successfully with message 'Record created successfully'
    When user filters created message type
    Then record display in listing successfully