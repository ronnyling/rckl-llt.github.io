*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/UserManagement/User/UserAddPage.py
Library         ${EXECDIR}${/}resources/web/UserManagement/User/UserListPage.py

*** Test Cases ***
1 - Able to filter user with fixed data
    [Documentation]    Able to filter created user
    [Tags]     hqadm    distadm    9.2
    [Teardown]    run keywords
    ...    user performs delete on user
    ...    AND     user deleted successfully with message 'Record deleted successfully'
    ...    AND     user logouts and closes browser
    ${user_details}=    create dictionary
    ...    login=USER2020
    ...    name=USER 2022
    ...    email=user202@user.com
    ...    phone=0198007000
    set test variable     &{user_details}
    Given user navigates to menu User Management | User
    When user creates user using fixed data
    Then user created successfully with message 'Record created successfully'
    When user clicks on Cancel button
    And user filters created user in listing page
    Then record display in listing successfully

2 - Able to search user with fixed data
    [Documentation]    Able to search created user
    [Tags]     hqadm    distadm    9.2
    [Teardown]    run keywords
    ...    user performs delete on user
    ...    AND     user deleted successfully with message 'Record deleted successfully'
    ...    AND     user logouts and closes browser
    ${user_details}=    create dictionary
    ...    login=USER2023
    ...    name=USER 2023
    ...    email=user203@user.com
    ...    phone=0198007000
    set test variable     &{user_details}
    Given user navigates to menu User Management | User
    When user creates user using fixed data
    Then user created successfully with message 'Record created successfully'
    When user clicks on Cancel button
    And user searches created user in listing page
    Then record display in listing successfully