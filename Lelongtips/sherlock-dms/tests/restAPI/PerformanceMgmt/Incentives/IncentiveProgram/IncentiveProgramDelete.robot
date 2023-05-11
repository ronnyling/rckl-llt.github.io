*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Incentives/IncentiveProgram/IncentiveProgramPost.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Incentives/IncentiveProgram/IncentiveProgramDelete.py

*** Test Cases ***
1 - Able to delete incentive program
    [Documentation]    To delete incentive program
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user posts for incentive program
    When user deletes incentive programs
    Then expected return status code 200
