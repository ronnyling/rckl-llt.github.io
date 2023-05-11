*** Settings ***
Resource            ${EXECDIR}${/}tests/web/common.robot
Library             ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Country/CountryPost.py
Library             ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Country/CountryDelete.py
Library             ${EXECDIR}${/}resources/web/Config/ReferenceData/State/StateListPage.py
Library             ${EXECDIR}${/}resources/web/Config/ReferenceData/State/StateAddPage.py
Library             ${EXECDIR}${/}resources/web/Config/ReferenceData/State/StateEditPage.py


Test Setup  run keywords     user creates country as prerequisite
...    AND       user open browser and logins using user role ${user_role}
Test Teardown  run keywords  user deletes created country as teardown
...    AND       user logouts and closes browser

*** Test Cases ***
1 - Able to Edit an existing state with fixed data
    [Documentation]    Able to Edit a state
    [Tags]     sysimp    9.0
    ${state_edit_details} =    create dictionary
    ...    state_cd=Per
    ...    state_name=Perak
    Given user navigates to menu Configuration | Reference Data | State
    When user creates state with random data
    Then state created successfully with message 'Record created successfully'
    When user selects state to edit
    And user edits state with fixed data
    Then state edited successfully with message 'Record updated successfully'
    When user selects state to delete
    Then state deleted successfully with message 'Record deleted'

2 - Able to Edit an existing state with random data
    [Documentation]    Able to Edit a state
    [Tags]     sysimp    9.0
    Given user navigates to menu Configuration | Reference Data | State
    When user creates state with random data
    Then state created successfully with message 'Record created successfully'
    When user selects state to edit
    And user edits state with random data
    Then state edited successfully with message 'Record updated successfully'
    When user selects state to delete
    Then state deleted successfully with message 'Record deleted'

3. - Unable to edit state data with invalid data
    [Tags]    sysimp    9.0
    ${state_edit_details}=   create dictionary
    ...    state_cd=A#%#@
    ...    state_name=AA%@&@EFG8
    Given user navigates to menu Configuration | Reference Data | State
    When user creates state with random data
    Then state created successfully with message 'Record created successfully'
    When user selects state to edit
    And user edits state with fixed data
    Then country unable to edit and confirms pop up message 'Invalid payload'
    And user clicks cancel
    When user selects state to delete
    Then state deleted successfully with message 'Record deleted'
