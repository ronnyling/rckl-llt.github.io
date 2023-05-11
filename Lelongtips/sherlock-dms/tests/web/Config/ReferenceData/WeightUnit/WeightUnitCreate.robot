*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/WeightUnit/WeightUnitAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/WeightUnit/WeightUnitListPage.py

*** Test Cases ***
1-Able to Create new Weight Unit with RandomData
    [Documentation]    To test creating new Weight Unit with Random Data
    [Tags]    sysimp    9.2
    Given user navigates to menu Configuration | Reference Data | Weight Unit
    When user creates weight unit with random data
    Then weight unit created successfully with message 'Record created successfully'
    When created weight unit is verified successfully and selects to delete
    Then weight unit deleted successfully with message 'Record deleted'

2-To ensure all the error message is showing correctly and standardize
    [Documentation]    Ensure the error message for the empty fields should shows correctly
    [Tags]    sysimp    9.2
    Given user navigates to menu Configuration | Reference Data | Weight Unit
    When user clicks on Add button
    And user clicks on Save button
    Then validate error message on empty fields



3-Not able to create new Weight Unit with existing Weight Unit and Weight Unit Description
    [Documentation]    To test not able to create new weight unit using existing weight unit and weight unit description
    [Tags]    sysimp    9.2
    Given user navigates to menu Configuration | Reference Data | Weight Unit
    When user creates weight unit with random data
    Then weight unit created successfully with message 'Record created successfully'
    When user creates weight unit with existing data
    Then expect pop up message: The record already exists
    When user clicks on Cancel button
    And created weight unit is verified successfully and selects to delete
    Then weight unit deleted successfully with message 'Record deleted'


