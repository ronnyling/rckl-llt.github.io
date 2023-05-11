*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/ProgramGroup/ProgramGroupPut.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/ProgramGroup/ProgramGroupPost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/ProgramGroup/ProgramGroupDelete.py

*** Test Cases ***
1-Able to retrieve all trade program via API
    [Documentation]  This test is to retrieve all program group via API
    [Tags]      hqadm
    [Teardown]  run keywords
    ...     user deletes program group details
    Given user retrieves token access as hqadm
    When user post to program group
    Then expected return status code 201
    When user puts to program group details
    Then expected return status code 200
