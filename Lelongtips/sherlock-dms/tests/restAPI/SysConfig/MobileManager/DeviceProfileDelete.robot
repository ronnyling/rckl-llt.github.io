*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/MobileManager/DeviceProfilePost.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/MobileManager/DeviceProfileGet.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/MobileManager/DeviceProfileDelete.py


*** Test Cases ***
1 - Able to delete Device Profile
    [Documentation]    Able to delete device Profile
    ...    This is not applicable to distadm, hqadm
    [Tags]     sysimp    9.1
    Given user retrieves token access as ${user_role}
    When user creates device profile using random data
    Then expected return status code 201
    When user retrieves fixed device profile
    Then expected return status code 200
    When user delete created device profile
    Then expected return status code 200
