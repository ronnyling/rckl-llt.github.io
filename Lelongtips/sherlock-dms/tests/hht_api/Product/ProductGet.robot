*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py
Library           ${EXECDIR}${/}resources/hht_api/Product/ProductGet.py

Test Setup        user gets distributor by using code 'DistPotato01'

*** Test Cases ***
1 - Able to get Product Sync Details using HQsalesperson
    [Documentation]    Able to retrieve Product Sync Details using HQsalesperson
    [Tags]    hqsalesperson    Product    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Product Details using hqsalesperson
    Then expected return status code 200

2 - Able to get Product UOM Sync Details using HQsalesperson
    [Documentation]    Able to retrieve Product UOM Sync Details using HQsalesperson
    [Tags]    hqsalesperson    Product    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Product UOM Details using hqsalesperson
    Then expected return status code 200

3 - Able to get Product Find Attribute Sync Details using HQsalesperson
    [Documentation]    Able to retrieve Product Find Attribute Sync Details using HQsalesperson
    [Tags]    hqsalesperson    Product    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Product Find Attribute Details using hqsalesperson
    Then expected return status code 200

4 - Able to get Product Cost Price Sync Details using HQsalesperson
    [Documentation]    Able to retrieve Product Cost Price Sync Details using HQsalesperson
    [Tags]    hqsalesperson    Product    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Product Cost Price Details using hqsalesperson
    Then expected return status code 200

5 - Able to get Product Inventory MRP Sync Details using HQsalesperson
    [Documentation]    Able to retrieve Product Inventory MRP Details using HQsalesperson
    [Tags]    hqsalesperson    Product    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Product Inventory MRP Details using hqsalesperson
    Then expected return status code 200

6 - Able to get Product Find Sync Details using HQsalesperson
    [Documentation]    Able to retrieve Product Find Details using HQsalesperson
    [Tags]    hqsalesperson    Product    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Product Find Details using hqsalesperson
    Then expected return status code 200

7 - Able to get POSM Material Sync Details using HQsalesperson
    [Documentation]    Able to retrieve POSM Material Details using HQsalesperson
    [Tags]    hqsalesperson    Product    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves POSM Material Details using hqsalesperson
    Then expected return status code 200

8 - Able to get POSM Route Product Sector using salesperson
    [Documentation]    Able to retrieve POSM Route Product Sector
    [Tags]    salesperson    Product    9.1
    Given user retrieves token access as salesperson
    When user retrieves POSM Route Product Sector using salesperson
    Then expected return status code 200

9 - Able to get POSM Route Product Sector using HQsalesperson
    [Documentation]    Able to retrieve POSM Route Product Sector using HQsalesperson
    [Tags]    hqsalesperson    Product    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves POSM Route Product Sector using hqsalesperson
    Then expected return status code 200

10 - Unable to get POSM Route Product Sector using system implementer
    [Documentation]    Unable to retrieve POSM Route Product Sector using system implementer
    [Tags]    sysimp    Product    9.1
    Given user retrieves token access as sysimp
    When user retrieves POSM Route Product Sector using sysimp
    Then expected return status code 403
