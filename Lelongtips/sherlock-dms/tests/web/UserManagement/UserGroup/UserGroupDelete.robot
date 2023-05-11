*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/UserManagement/UserGroup/UserGroupAddPage.py
Library         ${EXECDIR}${/}resources/web/UserManagement/UserGroup/UserGroupListPage.py
*** Test Cases ***

1 - Able to delete created user group
    [Documentation]    Able to delete created user group
    [Tags]     sysimp    9.2
    ${group_details}=    create dictionary
    ...    code=USDL100
    ...    name=USER DELETE
    ...    desc=User to test delete function
    ...    role=HQ Admin
    set test variable     &{group_details}
    Given user navigates to menu User Management | User Group
    When user creates user group using fixed data
    Then user group created successfully with message 'Record created successfully'
    When user performs delete on user group
    Then user group deleted successfully with message 'Record deleted'

2 - Validate delete button is not visible for hqadm and distadm login
    [Documentation]    Validate delete button is not visible for hqadm / distadm login
    [Tags]     hqadm    9.2
    Given user navigates to menu User Management | User Group
    Then validate delete button is not visible

