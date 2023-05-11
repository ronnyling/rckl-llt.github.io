*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/State/StateAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/State/StateListPage.py

*** Test Cases ***
1 - Able to Create State using fixed data
    [Tags]   sysimp    9.0 
    ${state_details}=   create dictionary
    ...    state_cd=ABCDFAY
    ...    state_name=ABCFG8
    set test variable    &state_details
    Given user navigates to menu Configuration | Reference Data | State
    When user creates state with fixed data
    Then state created successfully with message 'Record created successfully'
    When user selects state to delete
    Then state deleted successfully with message 'Record deleted'

2 - Able to Create State using random data
    [Tags]  sysimp    9.0
    Given user navigates to menu Configuration | Reference Data | State
    When user creates state with random data
    Then state created successfully with message 'Record created successfully'
    When user selects state to delete
    Then state deleted successfully with message 'Record deleted'

3 - Unable to Create State with invalid data
    [Tags]    sysimp    9.0
     ${state_details}=   create dictionary
    ...    state_cd=&$&(@@
    ...    state_name=*&^%&(@%
    set test variable    &state_details
    Given user navigates to menu Configuration | Reference Data | State
    When user creates state with fixed data
    Then unable to create and confirms pop up message 'Invalid payload'