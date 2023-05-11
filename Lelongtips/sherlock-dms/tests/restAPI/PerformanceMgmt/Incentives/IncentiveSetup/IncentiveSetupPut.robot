*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Incentives/IncentiveSetup/IncentiveSetupPut.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Incentives/IncentiveSetup/IncentiveSetupPost.py

*** Test Cases ***
1 - Able to put to incentive setup
    [Documentation]    To put to incentive setup
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user posts for incentive setup
    And expected return status code 200
    When user puts to save incentive setup
    Then expected return status code 200
    When user puts to confirm incentive setup
    Then expected return status code 200
