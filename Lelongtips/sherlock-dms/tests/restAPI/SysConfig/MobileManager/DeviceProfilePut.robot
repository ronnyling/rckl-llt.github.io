*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/MobileManager/DeviceProfilePost.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/MobileManager/DeviceProfilePut.py


*** Test Cases ***
1 - Able to update Device Profile
    [Documentation]    Able to update Device Profile
    ...    This is not applicable to distadm, hqadm
    [Tags]   sysimp     9.1
    Given user retrieves token access as ${user_role}
    When user creates device profile using random data
    Then expected return status code 201
    When user updates created attribute assign to record
    Then expected return status code 200

