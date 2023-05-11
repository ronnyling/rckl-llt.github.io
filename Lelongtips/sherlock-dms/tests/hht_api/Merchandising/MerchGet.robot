*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/Merchandising/MerchandisingGet.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py

Test Setup        user gets distributor by using code 'DistMerch'

*** Test Cases ***
1 - Able to retrieves Merchandising activities
    [Documentation]    Able to retrieves Merchandising activities
    [Tags]    salesperson1    Merch    9.1     bugticket:NRSZUANQ-52633
    Given user retrieves token access as ${user_role}
    When user retrieves Merchandising activity using merchandiser
    Then expected return status code 200

2 - Unable to retrieves Merchandising activities
    [Documentation]    Unable to retrieve Merchandising activiy record when no data, return 204
    [Tags]    salesperson1    Merch    9.1    TODO      bugticket:NRSZUANQ-52633
    Given user retrieves token access as ${user_role}
    When user retrieves Merchandising activity using merchandiser
    Then expected return status code 200

3 - Unable to retrieve Merchandising activiy using invalid access
    [Documentation]    Unable to retrieve Merchandising activiy using invalid access, return 403
    [Tags]    salesperson    Merch    9.1
    Given user retrieves token access as ${user_role}
    When user retrieves Merchandising activity history using merchandiser
    Then expected return status code 200

4 - Able to retrieves Merchandising activity history
    [Documentation]    Able to retrieves Merchandising activity history
    [Tags]    salesperson    Merch    9.1
    Given user retrieves token access as ${user_role}
    When user retrieves Merchandising activity history using merchandiser
    Then expected return status code 200

5 - Unable to retrieves Merchandising activity history
    [Documentation]    Unable to retrieve Merchandising activiy history when no data, return 204
    [Tags]    salesperson    Merch    9.1    TODO
    Given user retrieves token access as ${user_role}
    When user retrieves Merchandising activity history using merchandiser
    Then expected return status code 200

6 - Unable to retrieve Merchandising activiy history using invalid access
    [Documentation]    Unable to retrieve Merchandising activiy history using invalid access, return 403
    [Tags]    salesperson    Merch    9.1
    Given user retrieves token access as ${user_role}
    When user retrieves Merchandising activity history using merchandiser
    Then expected return status code 200

7 - Able to get Merch Product Group using HQmerchandiser
    [Documentation]    Able to retrieve Merch Product Group using HQmerchandiser
    [Tags]    hqmerchandiser    Merch    9.1
    Given user retrieves token access as hqmerchandiser
    When user retrieves Merch Product Group using hqmerchandiser
    Then expected return status code 200

8 - Able to get Merch Store Space using HQmerchandiser
    [Documentation]    Able to retrieve Merch Store Space using HQmerchandiser
    [Tags]    hqmerchandiser1    Merch    9.1
    Given user retrieves token access as hqmerchandiser
    When user retrieves Merch Store Space using hqmerchandiser
    Then expected return status code 200

9 - Able to get Merch Store Space Level using HQmerchandiser
    [Documentation]    Able to retrieve Merch Store Space Level using HQmerchandiser
    [Tags]    hqmerchandiser    Merch    9.1
    Given user retrieves token access as hqmerchandiser
    When user retrieves Merch Store Space Level using hqmerchandiser
    Then expected return status code 200

10 - Able to get Merch Route Activity using HQmerchandiser
    [Documentation]    Able to retrieve Merch Route Activity using HQmerchandiser
    [Tags]    hqmerchandiser    Merch    9.1
    Given user retrieves token access as hqmerchandiser
    When user retrieves Merch Route Activity using hqmerchandiser
    Then expected return status code 200

10 - Able to get Merch Customer Assignment using HQmerchandiser
    [Documentation]    Able to retrieve Merch Customer Assignment using HQmerchandiser
    [Tags]    hqmerchandiser    Merch    9.1
    Given user retrieves token access as hqmerchandiser
    When user retrieves Merch Customer Assignment using hqmerchandiser
    Then expected return status code 200

11 - Able to retrieves Merchandising activities using HQmerchandiser
    [Documentation]    Able to retrieves Merchandising activities using HQmerchandiser
    [Tags]    hqmerchandiser    Merch    9.1
    Given user retrieves token access as hqmerchandiser
    When user retrieves Merchandising activity using hqmerchandiser
    Then expected return status code 200

15 - Able to retrieves Merchandising activity history using HQmerchandiser
    [Documentation]    Able to retrieves Merchandising activity history using HQmerchandiser
    [Tags]    hqmerchandiser    Merch    9.1
    Given user retrieves token access as hqmerchandiser
    When user retrieves Merchandising activity history using hqmerchandiser
    Then expected return status code 200

