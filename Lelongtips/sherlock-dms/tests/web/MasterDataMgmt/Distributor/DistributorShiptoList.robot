*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorShipToListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorShipToAddPage.py


*** Test Cases ***
1 - Validate buttons on distributor ship to listing page
    [Documentation]  To validate buttons on distributor ship to listing page
    [Tags]    hqadm
    Given user navigates to menu Master Data Management | Distributor
    When user selects distributor to edit
    And user navigates to Ship To tab
    Then user validates buttons for ship to listing page
