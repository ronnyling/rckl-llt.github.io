*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/ProgramGroup/ProgramGroupGet.py

*** Test Cases ***
1-Able to retrieve all program groups via API
    [Documentation]  This test is to retrieve all program groups via API
    [Tags]      hqadm
    Given user retrieves token access as hqadm
    When user retrieves all program groups
    Then expected return status code 200

2-Able to retrieve all program group details via API
    [Documentation]  This test is to retrieve all program group details via API
    [Tags]      hqadm
    Given user retrieves token access as hqadm
    When user retrieves program group details
    Then expected return status code 200