16 - Able to retrieves Merchandising Audit using HQmerchandiser
    [Documentation]    Able to retrieves Merchandising Audit using HQmerchandiser
    [Tags]    hqmerchandiser    Merch    9.1
    Given user retrieves token access as hqmerchandiser
    When user retrieves Merch Audit using hqmerchandiser
    Then expected return status code 200

17 - Able to retrieves Merchandising Audit Customer using HQmerchandiser
    [Documentation]    Able to retrieves Merchandising Audit Customer using HQmerchandiser
    [Tags]    hqmerchandiser    Merch    9.1
    Given user retrieves token access as hqmerchandiser
    When user retrieves Merch Audit Customer using hqmerchandiser
    Then expected return status code 200

18 - Able to retrieves Merchandising Audit Attribute using HQmerchandiser
    [Documentation]    Able to retrieves Merchandising Audit Attribute using HQmerchandiser
    [Tags]    hqmerchandiser    Merch    9.1
    Given user retrieves token access as hqmerchandiser
    When user retrieves Merch Audit Attribute using hqmerchandiser
    Then expected return status code 200

19 - Able to retrieves Merchandising Distribution Check using HQmerchandiser
    [Documentation]    Able to retrieves Merchandising Distribution Check using HQmerchandiser
    [Tags]    hqmerchandiser    Merch    9.1
    Given user retrieves token access as hqmerchandiser
    When user retrieves Merch Distribution Check using hqmerchandiser
    Then expected return status code 200

20 - Able to retrieves Merchandising Audit Price using HQmerchandiser
    [Documentation]    Able to retrieves Merchandising Audit Price using HQmerchandiser
    [Tags]    hqmerchandiser    Merch    9.1
    Given user retrieves token access as hqmerchandiser
    When user retrieves Merch Audit Price using hqmerchandiser
    Then expected return status code 200

21 - Able to retrieves Merchandising Audit Facing using HQmerchandiser
    [Documentation]    Able to retrieves Merchandising Audit Facing using HQmerchandiser
    [Tags]    hqmerchandiser    Merch    9.1
    Given user retrieves token access as hqmerchandiser
    When user retrieves Merch Audit Facing using hqmerchandiser
    Then expected return status code 200

22 - Able to retrieves Merchandising Audit Plano using HQmerchandiser
    [Documentation]    Able to retrieves Merchandising Audit Plano using HQmerchandiser
    [Tags]    hqmerchandiser    Merch    9.1
    Given user retrieves token access as hqmerchandiser
    When user retrieves Merch Audit Plano using hqmerchandiser
    Then expected return status code 200

23 - Able to retrieves Transaction Merchandising Price using HQmerchandiser
    [Documentation]    Able to retrieves Transaction Merchandising Price using HQmerchandiser
    [Tags]    hqmerchandiser    Merch    9.1
    Given user retrieves token access as hqmerchandiser
    When user retrieves Transaction Merch Price using hqmerchandiser
    Then expected return status code 200

24 - Able to retrieves Transaction Merchandising Price Product using HQmerchandiser
    [Documentation]    Able to retrieves Transaction Merchandising Price Product using HQmerchandiser
    [Tags]    hqmerchandiser    Merch    9.1    TODO
    Given user retrieves token access as hqmerchandiser
    When user retrieves Transaction Merch Price Product using hqmerchandiser
    Then expected return status code 200

25 - Able to retrieves Merchandising Audit Promo using HQmerchandiser
    [Documentation]    Able to retrieves Merchandising Audit Promo using HQmerchandiser
    [Tags]    hqmerchandiser    Merch    9.1
    Given user retrieves token access as hqmerchandiser
    When user retrieves Merch Audit Promo using hqmerchandiser
    Then expected return status code 200

26 - Able to retrieves Merchandising Checklist Header using HQmerchandiser
    [Documentation]    Able to retrieves Merchandising Checklist Header using HQmerchandiser
    [Tags]    hqmerchandiser    Merch    9.1
    Given user retrieves token access as hqmerchandiser
    When user retrieves Merc Checklist Header using hqmerchandiser
    Then expected return status code 200

27 - Able to retrieves Merchandising Checklist Details using HQmerchandiser
    [Documentation]    Able to retrieves Merchandising Checklist Details using HQmerchandiser
    [Tags]    hqmerchandiser    Merch    9.1
    Given user retrieves token access as hqmerchandiser
    When user retrieves Merc Checklist Details using hqmerchandiser
    Then expected return status code 200

28 - Able to retrieves Merchandising Checklist Customer using HQmerchandiser
    [Documentation]    Able to retrieves Merchandising Checklist Customer using HQmerchandiser
    [Tags]    hqmerchandiser    Merch    9.1
    Given user retrieves token access as hqmerchandiser
    When user retrieves Merc Checklist Customer using hqmerchandiser
    Then expected return status code 200