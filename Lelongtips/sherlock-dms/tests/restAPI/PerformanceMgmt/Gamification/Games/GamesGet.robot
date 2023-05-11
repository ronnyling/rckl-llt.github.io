*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Games/GamesPost.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Games/GamesGet.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Games/GamesDelete.py

*** Test Cases ***
1 - Able to retrieve all team assignment in game setup
    [Documentation]    Able to retrieve all team assignment in game setup
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28534
    Given user retrieves token access as ${user_role}
    When user retrieves team assignment in all game setup
    Then expected return status code 200

2 - Able to retrieve team assignment in created game setup
    [Documentation]    Able to retrieve team assignment in created game setup
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28534
    Given user retrieves token access as ${user_role}
    When user creates game setup using random data
    Then expected return status code 201
    When user retrieves team assignment in created game setup
    Then expected return status code 204
    When user deletes created game setup
    Then expected return status code 200

3 - Validate user scope for team assignment retrieval in game setup via GET request
    [Documentation]    Validate user scope on GET request for team assignment retrieval in game setup
    ...    This is not applicable to distadm, hqadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28537
    [Template]    Validate user scope on get game setup team
    ${user_role}          200