*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supplier/SupplierPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supplier/SupplierGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supplier/SupplierDelete.py


*** Test Cases ***
1 - Able to retrieve all Supplier
    [Documentation]    To retrieve all supplier via API
    [Tags]     distadm     9.0
    Given user retrieves token access as ${user_role}
    When user retrieves all supplier
    Then expected return status code 200

2 - Able to retrieve specific supplier using id
    [Documentation]    To retrieve supplier using given id via API
    [Tags]     distadm     9.0
    [Teardown]   run keywords
    ...    user deletes supplier
    Given user retrieves token access as ${user_role}
    And user creates supplier with random data
    When user retrieves supplier by id
    Then expected return status code 200
