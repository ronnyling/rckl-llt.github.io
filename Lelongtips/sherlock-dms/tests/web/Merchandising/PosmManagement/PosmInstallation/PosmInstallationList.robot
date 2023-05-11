*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/PosmManagement/PosmInstallation/PosmInstallationListPage.py

*** Test Cases ***
1 - Validate buttons on POSM Installation listing page for HQ Admin
    [Documentation]  To validate hq admin able to view add new installation, process installation, reject, search and filter button on POSM Installation listing page
    [Tags]    hqadm    9.2
    Given user navigates to menu Merchandising | POSM Management | POSM Installation
    Then user validates buttons on posm installation listing page for hq admin

2 - Validate buttons on POSM Installation listing page for Distributor Admin
    [Documentation]  To validate distributor admin only able to view search and filter button on POSM Installation listing page
    [Tags]    distadm    9.2
    Given user navigates to menu Merchandising | POSM Management | POSM Installation
    Then user validates buttons on posm installation listing page for distributor