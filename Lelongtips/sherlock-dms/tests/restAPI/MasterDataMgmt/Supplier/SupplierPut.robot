*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supplier/SupplierPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supplier/SupplierGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supplier/SupplierPut.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supplier/SupplierDelete.py


*** Test Cases ***
#1 - Able to update Supplier using random data
#    [Documentation]    To update Supplier using random data via API
#    [Tags]     hehehe       distadm     9.0
#    Given user retrieves token access as ${user_role}
#    When user updates supplier with random data
#    Then expected return status code 200

2 - Able to update Supplier using fixed data
    [Documentation]    To update Supplier using fixed data via API
    [Tags]     distadm     9.0
    [Teardown]  user deletes supplier
    ${update_supplier_details}=    create dictionary
    ...    SUPP_NAME= YourName
    Given user retrieves token access as ${user_role}
    Then user creates supplier with random data
    When user retrieves supplier by id
    And user updates supplier details
    Then expected return status code 200
