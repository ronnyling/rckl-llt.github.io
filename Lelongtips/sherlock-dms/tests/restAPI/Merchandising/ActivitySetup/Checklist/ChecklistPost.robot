*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/ActivitySetup/Checklist/ChecklistPost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/ActivitySetup/Checklist/ChecklistDelete.py

*** Test Cases ***
1 - Able to POST merchandising checklist with random data
    [Documentation]  Able to add merchandising checklist with random data
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user adds merchandising checklist using random data
    Then expected return status code 201
    When user deletes merchandising checklist
    Then expected return status code 200

2 - Able to POST merchandising checklist with fixed data
    [Documentation]  Able to add merchandising checklist with fixed data
    [Tags]    hqadm    9.2
    ${checklist_details}=    create dictionary
    ...    CHECKLIST_DESC=ChecklistDesc
    ...    START_DATE=2026-06-02
    ...    END_DATE=2026-06-03
    ...    ACTIVITY_CODE=ActivityCode
    ...    ACTIVITY_DESC=ActivityDesc
    set test variable  &{checklist_details}
    Given user retrieves token access as hqadm
    When user adds merchandising checklist using fixed data
    Then expected return status code 201
    When user deletes merchandising checklist
    Then expected return status code 200
