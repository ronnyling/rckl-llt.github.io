*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/ActivitySetup/Checklist/ChecklistListPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/ActivitySetup/Checklist/ChecklistAddPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/ActivitySetup/Checklist/ChecklistAssignmentPage.py


*** Test Cases ***
1 - User able to add assignment to merchandising checklist
    [Documentation]  To validate user able to add assignment to merchandising checklist
    [Tags]    hqadm    9.2
    Given user navigates to menu Merchandising | Activity Setup | Checklist
    When user creates merchandising checklist using random data
    Then merchandising checklist created successfully with message 'Record created successfully'
    When user selects merchandising checklist to edit
    And user adds Level:Country assignment to merchandising checklist
    Then merchandising checklist assigned successfully with message 'Record created successfully'
    When user selects merchandising checklist to delete
    Then merchandising checklist deleted successfully with message 'Record deleted'
