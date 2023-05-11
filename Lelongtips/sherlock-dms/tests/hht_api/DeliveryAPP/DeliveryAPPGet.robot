*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/DeliveryAPP/DeliveryAPP.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py

Test Setup        user gets distributor by using code 'DistPotato01'

*** Test Cases ***
1 - Able to retrieves Step of call setup
    [Documentation]    Able to retrieves Step of call setup
    [Tags]    salespersonDR    Setup
    Given user retrieves token access as salesperson
    When user retrieves Step Of Call setup using salesperson
    Then expected return status code 403
#    And Step of Call data correctly downloaded

2 - Able to retrieves activity assignment setup
    [Documentation]    Able to retrieves activity assignment setup
    [Tags]    salespersonDR    Setup
    Given user retrieves token access as salesperson
    When user retrieves activity assignment using salesperson
    Then expected return status code 403

3 - Able to retrieves Merchandising Step of call
    [Documentation]    Able to retrieves Merchandising Step of call setup
    [Tags]    salespersonDR    Setup
    Given user retrieves token access as salesperson
    When user retrieves Merchandising Step of Call using salesperson
    Then expected return status code 403

4 - Able to retrieves aging term
    [Documentation]    Able to retrieves aging term setup
    [Tags]    salespersonDR    Setup
    Given user retrieves token access as salesperson
    When user retrieves aging term using salesperson
    Then expected return status code 200

5 - Able to retrieves setting invoice term
    [Documentation]    Able to retrieves setting invoice term
    [Tags]    salespersonDR    Setup
    Given user retrieves token access as salesperson
    When user retrieves setting invoice term using salesperson
    Then expected return status code 200

6 - Able to retrieves setting invoice term details
    [Documentation]    Able to retrieves setting invoice term details
    [Tags]    salespersonDR    Setup
    Given user retrieves token access as ${user_role}
    When user retrieves invoice term details
    Then expected return status code 200

7 - Able to retrieves bank setting
    [Documentation]    Able to retrieves bank setting
    [Tags]    salespersonDR    Setup
    Given user retrieves token access as salesperson
    When user retrieves bank setting using salesperson
    Then expected return status code 200

8 - Able to retrieves van setting
    [Documentation]    Able to retrieves van setting
    [Tags]    salespersonDR    Setup
    Given user retrieves token access as ${user_role}
    When user retrieves van setting
    Then expected return status code 200

9 - Able to retrieves warehouse setting
    [Documentation]    Able to retrieves warehouse setting
    [Tags]    salespersonDR    Setup
    Given user retrieves token access as salesperson
    When user retrieves warehouse setting using salesperson
    Then expected return status code 200

10 - Able to retrieves message setup
    [Documentation]    Able to retrieves message setup
    [Tags]    salespersonDR    Setup
    Given user retrieves token access as ${user_role}
    When user retrieves message setup
    Then expected return status code 200

11 - Able to retrieves message assignment
    [Documentation]    Able to retrieves message assignment
    [Tags]    salespersonDR    Setup
    Given user retrieves token access as ${user_role}
    When user retrieves message assignment
    Then expected return status code 200

12 - Able to retrieves application setup
    [Documentation]    Able to retrieves application setup
    [Tags]    salespersonDR    Setup
    Given user retrieves token access as ${user_role}
    When user retrieves application setup
    Then expected return status code 200

13 - Able to retrieves application setup reference
    [Documentation]    Able to retrieves application setup reference
    [Tags]    salespersonDR    Setup
    Given user retrieves token access as ${user_role}
    When user retrieves application setup reference
    Then expected return status code 200

14 - Able to retrieves application setup parameter
    [Documentation]    Able to retrieves application setup parameter
    [Tags]    salespersonDR    Setup
    Given user retrieves token access as ${user_role}
    When user retrieves application setup parameter
    Then expected return status code 200
15 - Able to retrieves promotion
    [Documentation]    Able to retrieves Promotion
    [Tags]    salespersonDR    Promo
    Given user retrieves token access as salesperson
    When user retrieves promotion using salesperson
    Then expected return status code 500

16 - Able to retrieves promotion slab
    [Documentation]    Able to retrieves Promotion slab
    [Tags]    salespersonDR    Promo
    Given user retrieves token access as salesperson
    When user retrieves promotion slab using salesperson
    Then expected return status code 200

17 - Able to retrieves promotion FOC
    [Documentation]    Able to retrieves Promotion FOC
    [Tags]    salespersonDR    Promo
    Given user retrieves token access as salesperson
    When user retrieves promotion FOC using salesperson
    Then expected return status code 500

