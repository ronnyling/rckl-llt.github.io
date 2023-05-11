*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/UserManagement/UserGroup/UserGroupPost.py
Library           ${EXECDIR}${/}resources/restAPI/UserManagement/UserGroup/UserGroupDelete.py
Library           ${EXECDIR}${/}resources/restAPI/UserManagement/UserGroup/UserGroupPut.py
*** Test Cases ***
1 - Able to update user group using random data
    [Documentation]    Able to update user group with random data and return status code 201
    [Tags]     sysimp    9.2
    Given user retrieves token access as ${user_role}
    When user creates user group using random data
    Then expected return status code 201
    When user updates user group using random data
    Then expected return status code 200
    When user deletes created user group
    Then expected return status code 200

2 - Able to update user group using fixed data
    [Documentation]    Able to update user group with fixed data and return status code 201
    [Tags]     sysimp    9.2
    Given user retrieves token access as ${user_role}
    When user creates user group using random data
    Then expected return status code 201
    ${user_group_details}=    create dictionary
    ...    NAME=UG1000
    ...    DESCRIPTION=Fixed user group
    set test variable   &{user_group_details}
    When user updates user group using fixed data
    Then expected return status code 200
    When user deletes created user group
    Then expected return status code 200

3 - Unable to update user group using invalid login
    [Documentation]    Unable to update user group using hqadm / distadm
    [Tags]     hqadm    distadm    9.2
    Given user retrieves token access as sysimp
    When user creates user group using random data
    Then expected return status code 201
    When user retrieves token access as ${user_role}
    And user updates user group using random data
    Then expected return status code 403

