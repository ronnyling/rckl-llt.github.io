*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/Incentives/IncentiveProgram/IncentiveProgramGet.py

*** Test Cases ***
1 - Able to retrieve incentive program listing
    [Documentation]    To retrieve incentive program listing
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves incentive program listing
    Then expected return status code 200

2 - Able to retrieve incentive program details
    [Documentation]    To retrieve incentive program details
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieves incentive program details
    And user retrieves incentive program details assignments
    Then expected return status code 200
