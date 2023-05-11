*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/UserManagement/UserGroup/UserGroupGet.py
Library           ${EXECDIR}${/}resources/restAPI/UserManagement/UserGroup/UserGroupPost.py
Library           ${EXECDIR}${/}resources/restAPI/UserManagement/UserGroup/UserGroupDelete.py

*** Test Cases ***
1 - Able to delete created user group using sysimp
    [Documentation]    Able to delete created user group using sys imp
    [Tags]     sysimp    9.2
    Given user retrieves token access as ${user_role}
    When user creates user group using random data
    Then expected return status code 201
    When user deletes created user group
    Then expected return status code 200

2 - Unable to delete user group using invalid login
    [Documentation]    Unable to delete user group using hqadm / distadm
    [Tags]     hqadm    distadm    9.2
    Given user retrieves token access as sysimp
    When user creates user group using random data
    Then expected return status code 201
    When user retrieves token access as ${user_role}
    And user deletes created user group
    Then expected return status code 403