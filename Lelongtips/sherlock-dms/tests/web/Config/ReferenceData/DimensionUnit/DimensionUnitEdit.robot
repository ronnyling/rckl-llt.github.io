*** Settings ***
Resource            ${EXECDIR}${/}tests/web/common.robot
Library             ${EXECDIR}${/}resources/web/Config/ReferenceData/DimensionUnit/DimensionUnitAddPage.py
Library             ${EXECDIR}${/}resources/web/Config/ReferenceData/DimensionUnit/DimensionUnitListPage.py
Library             ${EXECDIR}${/}resources/web/Config/ReferenceData/DimensionUnit/DimensionUnitEditPage.py


*** Test Cases ***
1-Able to view dimension unit details
    [Documentation]    To test that user able to view dimension unit details
    [Tags]   sysimp    9.2
    Given user navigates to menu Configuration | Reference Data | Dimension Unit
    When user creates dimension unit with random data
    Then dimension unit created successfully with message 'Record created successfully'
    When created dimension unit is verified successfully and selects to edit
    Then dimension unit viewed successfully
    When created dimension unit is verified successfully and selects to delete
    Then dimension unit deleted successfully with message 'Record deleted'

2-Able to update dimension unit with all valid input
    [Documentation]    To test updating new dimension unit with all valid input
    [Tags]   sysimp    9.2
    Given user navigates to menu Configuration | Reference Data | Dimension Unit
    When user creates dimension unit with random data
    Then dimension unit created successfully with message 'Record created successfully'
    When created dimension unit is verified successfully and selects to edit
    And user edits dimension unit with random data
    Then dimension unit updated successfully with message 'Record updated successfully'
    When created dimension unit is verified successfully and selects to delete
    Then dimension unit deleted successfully with message 'Record deleted'