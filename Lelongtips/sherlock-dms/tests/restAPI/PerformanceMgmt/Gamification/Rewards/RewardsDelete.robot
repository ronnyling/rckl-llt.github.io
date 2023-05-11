*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Rewards/RewardsPost.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Rewards/RewardsDelete.py

*** Test Cases ***
1 - Validate user scope for reward setup via DELETE request
    [Documentation]    Validate user scope on DELETE reward setup
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27111
    [Template]    Validate user scope on delete reward setup
    ${user_role}

2 - Able to delete created reward setup
    [Documentation]    Able to delete created reward setup
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27115
    [Teardown]    User deletes created reward setup
    user retrieves token access as ${user_role}
    user creates reward setup using random data
    expected return status code 201