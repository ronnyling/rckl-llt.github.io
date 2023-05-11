*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Incentives/IncentivePayout/IncentivePayoutPost.py

*** Test Cases ***
1 - Able to post to incentive payout
    [Documentation]    To post to incentive payout
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user posts for incentive payout
    Then expected return either status code 200 or status code 204
