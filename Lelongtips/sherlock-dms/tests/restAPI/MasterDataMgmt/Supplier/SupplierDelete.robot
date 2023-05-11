*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supplier/SupplierPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supplier/SupplierDelete.py

*** Test Cases ***
1 - Able to delete created Supplier
    [Documentation]    To delete created supplier via API
    [Tags]     distadm     9.0
    Given user retrieves token access as ${user_role}
    When user creates supplier with random data
    And user deletes supplier
    Then expected return status code 200
