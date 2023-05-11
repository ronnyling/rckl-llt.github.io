*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Rewards/RewardsPost.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Rewards/RewardsPut.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Rewards/RewardsDelete.py

*** Test Cases ***
1 - Validate user scope for reward setup via PUT request
    [Documentation]    Validate user scope on PUT reward setup
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27111
    [Template]    Validate user scope on put reward setup
    ${user_role}    200


2 - Able to update created reward setup using fixed data
    [Documentation]    Able to update created reward setup
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27115
    [Teardown]    User deletes created reward setup
    user retrieves token access as ${user_role}
    user creates reward setup using random data
    expected return status code 201
    ${RewardSetupDetails}=    create dictionary
    ...    REWARD_DESC=Reward_Desc
    set test variable    ${RewardSetupDetails}
    I update created reward setup using fixed data
    expected return status code 200

3 - Unable to update KPI Code once it's created
    [Documentation]    Unable to update KPI Code once it's created
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27123
    [Teardown]    User deletes created reward setup
    user retrieves token access as ${user_role}
    ${RewardSetupDetails}=    create dictionary
    ...    KPI_CD=LPC
    set test variable    ${RewardSetupDetails}
    user creates reward setup using given data
    expected return status code 201
    ${RewardSetupDetails}=    create dictionary
    ...    KPI_CD=MSL
    set test variable    ${RewardSetupDetails}
    I update created reward setup using fixed data
    expected return status code 400