*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerShipToPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerShipToDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library           Collections

*** Test Cases ***
1. Able to delete customer shipto details
    [Documentation]    Able to post customer shipto details
    [Tags]        hqadm    distadm
    [Setup]  run keywords
    ...    user retrieves token access as distadm
    ...    AND    user gets distributor by using code 'DistEgg'
    ...    AND    user retrieves cust by using name 'CXTESTTAX'
    Given user retrieves token access as ${user_role}
    When user retrieves all cust
    Then user creates customer shipto
    When user deletes ship to details
    Then expected return status code 200
