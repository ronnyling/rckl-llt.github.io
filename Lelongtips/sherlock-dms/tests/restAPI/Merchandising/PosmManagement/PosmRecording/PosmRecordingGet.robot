*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/PosmManagement/PosmRecording/PosmRecordingGet.py


*** Test Cases ***
1 - Able to retrieve all posm recording
    [Documentation]  Able to retrieve all posm recording
    [Tags]    distadm    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves posm recording
    Then expected return status code 200