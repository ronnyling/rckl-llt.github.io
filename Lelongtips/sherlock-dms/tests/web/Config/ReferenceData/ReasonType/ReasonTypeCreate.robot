*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/ReasonType/ReasonTypeAllPage.py

*** Test Cases ***
1 - Able to Create Reason Type using given data
    [Documentation]    Able to create reason type using given data
    [Tags]     hquser    hqadm    9.0
    [Teardown]  run keywords
    ...    user selects reason to delete
    ...    AND     reason deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    ${ReasonDetails}=    create dictionary
    ...    REASON_CD=TestA11
    ...    REASON_DESC=Test Auto 1
    set test variable     &{ReasonDetails}
    Given user navigates to menu Configuration | Reference Data | Reason Type
    When user creates given reason for Return - Bad Stock
    Then reason created successfully with message 'Record created successfully'

2 - Able to Create Reason Type using random data
    [Documentation]    Able to create reason type using random data
    [Tags]     hquser    hqadm    9.0    9.1   NRSZUANQ-29973    test
    [Teardown]  run keywords
    ...    user selects reason to delete
    ...    AND     reason deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Reference Data | Reason Type
    When user creates random reason for Stock Out
    Then reason created successfully with message 'Record created successfully'

3 - Unable to create Reason Type with invalid inputs
    [Documentation]    Unable to create reason type using invalid data
    [Tags]     hquser    hqadm    9.0
    ${ReasonDetails}=    create dictionary
    ...    REASON_CD=#$#%#%#
    ...    REASON_DESC=%$%$%^%$
    set test variable     &{ReasonDetails}
    Given user navigates to menu Configuration | Reference Data | Reason Type
    When user creates given reason for Return to Supplier
    Then unable to create and confirms pop up message 'only accept alphabet and number'

4-To validate the Reason Type fields with values exceeding maximum characters
    [Documentation]    To ensure user is able to validate the Reason Type fields with values exceeding maximum characters
    [Tags]     hqadm    9.2
    ${ReasonDetails}=    create dictionary
    ...    REASON_CD=ABCDEFGHI1234567890J123456789
    ...    REASON_DESC=abcdefghij123451234512345klmno12345pqrst12345uvwxy12345
    set test variable     &{ReasonDetails}
    Given user navigates to menu Configuration | Reference Data | Reason Type
    When user creates maximum reason for Return - Bad Stock
    Then validate data is limited to set length

5- Unable to create with reason type only with reason code field and verifies the disabled save button
    [Documentation]      To ensure user is unable to create with reason type only with reason code field and verifies the disabled save button
    [Tags]    hqadm    9.2
    ${ReasonDetails}=    create dictionary
    ...    REASON_CD=TESTCD21
    set test variable     &{ReasonDetails}
    Given user navigates to menu Configuration | Reference Data | Reason Type
    When user creates code reason for Return - Bad Stock
    Then user validates that the save button is disabled

6-Unable to create Reason Type with invalid inputs in Reason Code and Reason Desc
    [Documentation]    To ensure user Unable to add Reason Type with empty value and space
    [Tags]   hqadm    9.2    NRSZUANQ-9628
    ${ReasonDetails}=    create dictionary
    ...    REASON_CD=${Empty}
    ...    REASON_DESC=${Empty}
    set test variable     &{ReasonDetails}
    Given user navigates to menu Configuration | Reference Data | Reason Type
    And user creates code reason for Return - Bad Stock
    When user validates that the save button is disabled

7-Unable to create Reason Type with invalid inputs in Reason Code and Reason Desc
    [Documentation]    To ensure user Unable to add Reason Type with space
    [Tags]   hqadm    9.2    NRSZUANQ-9628
    ${ReasonDetails}=    create dictionary
    ...    REASON_CD=${Space}
    ...    REASON_DESC=${Space}
    set test variable     &{ReasonDetails}
    Given user navigates to menu Configuration | Reference Data | Reason Type
    When user creates fixed reason for Return - Bad Stock
    Then expect pop up message: Invalid payload: REASON_CD only accept alphabet and number

8-Able to perform on add button for reason type and able to cancel without entering value
    [Documentation]    To ensure user able to perform on add button and performs on cancel to go back to the main tab
    [Tags]   hqadm    9.2
    Given user navigates to menu Configuration | Reference Data | Reason Type
    When user adds new reason
    Then user clicks on Cancel button
