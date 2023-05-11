*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PriceGroup/PriceGroupListPage.py


*** Test Cases ***
1 - Validate buttons on price group listing page
    [Documentation]  To validate user able to view add, delete, filter and search buttons on price group listing page
    [Tags]    hqadm
    Given user navigates to menu Master Data Management | Price Group
    Then user validates buttons for price group listing page

