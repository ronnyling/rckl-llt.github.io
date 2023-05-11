*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/ActivitySetup/Checklist/ChecklistListPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/ActivitySetup/Checklist/ChecklistAddPage.py


*** Test Cases ***
1 - User able to delete merchandising checklist
    [Documentation]  To validate user able to delete merchandising checklist
    [Tags]    hqadm    9.2
    Given user navigates to menu Merchandising | Activity Setup | Checklist
    When user creates merchandising checklist using random data
    Then merchandising checklist created successfully with message 'Record created successfully'
    When user selects merchandising checklist to delete
    Then merchandising checklist deleted successfully with message 'Record deleted'