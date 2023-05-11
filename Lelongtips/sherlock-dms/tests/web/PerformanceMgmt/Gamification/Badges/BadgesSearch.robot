*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/Gamification/Badges/BadgesAddPage.py
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/Gamification/Badges/BadgesListPage.py

#not applicable to distadm, but applicable for hqadm, sysimp
*** Test Cases ***
1 - Able to inline search created record in badge setup
    [Documentation]    Able to filter created record in badge setup
    [Tags]    hqadm    sysimp   9.1    NRSZUANQ-27117
    When user navigates to menu Performance Management | Gamification | Badges
    Then user can create badge setup using random data
    And badge setup created successfully with message 'Record created successfully'
    When user inline search created badge setup
    And user selects badge setup to delete
    Then badge setup deleted successfully with message 'Record deleted'
