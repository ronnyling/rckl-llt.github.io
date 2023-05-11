*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/State/StateAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/State/StateListPage.py

*** Test Cases ***
1 - Able to Delete State with random data
    [Tags]    sysimp    9.0
    Given user navigates to menu Configuration | Reference Data | State
    When user creates state with random data
    Then state created successfully with message 'Record created successfully'
    When user selects state to delete
    Then state deleted successfully with message 'Record deleted'
