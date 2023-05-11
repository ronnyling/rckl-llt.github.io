*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/MessageType/MessageTypeAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/MessageType/MessageTypeListPage.py

*** Test Cases ***
1-To create and delete new message type
    [Documentation]    To ensure user is able to delete created Message Type
    [Tags]      hqadm     9.2
    Given user navigates to menu Configuration | Reference Data | Message Type
    When user creates message type with random data
    Then message type created successfully with message 'Record created successfully'
    When user selects message type to delete
    Then message type deleted successfully with message 'Record deleted'

