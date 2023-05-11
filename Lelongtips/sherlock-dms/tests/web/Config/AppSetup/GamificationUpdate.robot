*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/AppSetup/GamificationEditPage.py
Library         ${EXECDIR}${/}resources/components/Tab.py

#not applicable to hqadm
*** Test Cases ***
1 - Able to update gamification using random data
    [Documentation]    Able to update gamification using random data
    [Tags]    sysimp    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Gamification tab
    Then user updates gamification using random data
    And gamification updated successfully with message 'Record updated successfully'

2 - Able to update gamification using fixed data
    [Documentation]    Able to update gamification using fixed data
    [Tags]    sysimp    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Gamification tab
    ${GamificationDetails}=    create dictionary
    ...    Geo_Level_for_Leaderboard=Sales Office
    set test variable    &{GamificationDetails}
    Then user updates gamification using fixed data
    And gamification updated successfully with message 'Record updated successfully'
