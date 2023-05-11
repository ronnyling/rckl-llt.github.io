*** Settings ***
Resource            ${EXECDIR}${/}tests/web/common.robot
Resource            ${EXECDIR}${/}tests/restAPI/common.robot
Library             ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/State/StatePost.py
Library             ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/State/StateDelete.py
Library             ${EXECDIR}${/}resources/web/Config/ReferenceData/Locality/LocalityListPage.py
Library             ${EXECDIR}${/}resources/web/Config/ReferenceData/Locality/LocalityAddPage.py
Library             ${EXECDIR}${/}resources/web/Config/ReferenceData/Locality/LocalityEditPage.py
Test Setup  run keywords     user creates state as prerequisite
...    AND    user open browser and logins using user role ${user_role}

Test Teardown  run keywords    user deletes created state as teardown
...    AND       user logouts and closes browser
*** Test Cases ***
1 - Able to Edit an existing locality with fixed data
    [Documentation]    Able to Edit a locality with fixed data
    [Tags]     sysimp    9.0   10
    ${locality_edit_details} =    create dictionary
    ...    city_cd=Per
    ...    city_name=Perak
    Given user navigates to menu Configuration | Reference Data | Locality
    When user creates locality with random data
    Then locality created successfully with message 'Record created successfully'
    When user selects locality to edit
    And user edits locality with fixed data
    Then locality edited successfully with message 'Record updated successfully'
    When user selects locality to delete
    Then locality deleted successfully with message 'Record deleted'


2 - Able to Edit an existing state with random data
    [Documentation]    Able to Edit a locality with random data
    [Tags]     sysimp    9.0
    Given user navigates to menu Configuration | Reference Data | Locality
    When user creates locality with random data
    Then locality created successfully with message 'Record created successfully'
    When user selects locality to edit
    And user edits locality with random data
    Then locality edited successfully with message 'Record updated successfully'
    When user selects locality to delete
    Then locatility deleted successfully with message 'Record deleted'

3. - Unable to edit locality data with invalid data
    [Documentation]    Unable to Edit a locality with invalid data
    [Tags]    sysimp   9.0
    ${locality_edit_details}=   create dictionary
    ...    city_cd=A#%#@
    ...    city_name=AA%@&@EFG8
    Given user navigates to menu Configuration | Reference Data | Locality
    When user creates locality with random data
    Then locality created successfully with message 'Record created successfully'
    When user selects locality to edit
    And user edits locality with fixed data
    Then return validation message 'Value does not match required pattern'
    And user clicks cancel
    When user selects locality to delete
    Then locality deleted successfully with message 'Record deleted'
