*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/TaskList/TaskListGet.py

*** Test Cases ***
1 - Able to retrieve all task
    [Documentation]    Able to retrieve all task
    [Tags]    sysimp    hqadm   9.2
    Given user retrieves token access as ${user_role}
    When user retrieves all task
    Then expected return status code 200

