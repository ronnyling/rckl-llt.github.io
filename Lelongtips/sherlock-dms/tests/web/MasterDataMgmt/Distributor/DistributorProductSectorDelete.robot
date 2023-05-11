*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorProductSectorListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorProductSectorAddPage.py


*** Test Cases ***
1 - Able to delete assigned product sector
    [Documentation]  To validate user able to delete assigned product sector
    [Tags]    hqadm
    Given user navigates to menu Master Data Management | Distributor
    When user selects distributor to edit
    And user navigates to Product Sector Distributor Mapping tab
    And user assigns product sector using random data
    Then user selects product sector to delete

