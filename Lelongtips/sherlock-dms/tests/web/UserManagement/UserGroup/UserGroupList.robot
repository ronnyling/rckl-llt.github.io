*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/UserManagement/UserGroup/UserGroupAddPage.py
Library         ${EXECDIR}${/}resources/web/UserManagement/UserGroup/UserGroupListPage.py

Test Teardown   run keywords
...    user performs delete on user group
...    AND     user group deleted successfully with message 'Record deleted'
...    AND     user logouts and closes browser

*** Test Cases ***
1-Able to filter existing user group using code
   [Documentation]    To test that user is able to filter user group by code
   [Tags]  sysimp    9.2
    ${group_details}=    create dictionary
    ...    code=FLCD100
    ...    name=USER FILTER
    ...    desc=User to test filter function
    ...    role=HQ Admin
    set test variable     &{group_details}
    Given user navigates to menu User Management | User Group
    When user creates user group using fixed data
    Then user group created successfully with message 'Record created successfully'
    When user filters created user group in listing page by code
    Then record display in listing successfully

2-Able to filter existing user group using description
   [Documentation]    To test that user is able to filter user group by description
   [Tags]  sysimp    9.2
    ${group_details}=    create dictionary
    ...    code=FLDS100
    ...    name=USER FILTER
    ...    desc=User to test filter function
    ...    role=HQ Admin
    set test variable     &{group_details}
    Given user navigates to menu User Management | User Group
    And user creates user group using fixed data
    And user group created successfully with message 'Record created successfully'
    When user filters created user group in listing page by description
    Then record display in listing successfully

3-Able to search existing user group using code
   [Documentation]    To test that user is able to search user group using code
   [Tags]    sysimp    9.2
   ${group_details}=    create dictionary
    ...    code=SRCD100
    ...    name=USER SEARCH
    ...    desc=User to test search function
    ...    role=HQ Admin
    set test variable     &{group_details}
    Given user navigates to menu User Management | User Group
    And user creates user group using fixed data
    And user group created successfully with message 'Record created successfully'
    When user searches created user group in listing page by code
    Then record display in listing successfully

4-Able to search existing user group using description
   [Documentation]    To test that user is able to search user group based on description
   [Tags]    sysimp    9.2
   ${group_details}=    create dictionary
    ...    code=SRDS100
    ...    name=USER SEARCH
    ...    desc=User to test search function
    ...    role=HQ Admin
    set test variable     &{group_details}
    Given user navigates to menu User Management | User Group
    And user creates user group using fixed data
    And user group created successfully with message 'Record created successfully'
    When user searches created user group in listing page by name
    Then record display in listing successfully

5-Able to view created user group
   [Documentation]    To test that user is able view created user group
   [Tags]  sysimp    9.2
   ${group_details}=    create dictionary
    ...    code=VWUSER100
    ...    name=USER View
    ...    desc=User to test view function
    ...    role=HQ Admin
    set test variable     &{group_details}
    Given user navigates to menu User Management | User Group
    And user creates user group using fixed data
    And user group created successfully with message 'Record created successfully'
    When user performs edit on user group
    Then user is able to navigate to EDIT | User Group