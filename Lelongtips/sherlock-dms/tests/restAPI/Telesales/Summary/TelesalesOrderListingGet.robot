*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Telesales/Summary/TelesalesOrderListingGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py

*** Test Cases ***
1 - Able to GET summary listing by order number using telesales access
    [Documentation]  To get summary listing by order number using telesales access via API
    [Tags]    telesales     9.3     NRSZUANQ-57405
    [Setup]     run keywords
    ...     user retrieves token access as hqadm
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user retrieves summary listing by order number SO0000008258
    Then expected return status code 200

2 - Able to GET summary listing by order number using hq telesales access
    [Documentation]  To get summary listing by order number using hq telesales access via API
    [Tags]    hqtelesales     9.3     NRSZUANQ-57405
    [Setup]     run keywords
    ...     user retrieves token access as hqadm
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user retrieves summary listing by order number SO0000008261
    Then expected return status code 200

3 - Able to GET summary listing by from order date and to order date
    [Documentation]  To get summary listing by from order date and to order date via API
    [Tags]    telesales     hqtelesales     9.3     NRSZUANQ-57405
    [Setup]     run keywords
    ...     user retrieves token access as hqadm
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user retrieves summary listing by from order date and to order date, 2021-10-13 and 2021-10-29
    Then expected return status code 200

4 - Able to GET summary listing by order type
    [Documentation]  To get summary listing by order type via API
    [Tags]    telesales     hqtelesales     9.3     NRSZUANQ-57405
    [Setup]     run keywords
    ...     user retrieves token access as hqadm
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user retrieves summary listing by order type S
    Then expected return status code 200

5 - Able to GET summary listing by customer code
    [Documentation]  To get summary listing by customer code via API
    [Tags]    telesales     hqtelesales     9.3     NRSZUANQ-57405
    [Setup]     run keywords
    ...     user retrieves token access as hqadm
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user retrieves summary listing by customer code CT0000001812
    Then expected return status code 200

6 - Able to GET summary listing by delivery date
    [Documentation]  To get summary listing by delivery date via API
    [Tags]    telesales     hqtelesales     9.3     NRSZUANQ-57405
    [Setup]     run keywords
    ...     user retrieves token access as hqadm
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user retrieves summary listing by delivery date 2021-11-03
    Then expected return status code 200

7 - Able to GET summary listing by total net tax
    [Documentation]  To get summary listing by total net tax via API
    [Tags]    telesales     hqtelesales     9.3     NRSZUANQ-57405
    [Setup]     run keywords
    ...     user retrieves token access as hqadm
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user retrieves summary listing by total net tax 378
    Then expected return status code 200

8 - Able to GET summary listing by adjustment amount
    [Documentation]  To get summary listing by adjustment amount via API
    [Tags]    telesales     hqtelesales     9.3     NRSZUANQ-57405
    [Setup]     run keywords
    ...     user retrieves token access as hqadm
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user retrieves summary listing by adjustment amount 0
    Then expected return status code 200

9 - Able to GET summary listing by order status
    [Documentation]  To get summary listing by order status via API
    [Tags]    telesales     hqtelesales     9.3     NRSZUANQ-57405
    [Setup]     run keywords
    ...     user retrieves token access as hqadm
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user retrieves summary listing by order status P
    Then expected return status code 200

10 - Able to GET summary listing by customer ID
    [Documentation]  To get summary listing by customer ID via API
    [Tags]    telesales     hqtelesales     9.3     NRSZUANQ-57176
    [Setup]     run keywords
    ...     user retrieves token access as hqadm
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user retrieves summary listing by customer ID 81398E09:C0D52634-9685-4CC3-8171-57DA1A05E7DC
    Then expected return status code 200