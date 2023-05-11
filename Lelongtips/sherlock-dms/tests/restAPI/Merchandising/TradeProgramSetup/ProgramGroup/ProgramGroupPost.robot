*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/ProgramGroup/ProgramGroupPost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/TradeProgramSetup/ProgramGroup/ProgramGroupDelete.py


*** Test Cases ***
1 - Able to post to program group API
    [Documentation]  This test is to post to program group API
    [Tags]      hqadm
    [Teardown]  run keywords
    ...     user deletes program group details
    Given user retrieves token access as hqadm
    When user post to program group
    Then expected return status code 201
