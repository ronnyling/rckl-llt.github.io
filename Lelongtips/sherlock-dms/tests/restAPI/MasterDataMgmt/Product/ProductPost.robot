*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxGroup/TaxGroupGet.py

Test Setup     run keywords
...    user retrieves token access as hqadm
...    AND     user get random tax group by PRIME principal flag
...    AND     user retrieves token access as distadm
...    AND     user get random tax group by NON_PRIME principal flag
Test Teardown     user deletes product

*** Test Cases ***
1 - Able to post product with random data
    [Documentation]    Able to post prime product with random data
    [Tags]    hqadm
    Given user retrieves token access as ${user_role}
    When user creates product with random data using ${user_role}
    Then expected return status code 201

2. Able to post product with fixed data
    [Documentation]    Able to post product with fixed data
    [Tags]    distadm
    ${product_details}=     create dictionary
    ...    PRD_DESC=MyProduct
    Given user retrieves token access as ${user_role}
    When user creates product with random data using ${user_role}
    Then expected return status code 201