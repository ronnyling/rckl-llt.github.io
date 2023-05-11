*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerPut.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerDelete.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py
Library           Collections

Test Setup        run keywords
...               user retrieves token access as distadm
...               AND    user gets distributor by using code 'DistEgg'

*** Test Cases ***
1 - Able to PUT customer data using customer ID
    [Documentation]    Able to edit Customer's data
    [Tags]       distadm
    Given user retrieves token access as ${user_role}
    When user retrieves random cust
    And user puts customer data
    Then expected return status code 200

