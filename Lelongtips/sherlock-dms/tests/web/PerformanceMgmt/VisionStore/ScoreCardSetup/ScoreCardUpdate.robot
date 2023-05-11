*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/Gamification/Games/GamesAddPage.py
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/Gamification/Games/GamesListPage.py

*** Test Cases ***
1 - Unable to update start date for score card setup once it is started
    [Documentation]    Unable to update start date for score card setup once it is started
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28788
    When user navigates to menu Performance Management | Gamification | score cards
    ${scorecardSetupDescription}=    create dictionary
    ...    EndDate=yesterday
    set test variable    ${scorecardSetupDescription}
    And user filters score card setup using fixed data
    Then user verified start date for score card setup is disabled
