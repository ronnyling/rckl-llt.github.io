*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/GamificationGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/GamificationPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py

Test Setup     run keywords
...    Given user retrieves token access as ${user_role}
...    user retrieves details of application_setup

Test Teardown    run keywords
...   user revert to previous setting
...   expected return status code 200

#not applicable to hqadm
*** Test Cases ***
1 - Able to update gamification using fixed data
    [Documentation]    Able to update gamification using fixed data
    [Tags]     sysimp   9.1
    Given user retrieves token access as ${user_role}
    ${AppSetupDetails}=    create dictionary
    ...    GEO_LEVEL_FOR_LEADERBOARD=Sales Office
    set test variable   &{AppSetupDetails}
    When user updates app setup gamification details using fixed data
    Then expected return status code 200
