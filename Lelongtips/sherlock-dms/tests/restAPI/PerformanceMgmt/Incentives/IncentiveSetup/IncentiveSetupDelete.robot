*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Incentives/IncentiveSetup/IncentiveSetupPost.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Incentives/IncentiveSetup/IncentiveSetupDelete.py

*** Test Cases ***
1 - Able to delete incentive setup
    [Documentation]    To delete incentive setup
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user posts for incentive setup
    And user posts to incentive setup details slabs
    Then expected return status code 200
    When user deletes incentive setup details
    Then expected return status code 200
