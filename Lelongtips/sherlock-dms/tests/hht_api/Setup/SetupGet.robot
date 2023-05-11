*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/Setup/SetupGet.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py

Test Setup        user gets distributor by using code 'DistPotato01'

*** Test Cases ***
1 - Able to retrieves Step of call setup
    [Documentation]    Able to retrieves Step of call setup
    [Tags]    salesperson    Setup    9.1
    Given user retrieves token access as salesperson
    When user retrieves Step Of Call setup using salesperson
    Then expected return status code 403
#    And Step of Call data correctly downloaded

2 - Able to retrieves activity assignment setup
    [Documentation]    Able to retrieves activity assignment setup
    [Tags]    salesperson    Setup    9.1
    Given user retrieves token access as salesperson
    When user retrieves activity assignment using salesperson
    Then expected return status code 403

3 - Able to retrieves Merchandising Step of call
    [Documentation]    Able to retrieves Merchandising Step of call setup
    [Tags]    salesperson    Setup    9.1
    Given user retrieves token access as salesperson
    When user retrieves Merchandising Step of Call using salesperson
    Then expected return status code 403

4 - Able to retrieves aging term
    [Documentation]    Able to retrieves aging term setup
    [Tags]    salesperson    Setup    9.0
    Given user retrieves token access as salesperson
    When user retrieves aging term using salesperson
    Then expected return status code 200

5 - Able to retrieves setting invoice term
    [Documentation]    Able to retrieves setting invoice term
    [Tags]    salesperson    Setup    9.0
    Given user retrieves token access as salesperson
    When user retrieves setting invoice term using salesperson
    Then expected return status code 200

6 - Able to retrieves setting invoice term details
    [Documentation]    Able to retrieves setting invoice term details
    [Tags]    salesperson    Setup    9.0
    Given user retrieves token access as ${user_role}
    When user retrieves invoice term details
    Then expected return status code 200

7 - Able to retrieves bank setting
    [Documentation]    Able to retrieves bank setting
    [Tags]    salesperson    Setup    9.0
    Given user retrieves token access as salesperson
    When user retrieves bank setting using salesperson
    Then expected return status code 200

8 - Able to retrieves van setting
    [Documentation]    Able to retrieves van setting
    [Tags]    salesperson    Setup    9.0
    Given user retrieves token access as ${user_role}
    When user retrieves van setting
    Then expected return status code 200

9 - Able to retrieves warehouse setting
    [Documentation]    Able to retrieves warehouse setting
    [Tags]    salesperson    Setup    9.0
    Given user retrieves token access as salesperson
    When user retrieves warehouse setting using salesperson
    Then expected return status code 200

10 - Able to retrieves message setup
    [Documentation]    Able to retrieves message setup
    [Tags]    salesperson    Setup    9.0
    Given user retrieves token access as ${user_role}
    When user retrieves message setup
    Then expected return status code 200

11 - Able to retrieves message assignment
    [Documentation]    Able to retrieves message assignment
    [Tags]    salesperson    Setup    9.0
    Given user retrieves token access as ${user_role}
    When user retrieves message assignment
    Then expected return status code 200

12 - Able to retrieves application setup
    [Documentation]    Able to retrieves application setup
    [Tags]    salesperson     Setup    9.0
    Given user retrieves token access as ${user_role}
    When user retrieves application setup

13 - Able to retrieves application setup reference
    [Documentation]    Able to retrieves application setup reference
    [Tags]    salesperson    Setup    9.0      BUG:NRSZUANQ-52085
    Given user retrieves token access as ${user_role}
    When user retrieves application setup reference

14 - Able to retrieves application setup parameter
    [Documentation]    Able to retrieves application setup parameter
    [Tags]    salesperson    Setup    9.0
    Given user retrieves token access as ${user_role}
    When user retrieves application setup parameter

15 - Able to retrieves Step of call setup using HQ salesperson
    [Documentation]    Able to retrieves Step of call setup using HQ salesperson
    [Tags]    HQSalesperson    Setup    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Step Of Call setup using hqsalesperson
    Then expected return status code 200

