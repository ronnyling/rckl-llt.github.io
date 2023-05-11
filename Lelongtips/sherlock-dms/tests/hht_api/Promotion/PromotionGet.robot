*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/Promotion/PromotionGet.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py

Test Setup        user gets distributor by using code 'DistPotato01'

*** Test Cases ***
1 - Able to retrieves promotion
    [Documentation]    Able to retrieves Promotion
    [Tags]    salesperson    Promo    9.1
    Given user retrieves token access as salesperson
    When user retrieves promotion using salesperson
    Then expected return status code 500

2 - Able to retrieves promotion slab
    [Documentation]    Able to retrieves Promotion slab
    [Tags]    salesperson    Promo    9.1
    Given user retrieves token access as salesperson
    When user retrieves promotion slab using salesperson
    Then expected return status code 200

3 - Able to retrieves promotion FOC
    [Documentation]    Able to retrieves Promotion FOC
    [Tags]    salesperson    Promo    9.1
    Given user retrieves token access as salesperson
    When user retrieves promotion FOC using salesperson
    Then expected return status code 500

4 - Able to retrieves promotion product
    [Documentation]    Able to retrieves Promotion product
    [Tags]    salesperson    Promo    9.1
    Given user retrieves token access as salesperson
    When user retrieves promotion product using salesperson
    Then expected return status code 200

5 - Able to retrieves promotion's distributor assignment
    [Documentation]    Able to retrieves promotion's distributor assignment
    [Tags]    salesperson    Promo    9.1
    Given user retrieves token access as salesperson
    When user retrieves promotion's distributor assignment using salesperson
    Then expected return status code 500

6 - Able to retrieves promotion's distributor exclusion
    [Documentation]    Able to retrieves promotion's distributor exclusion
    [Tags]    salesperson    Promo    9.1
    Given user retrieves token access as salesperson
    When user retrieves promotion's distributor exclusion using salesperson
    Then expected return status code 500

7 - Able to retrieves promotion's customer assignment
    [Documentation]    Able to retrieves promotion's customer assignment
    [Tags]    salesperson    Promo    9.1
    Given user retrieves token access as salesperson
    When user retrieves promotion's customer assignment using salesperson
    Then expected return status code 500

8 - Able to retrieves promotion's customer exclusion
    [Documentation]    Able to retrieves promotion's customer exclusion
    [Tags]    salesperson    Promo    9.1
    Given user retrieves token access as salesperson
    When user retrieves promotion's customer exclusion using salesperson
    Then expected return status code 500

9 - Able to retrieves promotion's product exclusion
    [Documentation]    Able to retrieves promotion's customer assignment
    [Tags]    salesperson    Promo    9.1
    Given user retrieves token access as salesperson
    When user retrieves promotion's product exclusion using salesperson
    Then expected return status code 204

10 - Able to retrieves promotion's budget assignment
    [Documentation]    Able to retrieves promotion's customer exclusion
    [Tags]    salesperson    Promo    9.1
    Given user retrieves token access as salesperson
    When user retrieves promotion's budget assignment using salesperson
    Then expected return status code 500

11 - Able to retrieves combi group promotion
    [Documentation]    Able to retrieves combi group promotion
    [Tags]    salesperson    Promo    9.1
    Given user retrieves token access as salesperson
    When user retrieves combi group promotion using salesperson
    Then expected return status code 200

12 - Able to retrieves max count promotion assignment
    [Documentation]    Able to retrieves max count promotion assignment
    [Tags]    salesperson    Promo    9.1
    Given user retrieves token access as salesperson
    When user retrieves max count promotion assignment using salesperson
    Then expected return status code 200

13 - Able to retrieves max count balance
    [Documentation]    Able to retrieves max count balance
    [Tags]    salesperson    Promo    9.1
    Given user retrieves token access as salesperson
    When user retrieves max count balance using salesperson
    Then expected return status code 200

14 - Able to retrieves promotion sequence
    [Documentation]    Able to retrieves promotion sequence
    [Tags]    salesperson    Promo    9.1
    Given user retrieves token access as salesperson
    When user retrieves promotion sequence using salesperson
    Then expected return status code 200

15 - Able to retrieves promotion sequence
    [Documentation]    Able to retrieves promotion sequence
    [Tags]    salesperson    Promo    9.1
    Given user retrieves token access as salesperson
    When user retrieves promotion sequence using salesperson
    Then expected return status code 200

16 - Able to retrieves QPS promotion's transaction header
    [Documentation]    Able to retrieves QPS promotion's transaction header
    [Tags]    salesperson    Promo    9.1
    Given user retrieves token access as salesperson
    When user retrieves QPS promotion's transaction header using salesperson
    Then expected return status code 403

17 - Able to retrieves QPS promotion product
    [Documentation]    Able to retrieves QPS promotion product
    [Tags]    salesperson    Promo    9.1      BUG:NRSZUANQ-52085
    Given user retrieves token access as salesperson
    When user retrieves QPS promotion product using salesperson

18 - Able to retrieves QPS promotion FOC
    [Documentation]    Able to retrieves QPS promotion FOC
    [Tags]    salesperson    Promo    9.1
    Given user retrieves token access as salesperson
    When user retrieves QPS promotion FOC using salesperson
    Then expected return status code 403

19 - Able to retrieves QPS promotion invoice
    [Documentation]    Able to retrieves QPS promotion invoice
    [Tags]    salesperson    Promo    9.1
    Given user retrieves token access as salesperson
    When user retrieves QPS promotion invoice using salesperson
    Then expected return status code 403

