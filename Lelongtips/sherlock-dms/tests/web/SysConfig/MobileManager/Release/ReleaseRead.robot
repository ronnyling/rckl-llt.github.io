*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/SysConfig/MobileManager/Release/ReleaseListPage.py

*** Test Cases ***
1 - Able to retrieve all release
    [Documentation]    Able to retrieve all release
    [Tags]    sysimp    9.1    NRSZUANQ-28615
    When user navigates to menu System Configuration | Mobile Manager | Release
    Then user retrieved all release     # fixme: this is user retrieve or page display?
