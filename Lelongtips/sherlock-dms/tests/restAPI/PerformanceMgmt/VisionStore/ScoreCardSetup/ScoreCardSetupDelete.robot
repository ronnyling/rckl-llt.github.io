*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/VisionStore/ScoreCardSetup/ScoreCardSetupPost.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/VisionStore/ScoreCardSetup/ScoreCardSetupDelete.py

*** Test Cases ***
1 - Able to create vision store with KPI Description
    [Documentation]    Able to create vision store with KPI Description
    ...    This is not applicable to distadm
    [Tags]    hqadm    hquser561    9.1.1    NRSZUANQ-39192    NRSZUANQ-39201
    Given user retrieves token access as hqadm
    When user creates vs score card using random data
    Then expected return status code 201
    When user deletes created vs score card
    Then expected return status code 200
