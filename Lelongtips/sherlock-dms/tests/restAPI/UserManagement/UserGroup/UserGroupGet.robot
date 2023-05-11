*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/UserManagement/UserGroup/UserGroupGet.py

*** Test Cases ***
1 - Able to get all user group
    [Documentation]    To retrieve all user group
    [Tags]     sysimp    hqadm     distadm    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves all user group
    Then expected return status code 200

2 - Able to get user group based on random ID
    [Documentation]    To retrieve valid user group by ID
    [Tags]     sysimp    hqadm    distadm     9.2
    Given user retrieves token access as distadm
    When user retrieves all user group
    Then expected return status code 200
    When user retrieves user group by random id
    Then expected return status code 200
