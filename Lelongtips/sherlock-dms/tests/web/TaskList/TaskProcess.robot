*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/TaskList/TaskListPage.py

*** Test Cases ***
1 - Validate user able to claim, process, cancel and release workflow task
    [Documentation]  Validate user able to claim, process, cancel and release workflow task
    [Tags]    hqadm    9.2
    Given user navigates to menu Dashboard | Task List
    Then user claims workflow task
    And user processes workflow task
    And user cancels workflow task process
    And user releases workflow task
