*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Product/ProductAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Product/ProductListPage.py

*** Test Cases ***
1 - Able to search created product
    [Documentation]    Able to search created product by using inline filter
    [Tags]    hqadm
    Given user navigates to menu Master Data Management | Product
    When user creates product with random data
    Then product created successfully with message 'Record created'
    And user back to listing page
    When user searches product using created data
    Then product record display in listing successfully
    When user selects product to delete
    Then product delete successfully with message 'Record deleted'

2 - Able to filter created product
    [Documentation]    Able to filter created product by using filter
    [Tags]    hqadm
    Given user navigates to menu Master Data Management | Product
    When user creates product with random data
    Then product created successfully with message 'Record created'
    And user back to listing page
    When user filters product using random data
    Then product record display in listing successfully
    When user selects product to delete
    Then product delete successfully with message 'Record deleted'
