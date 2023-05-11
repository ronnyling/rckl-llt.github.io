*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/UserManagement/UserGroup/UserGroupGet.py
Library           ${EXECDIR}${/}resources/restAPI/UserManagement/UserGroup/UserGroupPost.py
Library           ${EXECDIR}${/}resources/restAPI/UserManagement/UserGroup/UserGroupDelete.py

*** Test Cases ***
1 - Able to create user group using random data
    [Documentation]    Able to create user group with random data and return status code 201
    [Tags]     sysimp    9.2
    Given user retrieves token access as ${user_role}
    When user creates user group using random data
    Then expected return status code 201
    When user deletes created user group
    Then expected return status code 200

2 - Able to create user group using fixed data
    [Documentation]    Able to create user group with fixed data and return status code 201
    [Tags]     sysimp    9.2
    ${user_group_details}=    create dictionary
    ...    GROUP_CD=USGRP100
    ...    NAME=User Group 100
    ...    DESCRIPTION=Fixed user group
    set test variable   &{user_group_details}
    Given user retrieves token access as ${user_role}
    When user creates user group using fixed data
    Then expected return status code 201
    When user deletes created user group
    Then expected return status code 200

3 - Unable to create user group with duplicate data
    [Documentation]    Able to create user group with fixed data and return status code 201
    [Tags]     sysimp    9.2
    ${user_group_details}=    create dictionary
    ...    GROUP_CD=DUPUSER100
    ...    NAME=Duplicate Test
    ...    DESCRIPTION=Test User Group
    set test variable   &{user_group_details}
    Given user retrieves token access as ${user_role}
    When user creates user group using fixed data
    Then expected return status code 201
    When user creates user group using fixed data
    Then expected return status code 409
    When user deletes created user group
    Then expected return status code 200

4 - Unable to create user group using invalid login
    [Documentation]    Unable to create new user group using hqadm / distadm
    [Tags]     hqadm    distadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates user group using random data
    Then expected return status code 403