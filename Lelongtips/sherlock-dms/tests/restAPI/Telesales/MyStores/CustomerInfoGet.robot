*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Telesales/MyStores/CustomerInfoGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py

*** Test Cases ***
1 - Able to GET telesales info for the customer details section in Dashboard
    [Documentation]  To test get telesales info for the customer details section in Dashboard via API
    [Tags]    telesales     hqtelesales        9.3     NRSZUANQ-56896
    Given user retrieves token access as ${user_role}
    When user retrieves all telesales info
    Then expected return status code 200

2 - Able to GET customer info and address for the customer details section in Dashboard
    [Documentation]  To test get customer info and address for the customer details section in Dashboard via API
    [Tags]    telesales        hqtelesales       9.3     NRSZUANQ-56898     NRSZUANQ-56899
    [Setup]     run keywords
    ...     user retrieves token access as hqadm
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user retrieves cust info and address for CXTESTTAX
    Then expected return status code 200

3 - Able to GET customer hierarchy for the customer details section in Dashboard
    [Documentation]  To test get customer hierarchy for the customer details section in Dashboard via API
    [Tags]    telesales     hqtelesales       9.3     NRSZUANQ-56898
    [Setup]     run keywords
    ...     user retrieves token access as hqadm
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user retrieves cust hierarchy for CXTESTTAX
    Then expected return status code 200

4 - Able to GET customer attribute for the customer details section in Dashboard
    [Documentation]  To test get customer attribute for the customer details section in Dashboard via API
    [Tags]    telesales     hqtelesales       9.3     NRSZUANQ-56898
    Given user retrieves token access as ${user_role}
    When user retrieves cust attribute
    Then expected return status code 200

