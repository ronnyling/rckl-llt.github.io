*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerPost.py
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
1. Able to delete Customer using sysimp
    [Documentation]    Able to delete Customer created by distadm using sysimp
    [Tags]      distadm
    [Teardown]  run keywords
    ...     user retrieves token access as distadm
    ...     AND     user gets distributor by using code 'DistEgg'
    ...     AND     user deletes created customer data
    Given user retrieves token access as ${user_role}
    When user creates customer with random data
    Then expected return status code 200
    When user retrieves token access as sysimp
    And user deletes created customer data
    Then expected return status code 403

2. Able to delete Customer created by distadm
    [Documentation]    Able to delete Customer created by distadm
    [Tags]      distadm
    [Teardown]  user deletes created customer data
    Given user retrieves token access as ${user_role}
    When user creates customer with random data
    Then expected return status code 200
    When user deletes created customer data
    Then expected return status code 200

3. Able to delete created Customer invoice term
    [Documentation]    Able to delete created Customer invoice term
    [Tags]    distadm
    [Teardown]  user deletes created customer data
    Given user retrieves token access as ${user_role}
    When user creates customer with random data
    Then expected return status code 200
    When user creates customer invoice term
    And user deletes created customer invoice term
    Then expected return status code 200
