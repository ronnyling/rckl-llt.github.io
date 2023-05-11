*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/ActivitySetup/Checklist/ChecklistPost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/ActivitySetup/Checklist/ChecklistPut.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/ActivitySetup/Checklist/ChecklistDelete.py

*** Test Cases ***
1 - Able to PUT merchandising checklist with random data
    [Documentation]  Able to update merchandising checklist with random data
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user adds merchandising checklist using random data
    Then expected return status code 201
    When user updates merchandising checklist using random data
    Then expected return status code 201
    When user deletes merchandising checklist
    Then expected return status code 200

2 - Able to PUT merchandising checklist with fixed data
    [Documentation]  Able to update merchandising checklist with fixed data
    [Tags]    hqadm    9.2
    ${checklist_details}=    create dictionary
    ...    CHECKLIST_DESC=ChecklistPutDesc
    ...    START_DATE=2026-02-06
    ...    END_DATE=2026-02-07
    ...    ACTIVITY_CODE=ActivityPutCode
    ...    ACTIVITY_DESC=ActivityPutDesc
    set test variable  &{checklist_details}
    Given user retrieves token access as hqadm
    When user adds merchandising checklist using random data
    Then expected return status code 201
    When user updates merchandising checklist using fixed data
    Then expected return status code 201
    When user deletes merchandising checklist
    Then expected return status code 200
