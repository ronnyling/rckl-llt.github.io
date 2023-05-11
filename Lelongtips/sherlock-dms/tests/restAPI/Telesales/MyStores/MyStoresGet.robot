*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/Telesales/MyStores/MyStoresGet.py


*** Test Cases ***
1 - Able to GET all HQ Telesales route plan customer assignment
    [Documentation]    Able to retrieve all HQ Telesales route plan customer assignment
    [Tags]    hqtelesales    9.3
    Given user retrieves token access as ${user_role}
    When user retrieves all route plan customer assignment for HQTELE10
    Then expected return status code 200

2 - Able to GET all Dist Telesales route plan customer assignment
    [Documentation]    Able to retrieve all Dist Telesales route plan customer assignment
    [Tags]    telesales    9.3
    Given user retrieves token access as ${user_role}
    When user retrieves all route plan customer assignment for DSTELE10
    Then expected return status code 200

3 - Able to GET HQ Telesales my store customer list
    [Documentation]    Able to retrieve HQ Telesales my store customer list
    [Tags]    hqtelesales    9.3
    Given user retrieves token access as ${user_role}
    When user retrieves my stores customer list
    Then expected return status code 200

4 - Able to GET Dist Telesales my store customer list
    [Documentation]    Able to retrieve Dist Telesales my store customer list
    [Tags]    telesales    9.3
    Given user retrieves token access as ${user_role}
    When user retrieves my stores customer list
    Then expected return status code 200

5 - Able to GET HQ Telesales my store customer contact
    [Documentation]    Able to retrieve HQ Telesales my store customer contact
    [Tags]    hqtelesales    9.3
    Given user retrieves token access as ${user_role}
    When user retrieves contact for CT0000001549
    Then expected return status code 200

6 - Able to GET Dist Telesales my store customer contact
    [Documentation]    Able to retrieve Dist Telesales my store customer contact
    [Tags]    telesales    9.3
    Given user retrieves token access as ${user_role}
    When user retrieves contact for CT0000001549
    Then expected return status code 200