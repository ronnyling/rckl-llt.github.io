*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Product/ProductAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Product/ProductListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Product/ProductUomListPage.py


*** Test Cases ***
1 - Validate buttons on product uom listing page
    [Documentation]  To validate user able to view add, delete, filter and search buttons on product uom listing page
    [Tags]    hqadm
    Given user navigates to menu Master Data Management | Product
    When user creates product with random data
    Then product created successfully with message 'Record created'
    When user back to listing page
    And user selects product to edit
    Then user validates buttons for product uom listing page
    When user back to listing page
    Then user selects product to delete

