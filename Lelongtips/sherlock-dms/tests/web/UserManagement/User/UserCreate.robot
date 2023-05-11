*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/UserManagement/User/UserAddPage.py
Library         ${EXECDIR}${/}resources/web/UserManagement/User/UserListPage.py

*** Test Cases ***
1 - Able to create user with fixed data
    [Documentation]    Able to user with fixed data
    [Tags]     hqadm    distadm    9.2
    [Teardown]    run keywords
    ...    user clicks on Cancel button
    ...    AND     user performs delete on user
    ...    AND     user deleted successfully with message 'Record deleted successfully'
    ...    AND     user logouts and closes browser
    ${user_details}=    create dictionary
    ...    login=USER1234
    ...    name=USER 1234
    ...    email=user1234@user.com
    ...    phone=0123004000
    set test variable     &{user_details}
    Given user navigates to menu User Management | User
    When user creates user using fixed data
    Then user created successfully with message 'Record created successfully'

2 - Able to create user with random data
    [Documentation]    Able to user with fixed data
    [Tags]     hqadm    distadm    9.2
    [Teardown]    run keywords
    ...    user clicks on Cancel button
    ...    AND     user performs delete on user
    ...    AND     user deleted successfully with message 'Record deleted successfully'
    ...    AND     user logouts and closes browser
    Given user navigates to menu User Management | User
    When user creates user using random data
    Then user created successfully with message 'Record created successfully'