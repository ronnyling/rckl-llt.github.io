*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorTrxNumListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorTrxNumAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py


*** Test Cases ***
1 - Validate buttons on distributor ship to listing page
    [Documentation]  To validate buttons on distributor ship to listing page
    [Tags]    distadm
    Given user navigates to menu Master Data Management | Distributor
    When user selects distributor to edit
    And user navigates to Distributor Transaction Number tab
    Then user validates buttons for distributor transaction number listing page