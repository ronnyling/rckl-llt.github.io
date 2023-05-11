*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/UserManagement/UserGroup/UserGroupAddPage.py
Library         ${EXECDIR}${/}resources/web/UserManagement/UserGroup/UserGroupListPage.py
Library         ${EXECDIR}${/}resources/web/UserManagement/UserGroup/UserGroupEditPage.py
*** Test Cases ***
1 - Able to update user group with random data
    [Documentation]    Able to update user group with random data
    [Tags]     sysimp    9.2
    [Teardown]    run keywords
    ...    user perform delete on user group
    ...    AND     user group deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    ${group_details}=    create dictionary
    ...    code=EDITUS800
    ...    name=EDIT USER 800
    ...    desc=This is user to edit
    ...    role=HQ Admin
    set test variable     &{group_details}
    Given user navigates to menu User Management | User Group
    When user creates user group using fixed data
    Then user group created successfully with message 'Record created successfully'
    When user performs edit on user group
    And user updates user group using random data
    Then user group created successfully with message 'Record updated successfully'