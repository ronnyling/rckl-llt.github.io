*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerShipToPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerShipToGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerShipToDelete.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py

Library           Collections

*** Test Cases ***
1 - Able to update Customer ship to details
    [Documentation]    Able to update Customer ship to details
    [Tags]    distadm
    Given user retrieves token access as ${user_role}
    Then user retrieves random cust
    When user retrieves random ship to
    And user retrieves ship to details
    Then expected return status code 200

2. Able to retrieve customer shipto list and details
    [Documentation]    Able to retrieve customer shipto list and details
    [Tags]        hqadm    distadm
    [Teardown]  run keywords
    ...     user deletes ship to details
    [Setup]  run keywords
    ...    user retrieves token access as distadm
    ...    AND    user gets distributor by using code 'DistEgg'
    ...    AND    user retrieves cust by using name 'CXTESTTAX'
    Given user retrieves token access as ${user_role}
    When user retrieves all cust
    And user creates customer shipto
    Then expected return status code 200
    When user gets customer shipto all
    Then expected return status code 200
    And user gets customer shipto details
    Then expected return status code 200