16 - Able to retrieves Merchandising Step of call using HQ merchandiser
    [Documentation]    Able to retrieves Merchandising Step of call setup using HQ salesperson
    [Tags]    HQSalesperson    Setup    9.1
    Given user retrieves token access as hqmerchandiser
    When user retrieves Merchandising Step of Call using hqmerchandiser
    Then expected return status code 200

17 - Able to retrieves activity assignment setup using HQ salesperson
    [Documentation]    Able to retrieves activity assignment setup using HQ salesperson
    [Tags]    HQSalesperson    Setup    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves activity assignment using hqsalesperson
    Then expected return status code 200

18 - Able to retrieves promotion sequence using HQ salesperson
    [Documentation]    Able to retrieves promotion sequence using HQ salesperson
    [Tags]    HQSalesperson    Setup    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves promotion sequence using hqsalesperson
    Then expected return status code 200

19 - Able to retrieves aging term using HQ salesperson
    [Documentation]    Able to retrieves aging term setup using HQ salesperson
    [Tags]    HQSalesperson    Setup    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves aging term using hqsalesperson
    Then expected return status code 200

20 - Able to retrieves setting invoice term using HQ salesperson
    [Documentation]    Able to retrieves setting invoice term using HQ salesperson
    [Tags]    HQSalesperson    Setup    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves setting invoice term using hqsalesperson
    Then expected return status code 200

21 - Able to retrieves setting invoice term detail using HQ salesperson
    [Documentation]    Able to retrieves setting invoice term detail using HQ salesperson
    [Tags]    HQSalesperson    Setup    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves setting invoice term detail using hqsalesperson
    Then expected return status code 200

22 - Able to retrieves bank setting using HQ salesperson
    [Documentation]    Able to retrieves bank setting using HQ salesperson
    [Tags]    HQSalesperson    Setup    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves bank setting using hqsalesperson
    Then expected return status code 200

23 - Able to retrieves warehouse setting using HQ salesperson
    [Documentation]    Able to retrieves warehouse setting using HQ salesperson
    [Tags]    HQSalesperson    Setup    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves warehouse setting using hqsalesperson
    Then expected return status code 200

24 - Able to retrieves warehouse product stock using HQ salesperson
    [Documentation]    Able to retrieves warehouse product stock using HQ salesperson
    [Tags]    HQSalesperson    Setup    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves warehouse product stock using hqsalesperson
    Then expected return status code 200

25 - Able to retrieve Tenant Logo
    [Documentation]    Able to retrieves Tenant Logo
    [Tags]    salesperson    Setup    9.1
    Given user retrieves token access as salesperson
    When user retrieves tenant logo using salesperson
    Then expected return status code 403

26 - Unable to retrieve Tenant Logo
    [Documentation]    Unable to retrieves Tenant Logo
    [Tags]    sysimp    Setup    9.1
    Given user retrieves token access as sysimp
    When user retrieves tenant logo using sysimp
    Then expected return status code 403

27 - Unable to retrieve Warehouse
    [Documentation]    Unable to retrieve Tenant Logo
    [Tags]    sysimp    Setup    9.1
    Given user retrieves token access as sysimp
    When user retrieves warehouse setting using sysimp
    Then expected return status code 403

28 - Unable to retrieve Warehouse Product Stock
    [Documentation]    Unable to retrieve warehouse product stock
    [Tags]    sysimp    Setup    9.1
    Given user retrieves token access as sysimp
    When user retrieves warehouse product stock using sysimp
    Then expected return status code 403

29 - Able to retrieve Route Distributor Warehouse
    [Documentation]    Able to retrieve Route Distributor Warehouse
    [Tags]    HQSalesperson    Setup    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves route distributor warehouse using hqsalesperson
    Then expected return status code 200

30 - Unable to retrieve Route Distributor Warehouse
    [Documentation]    Unable to retrieve Route Distributor Warehouse
    [Tags]    sysimp    Setup    9.1
    Given user retrieves token access as sysimp
    When user retrieves route distributor warehouse using sysimp
    Then expected return status code 403