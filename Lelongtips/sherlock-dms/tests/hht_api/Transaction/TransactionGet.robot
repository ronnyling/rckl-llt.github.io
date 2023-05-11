*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/Transaction/TransactionGet.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py

Test Setup        user gets distributor by using code 'DistPotato01'

*** Test Cases ***
1 - Able to retrieves invoice balance details
    [Documentation]    Able to retrieves invoice balance details
    [Tags]    salesperson    Transaction    9.1
    Given user retrieves token access as ${user_role}
    When user retrieves invoice balance details
    Then expected return status code 403

2 - Able to retrieves invoice balance promo
    [Documentation]    Able to retrieves invoice balance details
    [Tags]    salesperson    Transaction    9.1
    Given user retrieves token access as ${user_role}
    When user retrieves invoice balance details
    Then expected return status code 403

3 - Able to retrieves invoice balance FOC
    [Documentation]    Able to retrieves invoice balance FOC
    [Tags]    salesperson    Transaction    9.1
    Given user retrieves token access as ${user_role}
    When user retrieves invoice balance FOC
    Then expected return status code 403

4 - Able to retrieves invoice header
    [Documentation]    Able to retrieves invoice header
    [Tags]    salesperson    Transaction    9.1
    Given user retrieves token access as salesperson
    When user retrieves invoice header using salesperson
    Then expected return status code 403

5 - Able to retrieves invoice details
    [Documentation]    Able to retrieves invoice details
    [Tags]    salesperson    Transaction    9.1
    Given user retrieves token access as salesperson
    When user retrieves invoice details using salesperson
    Then expected return status code 403

6 - Able to retrieves invoice invoice details tax
    [Documentation]    Able to retrieves invoice invoice details tax
    [Tags]    salesperson    Transaction    9.1
    Given user retrieves token access as salesperson
    When user retrieves invoice details tax using salesperson
    Then expected return status code 403

7 - Able to retrieves invoice promotion
    [Documentation]    Able to retrieves invoice promotion
    [Tags]    salesperson    Transaction    9.1
    Given user retrieves token access as salesperson
    When user retrieves invoice promotion using salesperson
    Then expected return status code 403

8 - Able to retrieves invoice FOC promotion
    [Documentation]    Able to retrieves invoice FOC promotion
    [Tags]    salesperson    Transaction    9.1
    Given user retrieves token access as salesperson
    When user retrieves invoice FOC promotion using salesperson
    Then expected return status code 403

9 - Unable to retrieves invoice FOC promotion
    [Documentation]    Able to retrieves invoice FOC promotion using invalid access, return 403
    [Tags]    salesperson    Transaction    9.1
    [Template]    user retrieves invoice FOC promotion using given access
    distadm                403
    hqadm                  403

10 - Unable to retrieves invoice details
    [Documentation]    Able to retrieves invoice FOC promotion using invalid access, return 403
    [Tags]    salesperson    Transaction    9.1
    [Template]    user retrieves invoice FOC promotion using given access
    distadm                403
    hqadm                  403

11 - Able to get Sales Order Header using HQsalesperson
    [Documentation]    Able to retrieve Sales Order Header using HQsalesperson
    [Tags]    hqsalesperson    Transaction    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Sales Order using hqsalesperson
    Then expected return status code 200

12 - Able to get first x Sales Order Header using HQsalesperson
    [Documentation]    Able to retrieve first x Sales Order Header using HQsalesperson
    [Tags]    hqsalesperson    Transaction    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves first 6 Sales Order Header using hqsalesperson
    Then expected return status code 200

13 - Able to get first x Sales Order Detail using HQsalesperson
    [Documentation]    Able to retrieve first x Sales Order Detail using HQsalesperson
    [Tags]    hqsalesperson    Transaction    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves first 6 Sales Order Detail using hqsalesperson
    Then expected return status code 200

14 - Able to get Customer Sales Order Invoice using HQsalesperson
    [Documentation]    Able to retrieve Customer Sales Order Invoice using HQsalesperson
    [Tags]    hqsalesperson    Transaction    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Customer Sales Order Invoice using hqsalesperson
    Then expected return status code 200

15 - Able to retrieves invoice header using HQ salesperson
    [Documentation]    Able to retrieves invoice header using HQ salesperson
    [Tags]    HQSalesperson    Transaction    9.1    TODO
    Given user retrieves token access as hqsalesperson
    When user retrieves invoice header using hqsalesperson
    Then expected return status code 200

16 - Able to retrieves invoice details using HQ salesperson
    [Documentation]    Able to retrieves invoice details using HQ salesperson
    [Tags]    HQSalesperson    Transaction    9.1   TODO
    Given user retrieves token access as hqsalesperson
    When user retrieves invoice details using hqsalesperson
    Then expected return status code 200

17 - Able to retrieves invoice invoice details tax using HQ salesperson
    [Documentation]    Able to retrieves invoice invoice details tax using HQ salesperson
    [Tags]    HQSalesperson    Transaction    9.1    TODO
    Given user retrieves token access as hqsalesperson
    When user retrieves invoice details tax using hqsalesperson
    Then expected return status code 200

18 - Able to retrieves invoice promotion using HQ salesperson
    [Documentation]    Able to retrieves invoice promotion using HQ salesperson
    [Tags]    HQSalesperson    Transaction    9.1    TODO
    Given user retrieves token access as hqsalesperson
    When user retrieves invoice promotion using hqsalesperson
    Then expected return status code 200

19- Able to retrieves invoice FOC promotion using HQ salesperson
    [Documentation]    Able to retrieves invoice FOC promotion using HQ salesperson
    [Tags]    HQSalesperson    Transaction    9.1    TODO
    Given user retrieves token access as hqsalesperson
    When user retrieves invoice FOC promotion using hqsalesperson
    Then expected return status code 200

20- Able to retrieves invoice balance product using HQ salesperson
    [Documentation]    Able to retrieves invoice balance product using HQ salesperson
    [Tags]    HQSalesperson    Transaction    9.1    TODO
    Given user retrieves token access as hqsalesperson
    When user retrieves invoice balance product using hqsalesperson
    Then expected return status code 200

21- Able to retrieves invoice balance promotion using HQ salesperson
    [Documentation]    Able to retrieves invoice balance promotion using HQ salesperson
    [Tags]    HQSalesperson    Transaction    9.1    TODO
    Given user retrieves token access as hqsalesperson
    When user retrieves invoice balance promotion using hqsalesperson
    Then expected return status code 200

22- Able to retrieves invoice balance promotion FOC using HQ salesperson
    [Documentation]    Able to retrieves invoice balance promotion using HQ salesperson
    [Tags]    HQSalesperson    Transaction    9.1    TODO
    Given user retrieves token access as hqsalesperson
    When user retrieves invoice balance promotion FOC using hqsalesperson
    Then expected return status code 200

23- Able to retrieves Customer Open Item using HQ salesperson
    [Documentation]    Able to retrieves Customer Open Item using HQ salesperson
    [Tags]    HQSalesperson    Transaction    9.1
    Given user retrieves token access as hqsalesperson
    When user retrieves Customer Open Item using hqsalesperson
    Then expected return status code 200