*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/VisionStore/ScoreCardResult/ScoreCardResultGet.py

*** Test Cases ***
1 - Able to retrieve score card result listing
    [Documentation]    To retrieve score card result listing
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieve score card result listing
    Then expected return status code 200

2 - Able to retrieve score card result details
    [Documentation]    To retrieve score card result details
    [Tags]     distadm
    Given user retrieves token access as ${user_role}
    When user retrieve score card result details
    Then expected return status code 200
