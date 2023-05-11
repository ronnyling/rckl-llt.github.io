*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/DimensionUnit/DimensionUnitAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/DimensionUnit/DimensionUnitListPage.py

*** Test Cases ***
1-Able to Create new Dimension Unit with RandomData
    [Documentation]    To test creating new Dimension Unit with Random Data
    [Tags]    sysimp    9.2
    Given user navigates to menu Configuration | Reference Data | Dimension Unit
    When user creates dimension unit with random data
    Then dimension unit created successfully with message 'Record created successfully'
    When created dimension unit is verified successfully and selects to delete
    Then dimension unit deleted successfully with message 'Record deleted'

2-To ensure all the error message is showing correctly and standardize
    [Documentation]    Ensure the error message for the empty fields should shows correctly
    [Tags]    sysimp    9.2
    Given user navigates to menu Configuration | Reference Data | Dimension Unit
    When user clicks on Add button
    And user clicks on Save button
    Then validate error message on empty fields



3-Not able to create new Dimension Unit with existing Dimension Unit and Dimension Unit Description
    [Documentation]    To test not able to create new dimension unit using existing dimension unit and dimension unit description
    [Tags]    sysimp    9.2
    Given user navigates to menu Configuration | Reference Data | Dimension Unit
    When user creates dimension unit with random data
    Then dimension unit created successfully with message 'Record created successfully'
    When user creates dimension unit with existing data
    Then expect pop up message: The record already exists
    When user clicks on Cancel button
    And created dimension unit is verified successfully and selects to delete
    Then dimension unit deleted successfully with message 'Record deleted'


