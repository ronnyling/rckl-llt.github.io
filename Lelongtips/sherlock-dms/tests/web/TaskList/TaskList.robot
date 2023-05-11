*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/TaskList/TaskListPage.py

*** Test Cases ***
1 - Validate buttons on workflow tasks listing page for HQ admin and distributor
    [Documentation]  To validate user able to view search and filter buttons on workflow task listing page
    [Tags]    hqadm    distadm    9.2
    Given user navigates to menu Dashboard | Task List
    Then user validates buttons for workflow task listing page

