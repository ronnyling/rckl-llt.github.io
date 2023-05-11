*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Incentives/IncentiveProgram/IncentiveProgramPut.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Incentives/IncentiveProgram/IncentiveProgramPost.py

*** Test Cases ***
1 - Able to put to incentive program
    [Documentation]    To put to incentive program
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user posts for incentive program
    And expected return status code 200
    When user puts to save incentive program
    Then expected return status code 200
