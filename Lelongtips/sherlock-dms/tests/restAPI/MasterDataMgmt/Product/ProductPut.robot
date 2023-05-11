*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductDelete.py

*** Test Cases ***
1 - Able to update product using random data
    [Documentation]    To update product using random data via API
    [Tags]     hqadm
    [Setup]    run keywords
    ...     user creates random product as prerequisite
    Given user retrieves token access as ${user_role}
    ${update_product_details} =   create dictionary
    ...    PRD_TAX_GRP=${None}
    ...    PRD_TAX=0
    When user updates product with random data
    Then expected return status code 200

2 - Able to update product using fixed data
    [Documentation]    To update product using random data via API
    [Tags]     hqadm
    [Setup]    run keywords
    ...     user creates random product as prerequisite
    ${update_product_details}=    create dictionary
    ...    PRD_DESC=YourProduct
    ...    PRD_TAX_GRP=${None}
    ...    PRD_TAX=0
    Given user retrieves token access as ${user_role}
    When user updates product with fixed data
    Then expected return status code 200
