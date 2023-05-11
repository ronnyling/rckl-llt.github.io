*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerShipToPut.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerShipToPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerShipToDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerShipToGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py


Library           Collections

*** Test Cases ***
1. Able to PUT customer shipto details
    [Documentation]    Able to put customer shipto details
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
    When user puts customer shipto
    Then expected return status code 200


