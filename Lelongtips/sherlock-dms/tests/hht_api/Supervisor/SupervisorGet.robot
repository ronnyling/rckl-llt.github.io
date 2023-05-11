*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/Supervisor/SupervisorGet.py


*** Test Cases ***
1 - Able to retrieve route compliance exception
    [Documentation]    Able to retrieve route compliance exception
    [Tags]    hqsupervisor    9.2    NRSZUANQ-48682
    Given user retrieves token access as ${user_role}
    When user retrieves route compliance exception
    Then expected return status code 200

2 - Able to retrieve salesman no sales outlet
    [Documentation]    Able to retrieve salesman no sales outlet
    [Tags]    hqsupervisor    9.2    NRSZUANQ-48793
    Given user retrieves token access as ${user_role}
    When user retrieves salesman no sales outlet
    Then expected return status code 200

3 - Able to retrieve salesman stale value
    [Documentation]    Able to retrieve salesman stale value
    [Tags]    hqsupervisor    9.2    NRSZUANQ-48630
    Given user retrieves token access as ${user_role}
    When user retrieves salesman stale value
    Then expected return status code 200

4 - Able to retrieve salesman average unique sku
    [Documentation]    Able to retrieve salesman average unique sku
    [Tags]    hqsupervisor    9.2    NRSZUANQ-48794
    Given user retrieves token access as ${user_role}
    When user retrieves salesman average unique sku
    Then expected return status code 200

5 - Able to retrieve team weekly performance
    [Documentation]    Able to retrieve team weekly performance
    [Tags]    hqsupervisor    9.2    NRSZUANQ-48678
    Given user retrieves token access as ${user_role}
    When user retrieves team weekly performance
    Then expected return status code 200