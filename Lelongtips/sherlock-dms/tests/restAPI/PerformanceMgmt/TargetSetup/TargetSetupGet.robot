*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/TargetSetup/TargetSetupGet.py
*** Test Cases ***
1 - Able to get all target setup upload history
    [Documentation]  To test get all upload history for target setup
    [Tags]    distadm    hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves upload history
    Then expected return status code 200
