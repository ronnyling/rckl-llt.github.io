*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerApprovalPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerShipToDelete.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library           Collections

*** Test Cases ***
1. Able to approve created Customer
    [Documentation]    Able to approve Customer
    [Tags]    distadm
    ${App_Setup_details}=    create dictionary
    ...     NEWCUST_HQ_APPROVAL=${True}
    [Setup]  run keywords
    ...     user retrieves token access as hqadm
    ...     user retrieves details of application setup
    ...     user updates app setup details using fixed data
    [Teardown]  run keywords
    ...     user revert to previous setting
    ...     user retrieves token access as distadm
    ...     user deletes created customer data
    Given user retrieves token access as ${user_role}
    When user creates customer with random data
    And user assign hierarchy
    Then expected return status code 200
    When user retrieves token access as hqadm
    And user approves created customer
    Then expected return status code 200
