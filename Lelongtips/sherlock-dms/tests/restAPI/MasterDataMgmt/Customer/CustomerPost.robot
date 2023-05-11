*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerShipToDelete.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py
Library           Collections

Test Setup        run keywords
...               user retrieves token access as distadm
...               AND    user gets distributor by using code 'DistEgg'

*** Test Cases ***
1 - Able to post Customer with random data
    [Documentation]    Able to post Customer with random data
    [Tags]    distadm   BUG:NRSZUANQ-52085
    [Teardown]  user deletes created customer data
    Given user retrieves token access as ${user_role}
    When user creates customer with random data
    Then expected return status code 200
    When user assign hierarchy
    Then expected return status code 200

2. Able to post Customer contacts
    [Documentation]    Able to post Customer contacts
    [Tags]    dingding      distadm
    [Teardown]  user deletes created customer data
    Given user retrieves token access as ${user_role}
    When user creates customer with random data
    Then expected return status code 200
    When user create customer contacts
    Then expected return status code 200

3. Able to post Customer invoice term
    [Documentation]    Able to post Customer invoice term
    [Tags]    distadm
    [Teardown]  user deletes created customer data
    Given user retrieves token access as ${user_role}
    When user creates customer with random data
    Then expected return status code 200
    When user creates customer invoice term
    Then expected return status code 200

