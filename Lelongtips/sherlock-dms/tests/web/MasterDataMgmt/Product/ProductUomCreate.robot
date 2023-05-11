*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Product/ProductAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Product/ProductListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Product/ProductUomListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Product/ProductUomAddPage.py


*** Test Cases ***
1 - Able to create product uom
    [Documentation]  To validate user able to create product uom
    [Tags]    hqadm
    Given user navigates to menu Master Data Management | Product
    When user creates product with random data
    Then product created successfully with message 'Record created'
    When user back to listing page
    And user selects product to edit
    Then user creates product uom using random data
    Then product uom created successfully with message 'Record created successfully'
    When user back to listing page
    Then user selects product to delete

