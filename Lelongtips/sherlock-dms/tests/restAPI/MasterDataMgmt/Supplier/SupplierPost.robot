*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supplier/SupplierPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supplier/SupplierDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Country/CountryPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/State/StatePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Locality/LocalityPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Country/CountryDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/State/StateDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Locality/LocalityDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxGroup/TaxGroupGet.py
Library           Collections


*** Test Cases ***
1 - Able to post Supplier with random data
    [Documentation]    Able to post Supplier with random data
    [Tags]    distadm     9.0
    [Teardown]  user deletes supplier
    Given user retrieves token access as ${user_role}
    When user creates supplier with random data
    Then expected return status code 201
