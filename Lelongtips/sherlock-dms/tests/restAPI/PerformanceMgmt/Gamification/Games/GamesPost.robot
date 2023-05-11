*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Games/GamesPost.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Games/GamesGet.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Gamification/Games/GamesDelete.py

*** Test Cases ***
1 - Able to create team assignment in game setup
    [Documentation]    Able to create team assignment in game setup
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28536
    Given user retrieves token access as ${user_role}
    When user creates game setup using random data
    Then expected return status code 201
    When user retrieves team assignment in created game setup
    Then expected return status code 204
    When user creates team assignment in game setup using random data
    Then expected return status code 200
    When user deletes created game setup
    Then expected return status code 200

2 - Validate user scope for team assignment creation in game setup via POST request
    [Documentation]    Validate user scope on POST request for team assignment creation in game setup
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28537
    ...    This is not applicable to distadm
    [Template]    Validate user scope on post game setup team
    ${user_role}          200