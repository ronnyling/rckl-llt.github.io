*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/MobileManager/DeviceProfilePost.py


*** Test Cases ***
1 - Able to create device profile using random data
    [Documentation]    Able to create module setup using random data
    ...    This is not applicable to distadm, hqadm
    [Tags]    sysimp    9.1
    Given user retrieves token access as ${user_role}
    When user creates device profile using random data
    Then expected return status code 201

2 - Able to create device profile using fixed data
    [Documentation]    Able to create module setup using fixed data
    ...    This is not applicable to distadm, hqadm
    [Tags]    sysimp    9.1
    Given user retrieves token access as ${user_role}
    ${DeviceProfileDetails}=    create dictionary
    ...    PROFILE_CODE=TestingFixedData
    set test variable    ${DeviceProfileDetails}
    When user creates device profile using fixed data
    Then expected return status code 201