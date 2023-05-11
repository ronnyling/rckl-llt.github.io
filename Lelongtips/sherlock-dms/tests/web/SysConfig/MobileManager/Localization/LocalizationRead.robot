*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/SysConfig/MobileManager/Localization/LocalizationAllPage.py

*** Test Cases ***
1 - Able to retrieve all localization
    [Documentation]    Able to retrieve all localization
    [Tags]    sysimp    9.1    NRSZUANQ-28615
    When user navigates to menu System Configuration | Mobile Manager | Localization
    Then user retrieved all localization     # fixme: this is user retrieve or page display?
