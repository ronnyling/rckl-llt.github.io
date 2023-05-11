*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supervisor/Checklist/ChecklistAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supervisor/Checklist/ChecklistListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supervisor/Checklist/ChecklistUpdatePage.py
*** Test Cases ***

1-Unable to update checklist code in Edit Page
    [Documentation]    To validate checklist code cannot be updated
    [Tags]   hqadm    9.2   NRSZUANQ-47946
    Given user navigates to menu Master Data Management | Supervisor | Checklist
    When user creates checklist with random data
    Then checklist create successfully with message 'Record created successfully'
    When user validate created checklist is listed in the table and select to edit
    Then validate checklist code is disabled

2-Unable to update checklist type in Edit Page
    [Documentation]    To validate checklist type cannot be updated
    [Tags]   hqadm    9.2   NRSZUANQ-47947     test
    Given user navigates to menu Master Data Management | Supervisor | Checklist
    When user creates checklist with random data
    Then checklist create successfully with message 'Record created successfully'
    When user validate created checklist is listed in the table and select to edit
    Then validate checklist type is disabled