20 - Able to retrieves promotion using HQsalesperson
    [Documentation]    Able to retrieves Promotion using HQsalesperson
    [Tags]    hqsalesperson    Promo    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves promotion using hqsalesperson
    Then expected return status code 200

21 - Able to retrieves promotion slab using HQsalesperson
    [Documentation]    Able to retrieves Promotion slab using HQsalesperson
    [Tags]    hqsalesperson    Promo    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves promotion slab using hqsalesperson
    Then expected return status code 200

22 - Able to retrieves promotion FOC using HQsalesperson
    [Documentation]    Able to retrieves Promotion FOC using HQsalesperson
    [Tags]    hqsalesperson    Promo    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves promotion FOC using hqsalesperson
    Then expected return status code 200

23 - Able to retrieves promotion product using HQsalesperson
    [Documentation]    Able to retrieves Promotion product using HQsalesperson
    [Tags]    hqsalesperson    Promo    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves promotion product using hqsalesperson
    Then expected return status code 200

24 - Able to retrieves promotion's distributor assignment using HQsalesperson
    [Documentation]    Able to retrieves promotion's distributor assignment using HQsalesperson
    [Tags]    hqsalesperson    Promo    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves promotion's distributor assignment using hqsalesperson
    Then expected return status code 200

25 - Able to retrieves promotion's distributor exclusion using HQsalesperson
    [Documentation]    Able to retrieves promotion's distributor exclusion using HQsalesperson
    [Tags]    hqsalesperson    Promo    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves promotion's distributor exclusion using hqsalesperson
    Then expected return status code 200

26 - Able to retrieves promotion's customer assignment using HQsalesperson
    [Documentation]    Able to retrieves promotion's customer assignment using HQsalesperson
    [Tags]    hqsalesperson    Promo    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves promotion's customer assignment using hqsalesperson
    Then expected return status code 200

27 - Able to retrieves promotion's customer exclusion using HQsalesperson
    [Documentation]    Able to retrieves promotion's customer exclusion using HQsalesperson
    [Tags]    hqsalesperson    Promo    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves promotion's customer exclusion using hqsalesperson
    Then expected return status code 200

28 - Able to retrieves promotion's product exclusion using HQsalesperson
    [Documentation]    Able to retrieves promotion's customer assignment using HQsalesperson
    [Tags]    hqsalesperson    Promo    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves promotion's product exclusion using hqsalesperson
    Then expected return status code 200

29 - Able to retrieves promotion's budget assignment using HQsalesperson
    [Documentation]    Able to retrieves promotion's customer exclusion using HQsalesperson
    [Tags]    hqsalesperson    Promo    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves promotion's budget assignment using hqsalesperson
    Then expected return status code 200

30 - Able to retrieves combi group promotion using HQsalesperson
    [Documentation]    Able to retrieves combi group promotion using HQsalesperson
    [Tags]    hqsalesperson    Promo    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves combi group promotion using hqsalesperson
    Then expected return status code 200

31 - Able to retrieves max count promotion assignment using HQsalesperson
    [Documentation]    Able to retrieves max count promotion assignment using HQsalesperson
    [Tags]    hqsalesperson    Promo    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves max count promotion assignment using hqsalesperson
    Then expected return status code 200

32 - Able to retrieves max count balance using HQsalesperson
    [Documentation]    Able to retrieves max count balance using HQsalesperson
    [Tags]    hqsalesperson    Promo    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves max count balance using hqsalesperson
    Then expected return status code 200

33 - Able to retrieves promotion MRP using HQsalesperson
    [Documentation]    Able to retrieves promotion MRP
    [Tags]    hqsalesperson    Promo    9.1    TODO
    Given user retrieves token access as hqsalesperson
    When user retrieves promotion MRP using hqsalesperson
    Then expected return status code 200

34 - Able to retrieves promotion sequence using HQsalesperson
    [Documentation]    Able to retrieves promotion sequence
    [Tags]    hqsalesperson    Promo    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves promotion sequence using hqsalesperson
    Then expected return status code 200

35 - Able to retrieves QPS promotion's transaction header using HQsalesperson
    [Documentation]    Able to retrieves QPS promotion's transaction header
    [Tags]    hqsalesperson    Promo    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves QPS promotion's transaction header using hqsalesperson
    Then expected return status code 200

36 - Able to retrieves QPS promotion product using HQsalesperson
    [Documentation]    Able to retrieves QPS promotion product
    [Tags]    hqsalesperson    Promo    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves QPS promotion product using hqsalesperson
    Then expected return status code 200

37 - Able to retrieves QPS promotion FOC using HQsalesperson
    [Documentation]    Able to retrieves QPS promotion FOC
    [Tags]    hqsalesperson    Promo    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves QPS promotion FOC using hqsalesperson
    Then expected return status code 200

38 - Able to retrieves QPS promotion invoice using HQsalesperson
    [Documentation]    Able to retrieves QPS promotion invoice
    [Tags]    hqsalesperson    Promo    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves QPS promotion invoice using hqsalesperson
    Then expected return status code 200

39 - Able to retrieves customer group discount using salesperson
    [Documentation]    Able to retrieves customer group discount using salespersona and return 200
    [Tags]    salespersoncgd    9.3    NRSZUANQ-54580
    Given user retrieves token access as salesperson
    When user retrieves customer group discount
    Then expected return status code 200

40 - Able to retrieves customer group discount product assignment using salesperson
    [Documentation]    Able to retrieves customer group discount product assignment using salespersona and return 200
    [Tags]    salespersoncgd    9.3    NRSZUANQ-54580
    Given user retrieves token access as salesperson
    When user retrieves customer group discount product assignment
    Then expected return status code 200