*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorTrxNumListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorTrxNumAddPage.py

*** Test Cases ***
1 - Able to delete Distributor Transaction number
    [Documentation]    Able to delete Distributor transaction number using created data
    [Tags]    distadm   9.0    9.1   NRSZUANQ-30005    NRSZUANQ-30006
    Given user navigates to menu Master Data Management | Distributor
    When user selects distributor to edit
    And user creates distributor transaction number with random data
    Then distributor transaction number created successfully with message 'Record created'
    When user selects distributor transaction number to delete
    Then distributor transaction number deleted successfully with message 'Record deleted'
