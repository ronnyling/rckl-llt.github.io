*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/ActivitySetup/Audit/AuditGet.py


*** Test Cases ***
1 - Able to GET merchandising audit
    [Documentation]  Able to retrieve all merchandising audit setup
    [Tags]    hqadm    distadm    9.2
    Given user retrieves token access as hqadm
    When user retrieves all audit setup
    Then expected return status code 200

2 - Able to GET merchandising audit by id
    [Documentation]  Able to retrieve merchandising audit setup by id
    [Tags]    hqadm    distadm    9.2
    Given user retrieves token access as hqadm
    When user retrieves all audit setup
    Then expected return status code 200
    When user retrieves audit setup by id
    Then expected return status code 200