*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/PosmManagement/PosmRemoval/PosmRemovalListPage.py

*** Test Cases ***
1 - Validate buttons on POSM Removal listing page for HQ Admin
    [Documentation]  To validate hq admin able to view add direct removal, process removal, reject, search and filter button on POSM Removal listing page
    [Tags]    hqadm    9.2
    Given user navigates to menu Merchandising | POSM Management | POSM Removal
    Then user validates buttons on posm removal listing page for hq admin

2 - Validate buttons on POSM Removal listing page for Distributor Admin
    [Documentation]  To validate distributor admin only able to view search and filter button on POSM Revmoval listing page
    [Tags]    distadm    9.2
    Given user navigates to menu Merchandising | POSM Management | POSM Removal
    Then user validates buttons on posm removal listing page for distributor