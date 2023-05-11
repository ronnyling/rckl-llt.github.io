*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/UserManagement/User/UserAddPage.py
Library         ${EXECDIR}${/}resources/web/UserManagement/User/UserListPage.py

*** Test Cases ***
1 - Able to delete created user
    [Documentation]    Able to delete created user
    [Tags]     hqadm    distadm    9.2
    ${user_details}=    create dictionary
    ...    login=DELUS100
    ...    name=Test UserDel
    ...    email=userdel@user.com
    ...    phone=0123004000
    set test variable     &{user_details}
    Given user navigates to menu User Management | User
    When user creates user using fixed data
    Then user created successfully with message 'Record created successfully'
    When user clicks on Cancel button
    And user performs delete on user
    Then user updated successfully with message 'Record deleted successfully'