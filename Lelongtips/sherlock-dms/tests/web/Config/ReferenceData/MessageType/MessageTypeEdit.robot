*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/MessageType/MessageTypeAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/MessageType/MessageTypeListPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/MessageType/MessageTypeEditPage.py

*** Test Cases ***
1 - Able to edit an existing message type with random data
    [Documentation]    Able to edit a message type with random data
    [Tags]     hqadm    9.2
    [Teardown]    run keywords
    ...    user selects message type to delete
    ...    AND     message type deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Reference Data | Message Type
    When user creates message type with random data
    Then message type created successfully with message 'Record created successfully'
    When user selects message type to edit
    And user edits message type with random data
    Then message type edited successfully with message 'Record updated successfully'

2 - Unable to edit an existing message type with invalid data
    [Documentation]    Unable to edit a message type with invalid data
    [Tags]     hqadm    9.2
    ${new_message_type_details}=    create dictionary
    ...    message_desc=!@@#@#@!!
    set test variable     &{new_message_type_details}
    Given user navigates to menu Configuration | Reference Data | Message Type
    When user creates message type with random data
    Then message type created successfully with message 'Record created successfully'
    When user selects message type to edit
    And user edits message type with invalid data
    Then validate error message on invalid description

