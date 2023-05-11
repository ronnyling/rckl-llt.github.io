*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/ActivitySetup/Checklist/ChecklistListPage.py

*** Test Cases ***
1 - Validate buttons on checklist listing page for HQ admin
    [Documentation]  To validate user able to view add and delete buttons on checklist listing page
    [Tags]    hqadm    9.2
    Given user navigates to menu Merchandising | Activity Setup | Checklist
    Then user validates buttons for hq admin

2 - Validate buttons on checklist listing page for distributor login
    [Documentation]  To validate user unable to see add and delete buttons on checklist listing page
    [Tags]    distadm    9.2
    Given user navigates to menu Merchandising | Activity Setup | Checklist
    Then user validates buttons for distributor
