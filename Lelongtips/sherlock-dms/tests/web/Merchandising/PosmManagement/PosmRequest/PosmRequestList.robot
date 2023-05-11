*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/PosmManagement/PosmRequest/PosmRequestListPage.py

*** Test Cases ***
1 - Validate buttons on POSM Requst listing page
    [Documentation]  To validate user able to view add new request, search and filter button on POSM Request listing page
    [Tags]    hqadm    distadm    9.2
    Given user navigates to menu Merchandising | POSM Management | POSM Request
    Then user validates buttons on posm request listing page

