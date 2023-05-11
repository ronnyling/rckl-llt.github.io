*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/GracePeriod/GracePeriodPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/GracePeriod/GracePeriodDelete.py

*** Test Cases ***
1 - Able to create grace period for dist
    [Documentation]    Able to create grace period and return 201
    [Tags]     hqadm    NRSZUANQ-45469
    Given user retrieves token access as ${user_role}
    When user creates grace period using random data
    Then expected return status code 200
    When user deletes created grace period
    Then expected return status code 200
