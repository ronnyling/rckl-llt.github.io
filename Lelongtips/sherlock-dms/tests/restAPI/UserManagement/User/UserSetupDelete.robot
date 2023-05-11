*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/UserManagement/User/UserSetupPost.py
Library           ${EXECDIR}${/}resources/restAPI/UserManagement/User/UserSetupDelete.py

*** Test Cases ***

1 - Able to delete user setup using random data
    [Documentation]    Able to create user setup using random data
    [Tags]   sysimp    hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates user setup using random data
    Then expected return status code 201
    When user deletes created user setup
    Then expected return status code 200
