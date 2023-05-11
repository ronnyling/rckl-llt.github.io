*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/Gamification/Badges/BadgesAddPage.py
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/Gamification/Badges/BadgesListPage.py

#not applicable to distadm, but applicable for hqadm, sysimp
*** Test Cases ***
1 - Able to delete badge record without assignment in reward setup
    [Documentation]    Able to delete badge record without assignment in reward setup
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27186
    When user navigates to menu Performance Management | Gamification | Badges
    Then user can create badge setup using random data
    And badge setup created successfully with message 'Record created successfully'
    When user selects badge setup to delete
    Then badge setup deleted successfully with message 'Record deleted'