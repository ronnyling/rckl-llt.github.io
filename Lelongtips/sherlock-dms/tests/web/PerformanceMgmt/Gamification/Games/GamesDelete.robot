*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/Gamification/Games/GamesAddPage.py
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/Gamification/Games/GamesListPage.py

*** Test Cases ***
1 - Unable to delete game setup once it is started
    [Documentation]    Unable to delete game setup once it is started
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28939
    When user navigates to menu Performance Management | Gamification | Games
    ${GameSetupDescription}=    create dictionary
    ...    EndDate=yesterday
    set test variable    ${GameSetupDescription}
    And user filters game setup using fixed data
    Then user deletes created game setup
    And message prompted successfully 'Started game is not allow to delete'