*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/ExecutionResult/AuditResult/AuditResultGet.py


*** Test Cases ***
1 - Able to GET all audit result for Facing Audit
    [Documentation]  Able to retrieve all audit result for facing audit
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user retrieves all audit result for facing audit
    Then expected return status code 200

2 - Able to GET all audit result for Price Audit
    [Documentation]  Able to retrieve all audit result for price audit
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user retrieves all audit result for price audit
    Then expected return status code 200

3 - Able to GET all audit result for Distribution Check
    [Documentation]  Able to retrieve all audit result for distribution check
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user retrieves all audit result for distribution check
    Then expected return status code 200

4 - Able to GET all audit result for Promo Compliance
    [Documentation]  Able to retrieve all audit result for promo compliance
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user retrieves all audit result for promo compliance
    Then expected return status code 200

5 - Able to GET audit result for Facing Audit by id
    [Documentation]  Able to retrieve result for facing audit by id
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user retrieves all audit result for facing audit
    Then expected return status code 200
    When user retrieves audit result for facing audit by id
    Then expected return status code 200

6 - Able to GET audit result for Price Audit by id
    [Documentation]  Able to retrieve result for price audit by id
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user retrieves all audit result for price audit
    Then expected return status code 200
    When user retrieves audit result for price audit by id
    Then expected return status code 200

7 - Able to GET audit result for Distribution Check by id
    [Documentation]  Able to retrieve result for distribution check by id
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user retrieves all audit result for distribution check
    Then expected return status code 200
    When user retrieves audit result for distribution check by id
    Then expected return status code 200

8 - Able to GET audit result for Promo Compliance by id
    [Documentation]  Able to retrieve result for promo compliance by id
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user retrieves all audit result for promo compliance
    Then expected return status code 200
    When user retrieves audit result for promo compliance by id
    Then expected return status code 200

