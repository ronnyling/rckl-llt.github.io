*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/SysConfig/MobileManager/Instruction/InstructionListPage.py

*** Test Cases ***
1 - Able to retrieve all instruction
    [Documentation]    Able to retrieve all instruction
    [Tags]    sysimp    9.1    NRSZUANQ-28615
    When user navigates to menu System Configuration | Mobile Manager | Instruction
    Then user retrieved all instruction     # fixme: this is user retrieve or page display?
