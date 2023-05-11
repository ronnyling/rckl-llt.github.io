*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/ProductSector/ProductSectorAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/ProductSector/ProductSectorListPage.py


*** Test Cases ***
1 - Able to delete product sector
    [Documentation]  To validate user able to delete product sector
    [Tags]    hqadm
    Given user navigates to menu Master Data Management | Product Sector
    When user creates product sector using random data
    And product sector created successfully with message 'New Product Sector Entry Added successfully'
    Then user selects product sector to delete


