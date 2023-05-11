*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/ProductSector/ProductSectorAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/ProductSector/ProductSectorListPage.py


*** Test Cases ***
1 - Validate buttons on product sector listing page
    [Documentation]  To validate user able to view add, delete, filter and search buttons on product sector listing page
    [Tags]    hqadm
    Given user navigates to menu Master Data Management | Product Sector
    Then user validates buttons for product sector listing page

