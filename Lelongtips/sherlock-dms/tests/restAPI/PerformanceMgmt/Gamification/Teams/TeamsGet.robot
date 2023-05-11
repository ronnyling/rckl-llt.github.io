*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Teams/TeamsPost.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Teams/TeamsGet.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Teams/TeamsDelete.py

*** Test Cases ***
1 - Able to retrieve created team setup
    [Documentation]    Able to retrieve created team setup
    ...    Distadm also can retrieve created team setup
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27090    NRSZUANQ-27089
    [Setup]    user retrieves token access as ${user_role}
    [Teardown]    user deletes created team setup
    When user creates team setup using random data
    Then expected return status code 201
    When user retrieves created team setup
    Then expected return status code 200

2 - Able to retrieve all team setup
    [Documentation]    Able to retrieve all team setup
    [Tags]    hqadm    distadm    sysimp    9.1    NRSZUANQ-27090    NRSZUANQ-27089
    [Setup]    user retrieves token access as ${user_role}
    When user retrieves all team setup
    Then expected return status code 200