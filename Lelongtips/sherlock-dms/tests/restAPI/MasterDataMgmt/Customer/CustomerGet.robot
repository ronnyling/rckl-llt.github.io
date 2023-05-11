*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerShipToDelete.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py
Library           Collections


*** Test Cases ***
1 - Unable to retrieve specified Customer's POSM data when there is not posm assigned
    [Documentation]    Unable to retrieve Customer's POSM data and expect return 204
    [Tags]    hqadm    distadm     9.1
    Given user retrieves token access as ${user_role}
    When user retrieves all cust
    Then expected return status code 200

2. Able to retrieve all Customer
    [Documentation]    Able to retrieve all Customers
    [Tags]    hqadm    distadm
    Given user retrieves token access as ${user_role}
    When user retrieves all cust
    Then expected return status code 200

3. Able to retrieve customer by id
    [Documentation]    Able to retrieve Customers by id
    [Tags]    hqadm    distadm
    Given user retrieves token access as ${user_role}
    When user retrieves all cust
    Then expected return status code 200

4. Able to retrieve customer contact list and details
    [Documentation]    Able to retrieve customer contact list and details
    [Tags]    hqadm    distadm     test
    [Setup]  run keywords
    ...    user retrieves token access as distadm
    ...    AND    user gets distributor by using code 'DistEgg'
    ...    AND    user retrieves cust by using name 'CXTESTTAX'
    Given user retrieves token access as ${user_role}
    When user retrieves all cust
    And user gets customer contacts
    Then expected return status code 200
    And user gets customer contacts details
    Then expected return status code 200

6. Able to retrieve customer invoice term list and details
    [Documentation]    Able to retrieve customer invoice term list and details
    [Tags]    hehehe1        hqadm    distadm
    [Teardown]  run keywords
    ...     user deletes created customer invoice term
    [Setup]  run keywords
    ...    user retrieves token access as distadm
    ...    AND    user gets distributor by using code 'DistEgg'
    ...    AND    user retrieves cust by using name 'CXTESTTAX'
    Given user retrieves token access as ${user_role}
    When user retrieves all cust
    And user creates customer invoice term
    Then expected return status code 200
    When user gets customer invoice term list
    And user gets customer invoice term details
    Then expected return status code 200

7. Able to retrieve customer open items
    [Documentation]    Able to retrieve customer open items
    [Tags]    hqadm    distadm
    [Setup]  run keywords
    ...    user retrieves token access as distadm
    ...    AND    user gets distributor by using code 'DistEgg'
    ...    AND    user retrieves cust by using name 'CXTESTTAX'
    Given user retrieves token access as ${user_role}
    When user retrieves all cust
    And user retrieve customer open items
    Then expected return status code 200

8. Able to retrieve customer order status
    [Documentation]    Able to retrieve customer order status
    [Tags]    hqadm    distadm
    [Setup]  run keywords
    ...    user retrieves token access as distadm
    ...    AND    user gets distributor by using code 'DistEgg'
    ...    AND    user retrieves cust by using name 'CXTESTTAX'
    Given user retrieves token access as ${user_role}
    When user retrieves all cust
    And user retrieve customer order status
    Then expected return status code 200

9. Able to retrieve customer license list and details
    [Documentation]    Able to retrieve customer license list and details
    [Tags]    hqadm    distadm
    [Setup]  run keywords
    ...    user retrieves token access as distadm
    ...    AND    user gets distributor by using code 'DistEgg'
    ...    AND    user retrieves cust by using name 'CXTESTTAX'
    Given user retrieves token access as ${user_role}
    When user retrieves all cust
    And user retrieve customer license
    Then expected return status code 200
    And user retrieve customer license details
    Then expected return status code 200

10. Able to retrieve customer posm listing and details
    [Documentation]    Able to retrieve customer posm listing and details
    [Tags]    hqadm    distadm
    [Setup]  run keywords
    ...    user retrieves token access as distadm
    ...    AND    user gets distributor by using code 'DistEgg'
    ...    AND    user retrieves cust by using name 'CXTESTTAX'
    Given user retrieves token access as ${user_role}
    When user retrieves all cust
    And user gets customer posm listing
    Then expected return status code 200

11. Able to retrieve trade asset listing
    [Documentation]    Able to retrieve trade asset listing
    [Tags]    hqadm    distadm
    [Setup]  run keywords
    ...    user retrieves token access as distadm
    ...    AND    user gets distributor by using code 'DistEgg'
    ...    AND    user retrieves cust by using name 'CXTESTTAX'
    Given user retrieves token access as ${user_role}
    When user gets customer trade asset listing
    Then expected return status code 200

12. Able to retrieve customer order status
    [Documentation]    Able to retrieve customer order status
    [Tags]    hqadm    distadm
    [Setup]  run keywords
    ...    user retrieves token access as distadm
    ...    AND    user gets distributor by using code 'DistEgg'
    ...    AND    user retrieves cust by using name 'CXTESTTAX'
    Given user retrieves token access as ${user_role}
    When user retrieve customer order status
    Then expected return status code 200
