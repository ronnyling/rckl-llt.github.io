*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductDelete.py

Test Teardown   user deletes product

*** Test Cases ***
1 - Able to retrieve all product
    [Documentation]    To retrieve all product via API
    [Tags]     distadm
    [Setup]    user creates random product as prerequisite
    Given user retrieves token access as ${user_role}
    When user retrieves all products
    Then expected return status code 200
    When user retrieves all product list
    Then expected return status code 200

2 - Able to retrieve specific product using id
    [Documentation]    To retrieve product using given id via API
    [Tags]     distadm
    [Setup]    user creates random product as prerequisite
    Given user retrieves token access as ${user_role}
    When user retrieves product by id
    Then expected return status code 200

3 - Able to retrieve product detilas
    [Documentation]    To retrieve product details via api
    [Tags]       distadm
    Given user retrieves token access as ${user_role}
    When user retrieves random product details
    Then expected return status code 200
