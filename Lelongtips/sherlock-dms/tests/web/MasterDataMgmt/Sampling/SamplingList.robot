*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Sampling/SamplingListPage.py

*** Test Cases ***
1 - Validate buttons on sampling listing page for HQ admin and distributor
    [Documentation]  To validate user able to view add and delete buttons on sampling listing page
    [Tags]    hqadm    distadm    9.2
    Given user navigates to menu Master Data Management | Sampling
    Then user validates buttons for sampling listing page

