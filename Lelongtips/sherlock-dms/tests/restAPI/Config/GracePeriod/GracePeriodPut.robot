*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/GracePeriod/GracePeriodPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/GracePeriod/GracePeriodPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/GracePeriod/GracePeriodDelete.py

*** Test Cases ***
1 - Able to update created grace period with fixed data
    [Documentation]    Able to update created grace period with fixed data
    [Tags]     hqadm    9.2
    ${period_details}=    create dictionary
    ...    GRACE_PERIOD=${15}
    ...    START_DT=2023-01-01
    ...    END_DT=2023-12-31
    Given user retrieves token access as ${user_role}
    When user creates grace period using random data
    Then expected return status code 200
    When user updates grace period using fixed data
    Then expected return status code 200
    When user deletes created grace period
    Then expected return status code 200

2 - Able to update created grace period with random data
    [Documentation]    Able to update created grace period with random data
    [Tags]     hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates grace period using random data
    Then expected return status code 200
    When user updates grace period using random data
    Then expected return status code 200
    When user deletes created grace period
    Then expected return status code 200

