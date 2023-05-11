*** Settings ***
Resource            ${EXECDIR}${/}tests/web/common.robot
Library             ${EXECDIR}${/}resources/web/Config/ReferenceData/WeightUnit/WeightUnitAddPage.py
Library             ${EXECDIR}${/}resources/web/Config/ReferenceData/WeightUnit/WeightUnitListPage.py


*** Test Cases ***
1-Able to filter Weight Unit with valid input
    [Documentation]    To test filtering Weight Unit with valid data
    [Tags]   sysimp    9.2
    Given user navigates to menu Configuration | Reference Data | Weight Unit
    When user creates weight unit with random data
    Then weight unit created successfully with message 'Record created successfully'
    When user filters created weight unit
    Then record display in listing successfully
    When created weight unit is verified successfully and selects to delete
    Then weight unit deleted successfully with message 'Record deleted'