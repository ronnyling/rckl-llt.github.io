*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/MobileManager/DeviceProfilePost.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/MobileManager/DeviceProfileGet.py

*** Test Cases ***
1 - Able to retrieve all device profile
    [Documentation]    Able to retrieve all device profile
    ...    This is not applicable to distadm, hqadm
    [Tags]    sysimp    9.0
    Given user retrieves token access as ${user_role}
    When user retrieves all device profile
    Then expected return status code 200

2 - Able to retrieve created device profile
    [Documentation]    Able to retrieve created device profile
    ...    This is not applicable to distadm, hqadm
    [Tags]    sysimp    9.0
    Given user retrieves token access as ${user_role}
    When user creates device profile using random data
    Then expected return status code 201
    When user retrieves created device profile
    Then expected return status code 200