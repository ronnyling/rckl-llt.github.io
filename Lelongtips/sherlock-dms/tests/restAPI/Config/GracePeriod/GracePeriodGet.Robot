*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/GracePeriod/GracePeriodPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/GracePeriod/GracePeriodDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/GracePeriod/GracePeriodGet.py

*** Test Cases ***
1 - Able to get all grace period
    [Documentation]    Able to retrieve all grace period and return 200
    [Tags]     hqadm    NRSZUANQ-45469
    Given user retrieves token access as ${user_role}
    When user retrieves all grace period
    Then expected return status code 200

2 - Able to get created grace period
    [Documentation]    Able to retrieve grace period by id and return 200
    [Tags]     hqadm    NRSZUANQ-45469
    Given user retrieves token access as ${user_role}
    When user creates grace period using random data
    Then expected return status code 200
    When user deletes created grace period
    Then expected return status code 200
