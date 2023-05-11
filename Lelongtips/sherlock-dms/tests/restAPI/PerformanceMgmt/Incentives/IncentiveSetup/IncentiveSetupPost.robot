*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Incentives/IncentiveSetup/IncentiveSetupPost.py

*** Test Cases ***
1 - Able to post to incentive setup
    [Documentation]    To post to incentive setup
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user posts for incentive setup
    And user posts to incentive setup details slabs
    Then expected return status code 200
