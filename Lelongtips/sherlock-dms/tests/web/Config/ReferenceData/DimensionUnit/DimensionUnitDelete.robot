*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/DimensionUnit/DimensionUnitAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/DimensionUnit/DimensionUnitListPage.py

*** Test Cases ***
1-Able to delete one Dimension Unit
    [Documentation]    To test deleting new Dimension Unit
    [Tags]   sysimp    9.2
    Given user navigates to menu Configuration | Reference Data | Dimension Unit
    When user creates dimension unit with random data
    Then dimension unit created successfully with message 'Record created successfully'
    When created dimension unit is verified successfully and selects to delete
    Then dimension unit deleted successfully with message 'Record deleted'