*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/ReasonType/ReasonTypeAllPage.py
*** Test Cases ***
1-To create and delete new reason type with all the mandatory fields
    [Documentation]    To ensure user is able to add the details in reason type code and description and deletes the careted Reason Type
    [Tags]      hqadm     9.2    NRSZUANQ-5913
    ${ReasonDetails}=    create dictionary
    ...    REASON_CD=DLR001
    ...    REASON_DESC=Reject Cause A
    set test variable     &{ReasonDetails}
    Given user navigates to menu Configuration | Reference Data | Reason Type
    When user creates fixed reason for Delivery Rejection
    Then reason created successfully with message 'Record created successfully'
    When user searches for reason Delivery Rejection
    And user selects reason to delete
    Then reason deleted successfully with message 'Record deleted successfully'

2-To create new reason type with mandatory fields and search through filter and deletes
    [Documentation]    To ensure user is able to create new reason type with mandatory fields and search through filter and deletes
    [Tags]      hqadm     9.2
    ${ReasonDetails}=    create dictionary
    ...    REASON_CD=DLR002
    ...    REASON_DESC=Reject Cause B
    set test variable     &{ReasonDetails}
    Given user navigates to menu Configuration | Reference Data | Reason Type
    When user creates fixed reason for Delivery Rejection
    Then reason created successfully with message 'Record created successfully'
    When user searches created reason using code field
    And user selects reason to delete
    Then reason deleted successfully with message 'Record deleted successfully'