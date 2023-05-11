*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Incentives/IncentiveSetup/IncentiveSetupGet.py

*** Test Cases ***
1 - Able to retrieve incentive setup listing
    [Documentation]    To retrieve incentive setup listing
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves incentive setup listing
    Then expected return status code 200

2 - Able to retrieve incentive setup details
    [Documentation]    To retrieve incentive setup details
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves incentive setup details
    And user retrieves incentive setup details slabs
    Then expected return status code 200
