*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Product/ProductAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Product/ProductListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Product/ProductUomListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Product/ProductUomAddPage.py


*** Test Cases ***
1 - Able to delete product uom
    [Documentation]  To validate user able to delete product uom
    [Tags]    hqadm
    Given user navigates to menu Master Data Management | Product
    When user creates product with random data
    Then product created successfully with message 'Record created'
    When user back to listing page
    And user selects product to edit
    And user creates product uom using random data
    Then product uom created successfully with message 'Record created successfully'
    When user selects product uom to delete
    Then product uom created successfully with message 'Record deleted'
    When user back to listing page
    Then user selects product to delete
