*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/MessageType/MessageTypeAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/MessageType/MessageTypeListPage.py


*** Test Cases ***

1 - Able to Create Message Type using random data
    [Documentation]    Able to create message type using random data
    [Tags]     hqadm    9.2
    [Teardown]    run keywords
    ...    user selects message type to delete
    ...    AND     message type deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Reference Data | Message Type
    When user creates message type with random data
    Then message type created successfully with message 'Record created successfully'

2 - Unable to edit an existing message type with invalid data
    [Documentation]    Unable to edit a message type with invalid
    [Tags]     hqadm    9.2
    ${message_type_details}=    create dictionary
    ...    message_code=!@@#@#@!!!@~$%%#
    ...    message_desc=!@@#@#@!!!@@#@#@!!!@@#@#@!!
    set test variable     &{message_type_details}
    Given user navigates to menu Configuration | Reference Data | Message Type
    When user creates message type with invalid data
    Then validate error message on invalid fields