*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/ReasonType/ReasonTypeAllPage.py

*** Test Cases ***
1-To create new reason type with mandatory fields and search through filter option after creation
    [Documentation]    To ensure user is able to create new reason type with mandatory fields and search through filter option after creation
    [Tags]     hqadm     9.2
    [Teardown]  run keywords
    ...    user selects reason to delete
    ...    AND     reason deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    ${ReasonDetails}=    create dictionary
    ...    REASON_CD=STK10101
    ...    REASON_DESC=STOCK OUT RS101
    set test variable     &{ReasonDetails}
    Given user navigates to menu Configuration | Reference Data | Reason Type
    When user creates fixed reason for Stock Out
    Then reason created successfully with message 'Record created successfully'
    When user searches created reason using both field

2-To create new reason type with mandatory fields and search only with reason code in filter option
    [Documentation]    To ensure user is able to create new reason type with mandatory fields and search only with reason code in filter option
    [Tags]      hqadm     9.2
    [Teardown]  run keywords
    ...    user selects reason to delete
    ...    AND     reason deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    ${ReasonDetails}=    create dictionary
    ...    REASON_CD=MDTD009
    ...    REASON_DESC=Mandatory desc here
    set test variable     &{ReasonDetails}
    Given user navigates to menu Configuration | Reference Data | Reason Type
    When user creates random reason for Stock Out
    Then reason created successfully with message 'Record created successfully'
    When user searches created reason using code field

3-To create new reason type with mandatory fields and resets Filter value without searching
    [Documentation]    To ensure user is able to create new reason type with mandatory fields and resets Filter values without searching
    [Tags]      hqadm     9.2
    Given user navigates to menu Configuration | Reference Data | Reason Type
    When user creates random reason for Stock Out
    And reason created successfully with message 'Record created successfully'
    Then user searches created reason and resets the search field

4-To create new reason type with mandatory fields and search only with reason desc in filter option
    [Documentation]    To ensure user is able to create new reason type with mandatory fields and search only with reason desc in filter option
    [Tags]      hqadm     9.2
    [Teardown]  run keywords
    ...    user selects reason to delete
    ...    AND     reason deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    ${ReasonDetails}=    create dictionary
    ...    REASON_CD=ERTS001
    ...    REASON_DESC=ER REASONDESC
    set test variable     &{ReasonDetails}
    Given user navigates to menu Configuration | Reference Data | Reason Type
    When user creates fixed reason for Stock Out
    Then reason created successfully with message 'Record created successfully'
    When user searches created reason using desc field