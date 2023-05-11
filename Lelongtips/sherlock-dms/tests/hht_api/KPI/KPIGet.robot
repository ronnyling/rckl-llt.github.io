*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/KPI/KPIGet.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py

Test Setup        user gets distributor by using code 'DistPotato01'

*** Test Cases ***
1 - Able to get Address Template using HQsalesperson
    [Documentation]    Able to retrieve Address Template using HQsalesperson
    [Tags]    hqsalesperson    KPI    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Address Template using hqsalesperson
    Then expected return status code 200

2 - Able to get Address Schema using HQsalesperson
    [Documentation]    Able to retrieve Address Schema using HQsalesperson
    [Tags]    hqsalesperson    KPI    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Address Schema using hqsalesperson
    Then expected return status code 200

3 - Able to get Address Reference using HQsalesperson
    [Documentation]    Able to retrieve Address Reference using HQsalesperson
    [Tags]    hqsalesperson    KPI    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Address Reference using hqsalesperson
    Then expected return status code 200

4 - Able to get Performance Header using HQsalesperson
    [Documentation]    Able to retrieve Performance Header using HQsalesperson
    [Tags]    hqsalesperson    KPI    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Performance Header using hqsalesperson
    Then expected return status code 200

5 - Able to get Performance Header Customer using HQsalesperson
    [Documentation]    Able to retrieve Performance Header Customer using HQsalesperson
    [Tags]    hqsalesperson    KPI    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Performance Header Customer using hqsalesperson
    Then expected return status code 200

6 - Able to get Performance Detail using HQsalesperson
    [Documentation]    Able to retrieve Performance Detail using HQsalesperson
    [Tags]    hqsalesperson    KPI    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Performance Detail using hqsalesperson
    Then expected return status code 200

7 - Able to get Performance Hierarchy using HQsalesperson
    [Documentation]    Able to retrieve Performance Hierarchy using HQsalesperson
    [Tags]    hqsalesperson    KPI    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Performance Hierarchy using hqsalesperson
    Then expected return status code 200

8 - Able to get Customer Sales History using HQsalesperson
    [Documentation]    Able to retrieve Customer Sales History using HQsalesperson
    [Tags]    hqsalesperson    KPI    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Customer Sales History using hqsalesperson
    Then expected return status code 200

9 - Able to get Customer Sales History Detail using HQsalesperson
    [Documentation]    Able to retrieve Customer Sales History Detail using HQsalesperson
    [Tags]    hqsalesperson    KPI    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Customer Sales History Detail using hqsalesperson
    Then expected return status code 200

10 - Able to get Customer Stock Take History Product using HQsalesperson
    [Documentation]    Able to retrieve Customer Stock Take History Product using HQsalesperson
    [Tags]    hqsalesperson    KPI    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Customer Stock Take History Product using hqsalesperson
    Then expected return status code 200

11 - Able to get Customer History Transaction Product using HQsalesperson
    [Documentation]    Able to retrieve CCustomer History Transaction Product using HQsalesperson
    [Tags]    hqsalesperson    KPI    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Customer History Transaction Product using hqsalesperson
    Then expected return status code 200

12 - Able to get KPI CSL Customer Header using HQsalesperson
    [Documentation]    Able to retrieve KPI CSL Customer Header using HQsalesperson
    [Tags]    hqsalesperson    KPI    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves KPI CSL Customer Header using hqsalesperson
    Then expected return status code 200

13 - Able to get KPI CSL Customer Product using HQsalesperson
    [Documentation]    Able to retrieve KPI CSL Customer Product using HQsalesperson
    [Tags]    hqsalesperson    KPI    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves KPI CSL Customer Product using hqsalesperson
    Then expected return status code 200

14 - Able to get KPI Call Route using HQsalesperson
    [Documentation]    Able to retrieve KPI Call Route using HQsalesperson
    [Tags]    hqsalesperson    KPI    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves KPI Call Route using hqsalesperson
    Then expected return status code 200

15 - Able to get KPI No Sales Cust Route
    [Documentation]    Able to retrieve KPI No Sales Cust Route using salesperson
    [Tags]    salesperson    KPI    9.1
    Given user retrieves token access as salesperson
    When user retrieves KPI No Sales Cust Route using salesperson

16 - Unable to get KPI No Sales Cust Route
    [Documentation]    Unable to retrieve KPI No Sales Cust Route
    [Tags]    sysimp    KPI    9.1
    Given user retrieves token access as sysimp
    When user retrieves KPI No Sales Cust Route using sysimp
    Then expected return status code 403

17 - Able to get KPI Average SKU Route
    [Documentation]    Able to retrieve KPI Average SKU Route
    [Tags]    salesperson    KPI    9.1     BUG:NRSZUANQ-52085
    Given user retrieves token access as salesperson
    When user retrieves KPI Average SKU Route using salesperson
    Then expected return status code 200

18 - Unable to get KPI Average SKU Route
    [Documentation]    Unable to retrieve KPI Average SKU Route
    [Tags]    sysimp    KPI    9.1
    Given user retrieves token access as sysimp
    When user retrieves KPI Average SKU Route using sysimp
    Then expected return status code 403

19 - Able to get KPI Stale Route
    [Documentation]    Able to retrieve KPI Stale Route
    [Tags]    salesperson    KPI    9.1      BUG:NRSZUANQ-52085
    Given user retrieves token access as salesperson
    When user retrieves KPI Stale Route using salesperson
    Then expected return status code 200

20 - Unable to get KPI Stale Route
    [Documentation]    Unable to retrieve KPI Stale Route
    [Tags]    sysimp    KPI    9.1
    Given user retrieves token access as sysimp
    When user retrieves KPI Stale Route using sysimp
    Then expected return status code 403

21 - Able to get KPI Average SKU Cust
    [Documentation]    Able to retrieve KPI Average SKU Cust
    [Tags]    salesperson    KPI    9.1        BUG:NRSZUANQ-52085
    Given user retrieves token access as salesperson
    When user retrieves KPI Average SKU Cust using salesperson
    Then expected return status code 200

22 - Unable to get KPI Average SKU Cust
    [Documentation]    Unable to retrieve KPI Average SKU Cust
    [Tags]    sysimp    KPI    9.1
    Given user retrieves token access as sysimp
    When user retrieves KPI Average SKU Cust using sysimp
    Then expected return status code 403

23 - Able to get KPI Stale Cust
    [Documentation]    Able to retrieve KPI Stale Cust
    [Tags]    salesperson    KPI    9.1      BUG:NRSZUANQ-52085
    Given user retrieves token access as salesperson
    When user retrieves KPI Stale Cust using salesperson
    Then expected return status code 200

24 - Unable to get KPI Stale Cust
    [Documentation]    Unable to retrieve KPI Stale Cust
    [Tags]    sysimp    KPI    9.1
    Given user retrieves token access as sysimp
    When user retrieves KPI Stale Cust using sysimp
    Then expected return status code 403