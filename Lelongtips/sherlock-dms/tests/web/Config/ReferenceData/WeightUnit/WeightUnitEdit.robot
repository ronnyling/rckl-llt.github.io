*** Settings ***
Resource            ${EXECDIR}${/}tests/web/common.robot
Library             ${EXECDIR}${/}resources/web/Config/ReferenceData/WeightUnit/WeightUnitAddPage.py
Library             ${EXECDIR}${/}resources/web/Config/ReferenceData/WeightUnit/WeightUnitListPage.py
Library             ${EXECDIR}${/}resources/web/Config/ReferenceData/WeightUnit/WeightUnitEditPage.py


*** Test Cases ***
1-Able to view weight unit details
    [Documentation]    To test that user able to view weight unit details
    [Tags]   sysimp    9.2
    Given user navigates to menu Configuration | Reference Data | Weight Unit
    When user creates weight unit with random data
    Then weight unit created successfully with message 'Record created successfully'
    When created weight unit is verified successfully and selects to edit
    Then weight unit viewed successfully
    When created weight unit is verified successfully and selects to delete
    Then weight unit deleted successfully with message 'Record deleted'

2-Able to update weight unit with all valid input
    [Documentation]    To test updating new weight unit with all valid input
    [Tags]   sysimp    9.2
    Given user navigates to menu Configuration | Reference Data | Weight Unit
    When user creates weight unit with random data
    Then weight unit created successfully with message 'Record created successfully'
    When created weight unit is verified successfully and selects to edit
    And user edits weight unit with random data
    Then weight unit updated successfully with message 'Record updated successfully'
    When created weight unit is verified successfully and selects to delete
    Then weight unit deleted successfully with message 'Record deleted'