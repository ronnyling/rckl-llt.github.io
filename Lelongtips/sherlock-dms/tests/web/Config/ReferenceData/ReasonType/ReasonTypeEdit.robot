*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/ReasonType/ReasonTypeAllPage.py

*** Test Cases ***
1-To create and edit new reason type with all the mandatory fields
    [Documentation]    To ensure user is able to add and edit the details in reason type code and description
    [Tags]      hqadm     9.2
    [Teardown]  run keywords
    ...    user selects reason to delete
    ...    AND     reason deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    ${ReasonDetails}=    create dictionary
    ...    REASON_CD=DELREJ001
    ...    REASON_DESC=Delivery Reject 001
    set test variable     &{ReasonDetails}
    ${NewReasonDetails}=    create dictionary
    ...    REASON_DESC=W00
    set test variable     &{NewReasonDetails}
    Given user navigates to menu Configuration | Reference Data | Reason Type
    When user creates fixed reason for Delivery Rejection
    And reason created successfully with message 'Record created successfully'
    Then user searches for reason Delivery Rejection
    When user selects reason to edit
    And user updates fixed reason for Delivery Rejection
    Then reason updated successfully with message 'Record updated successfully'

2-Able to cancel the reason type after selecting the edit option
    [Documentation]    To ensure user is able to cancel the reason type after selecting the edit option
    [Tags]      hqadm     9.2
    [Teardown]  run keywords
    ...    user selects reason to delete
    ...    AND     reason deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
       ${ReasonDetails}=    create dictionary
    ...    REASON_CD=DELREJ002
    ...    REASON_DESC=Delivery Reject 002
    set test variable     &{ReasonDetails}
    Given user navigates to menu Configuration | Reference Data | Reason Type
    When user creates fixed reason for Delivery Rejection
    Then reason created successfully with message 'Record created successfully'
    When user selects reason to edit
    Then user clicks on Cancel button












