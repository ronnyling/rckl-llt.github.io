*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorProductSectorListPage.py


*** Test Cases ***
1 - Validate buttons on distributor product sector mapping listing page
    [Documentation]  To Validate buttons on distributor product sector mapping listing page
    [Tags]    hqadm
    Given user navigates to menu Master Data Management | Distributor
    When user selects distributor to edit
    And user navigates to Product Sector Distributor Mapping tab
    Then user validates buttons for product sector mapping listing page


