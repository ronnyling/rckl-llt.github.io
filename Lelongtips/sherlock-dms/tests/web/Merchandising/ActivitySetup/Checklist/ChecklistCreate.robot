*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/ActivitySetup/Checklist/ChecklistListPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/ActivitySetup/Checklist/ChecklistAddPage.py


*** Test Cases ***
1 - User able to create new checklist with random data
    [Documentation]  To validate user able to create new checklist with random data
    [Tags]    hqadm    9.2
    Given user navigates to menu Merchandising | Activity Setup | Checklist
    When user creates merchandising checklist using random data
    Then merchandising checklist created successfully with message 'Record created successfully'
    When user selects merchandising checklist to delete
    Then merchandising checklist deleted successfully with message 'Record deleted'

2 - User able to create new checklist with fixed data
    [Documentation]  To validate user able to create new checklist with fixed data
    [Tags]    hqadm    9.2
    ${checklist_details}=    create dictionary
    ...    CHECKLIST_DESC=CLTEST001
    ...    START_DATE=2026-06-02
    ...    END_DATE=2026-06-02
    ...    ACTIVITY_CODE=ACTTEST001
    ...    ACTIVITY_DESC=Activity Test 001
    ...    STATUS=Active
    set test variable     &{checklist_details}
    Given user navigates to menu Merchandising | Activity Setup | Checklist
    When user creates merchandising checklist using fixed data
    Then merchandising checklist created successfully with message 'Record created successfully'
    When user selects merchandising checklist to delete
    Then merchandising checklist deleted successfully with message 'Record deleted'
