*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/SysConfig/MobileManager/DeviceProfile/DeviceProfileListPage.py

*** Test Cases ***
1 - Able to retrieve all device profile
    [Documentation]    Able to retrieve all device profile
    [Tags]    sysimp    9.1    NRSZUANQ-28615
    When user navigates to menu System Configuration | Mobile Manager | Device Profile
    Then user retrieved all device profile    # fixme: this is user retrieve or page display?
