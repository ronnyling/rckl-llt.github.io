*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/Gamification/Badges/BadgesAddPage.py
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/Gamification/Badges/BadgesListPage.py
Library         ${EXECDIR}${/}resources/components/Pagination.py

#not applicable to distadm, but applicable for hqadm, sysimp
*** Test Cases ***
1 - Unable to update badge code
    [Documentation]    Unable to update badge code
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27120
    When user navigates to menu Performance Management | Gamification | Badges
    Then user can create badge setup using random data
    And badge setup created successfully with message 'Record created successfully'
    When user selects badge setup to edit
    Then expect badge code is disabled
    When user selects badge setup to delete
    Then badge setup deleted successfully with message 'Record deleted'

2 - Able to update badge description
    [Documentation]    Able to update badge description
    [Tags]    hqadm    sysimp    9.1
    When user navigates to menu Performance Management | Gamification | Badges
    Then user can create badge setup using random data
    And badge setup created successfully with message 'Record created successfully'
    When user selects badge setup to edit
    And user able to update badge description
    Then badge setup updated successfully with message 'Record updated successfully'
    When user selects badge setup to delete
    Then badge setup deleted successfully with message 'Record deleted'