18 - Able to retrieves promotion product
    [Documentation]    Able to retrieves Promotion product
    [Tags]    salespersonDR    Promo
    Given user retrieves token access as salesperson
    When user retrieves promotion product using salesperson
    Then expected return status code 200

19 - Able to retrieves promotion's distributor assignment
    [Documentation]    Able to retrieves promotion's distributor assignment
    [Tags]    salespersonDR    Promo
    Given user retrieves token access as salesperson
    When user retrieves promotion's distributor assignment using salesperson
    Then expected return status code 500

20 - Able to retrieves promotion's distributor exclusion
    [Documentation]    Able to retrieves promotion's distributor exclusion
    [Tags]    salespersonDR    Promo
    Given user retrieves token access as salesperson
    When user retrieves promotion's distributor exclusion using salesperson
    Then expected return status code 500

21 - Able to retrieves promotion's customer assignment
    [Documentation]    Able to retrieves promotion's customer assignment
    [Tags]    salespersonDR    Promo
    Given user retrieves token access as salesperson
    When user retrieves promotion's customer assignment using salesperson
    Then expected return status code 500

22 - Able to retrieves promotion's customer exclusion
    [Documentation]    Able to retrieves promotion's customer exclusion
    [Tags]    salespersonDR    Promo
    Given user retrieves token access as salesperson
    When user retrieves promotion's customer exclusion using salesperson
    Then expected return status code 500

23 - Able to retrieves promotion's product exclusion
    [Documentation]    Able to retrieves promotion's customer assignment
    [Tags]    salespersonDR    Promo
    Given user retrieves token access as salesperson
    When user retrieves promotion's product exclusion using salesperson
    Then expected return status code 204

24 - Able to retrieves promotion's budget assignment
    [Documentation]    Able to retrieves promotion's customer exclusion
    [Tags]    salespersonDR    Promo
    Given user retrieves token access as salesperson
    When user retrieves promotion's budget assignment using salesperson
    Then expected return status code 500

25 - Able to retrieves combi group promotion
    [Documentation]    Able to retrieves combi group promotion
    [Tags]    salespersonDR    Promo
    Given user retrieves token access as salesperson
    When user retrieves combi group promotion using salesperson
    Then expected return status code 200

26 - Able to retrieves max count promotion assignment
    [Documentation]    Able to retrieves max count promotion assignment
    [Tags]    salespersonDR    Promo
    Given user retrieves token access as salesperson
    When user retrieves max count promotion assignment using salesperson
    Then expected return status code 200

27 - Able to retrieves max count balance
    [Documentation]    Able to retrieves max count balance
    [Tags]    salespersonDR    Promo
    Given user retrieves token access as salesperson
    When user retrieves max count balance using salesperson
    Then expected return status code 200

28 - Able to retrieves promotion sequence
    [Documentation]    Able to retrieves promotion sequence
    [Tags]    salespersonDR    Promo
    Given user retrieves token access as salesperson
    When user retrieves promotion sequence using salesperson
    Then expected return status code 200

29 - Able to retrieves promotion sequence
    [Documentation]    Able to retrieves promotion sequence
    [Tags]    salespersonDR    Promo
    Given user retrieves token access as salesperson
    When user retrieves promotion sequence using salesperson
    Then expected return status code 200

30 - Able to retrieves QPS promotion's transaction header
    [Documentation]    Able to retrieves QPS promotion's transaction header
    [Tags]    salespersonDR    Promo
    Given user retrieves token access as salesperson
    When user retrieves QPS promotion's transaction header using salesperson
    Then expected return status code 403

31 - Able to retrieves QPS promotion product
    [Documentation]    Able to retrieves QPS promotion product
    [Tags]    salespersonDR    Promo
    Given user retrieves token access as salesperson
    When user retrieves QPS promotion product using salesperson
    Then expected return status code 200

32 - Able to retrieves QPS promotion FOC
    [Documentation]    Able to retrieves QPS promotion FOC
    [Tags]    salespersonDR    Promo
    Given user retrieves token access as salesperson
    When user retrieves QPS promotion FOC using salesperson
    Then expected return status code 403

33 - Able to retrieves QPS promotion invoice
    [Documentation]    Able to retrieves QPS promotion invoice
    [Tags]    salespersonDR    Promo
    Given user retrieves token access as salesperson
    When user retrieves QPS promotion invoice using salesperson
    Then expected return status code 403
