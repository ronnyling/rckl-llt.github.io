*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorShipToListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorShipToAddPage.py


*** Test Cases ***
1 - Able to create distributor ship to
    [Documentation]  To validate user able to create distributor ship to
    [Tags]    hqadm
    Given user navigates to menu Master Data Management | Distributor
    When user selects distributor to edit
    And user navigates to Ship To tab
    And user creates ship to using random data
    Then ship to created successfully with message 'Record created successfully'
    And user selects ship to to delete

