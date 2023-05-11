*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Rewards/RewardsPost.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Rewards/RewardsGet.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Rewards/RewardsDelete.py

*** Test Cases ***
1 - Validate user scope for reward setup via GET request
    [Documentation]    Validate user scope on GET reward setup
    [Tags]    hqadm    sysimp    distadm    9.1    NRSZUANQ-27111
    [Template]    Validate user scope on get reward setup
    ${user_role}          200

2 - Able to read created reward setup
    [Documentation]    Able to read created reward setup
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27115
    [Setup]    user retrieves token access as ${user_role}
    [Teardown]    User deletes created reward setup
    When user creates reward setup using random data
    Then expected return status code 201
    When user retrieves created reward setup
    Then expected return status code 200