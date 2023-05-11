*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductUomGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductUomPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxGroup/TaxGroupGet.py

Test Setup     run keywords
...    user retrieves token access as hqadm
...    AND     user get random tax group by PRIME principal flag
...    AND     user retrieves token access as distadm
...    AND     user get random tax group by NON_PRIME principal flag
Test Teardown     user deletes product

*** Test Cases ***
1 - Able to GET all product uom
    [Documentation]    Able to get all product uom
    [Tags]    hqadm
    Given user retrieves token access as ${user_role}
    When user creates product with random data using ${user_role}
    Then expected return status code 201
    When user creates product uom with random data
    Then expected return status code 200
    When user retrieves all product uom
    Then expected return status code 200

2 - Able to retrieve uom details of product
    [Documentation]    Able to retrieve uom details of product
    [Tags]        distadm
    Given user retrieves token access as ${user_role}
    When user retrieves random product details
    Then expected return status code 200
    When user retrieves previous prd uom
    And user retrieves uom details of product
    Then expected return status code 200


