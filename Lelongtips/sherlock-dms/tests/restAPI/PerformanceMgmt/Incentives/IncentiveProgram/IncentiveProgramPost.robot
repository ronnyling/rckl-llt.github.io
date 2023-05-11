*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Incentives/IncentiveProgram/IncentiveProgramPost.py

*** Test Cases ***
1 - Able to post to incentive setup
    [Documentation]    To post to incentive program
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user posts for incentive program
    Then expected return status code 200
