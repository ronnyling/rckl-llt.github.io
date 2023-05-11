*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/UserManagement/UserGroup/UserGroupAddPage.py
Library         ${EXECDIR}${/}resources/web/UserManagement/UserGroup/UserGroupListPage.py
*** Test Cases ***
1 - Able to create user group with fixed data
    [Documentation]    Able to user group with fixed data
    [Tags]     sysimp    9.2
    [Teardown]    run keywords
    ...    user performs delete on user group
    ...    AND     user group deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    ${group_details}=    create dictionary
    ...    code=MYUSER20
    ...    name=MY USER 20
    ...    desc=This is MY User Description
    ...    role=HQ Admin
    set test variable     &{group_details}
    Given user navigates to menu User Management | User Group
    When user creates user group using fixed data
    Then user group created successfully with message 'Record created successfully'

2 - Able to create user group with random data
    [Documentation]    Able to create user group with random data
    [Tags]     sysimp    9.2
    Given user navigates to menu User Management | User Group
    When user creates user group using random data
    Then user group created successfully with message 'Record created successfully'

3 - Validate Add button is not visible for hqadm and distadm login
    [Documentation]    Validate add button is not visible for hqadm / distadm login
    [Tags]     hqadm    9.2
    Given user navigates to menu User Management | User Group
    Then validate Add button is not visible

