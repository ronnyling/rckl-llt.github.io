*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supervisor/Checklist/ChecklistAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supervisor/Checklist/ChecklistListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supervisor/Checklist/ChecklistUpdatePage.py

Test Teardown   run keywords
...    user validate created checklist is listed in the table and select to delete
...    AND     checklist deleted successfully with message 'Record deleted'
...    AND     user logouts and closes browser
*** Test Cases ***
1-Able to filter existing checklist
    [Documentation]    To ensure user able to filter principal in supplier
    [Tags]   hqadm    9.2   NRSZUANQ-47867      test
    Given user navigates to menu Master Data Management | Supervisor | Checklist
    When user creates checklist with random data
    Then checklist created successfully with message 'Record created successfully'
    When user filters created checklist in listing page
    Then record display in listing successfully

2-Able to search existing checklist
    [Documentation]    To test user is able to search existing checklist
    [Tags]   hqadm   9.2   NRSZUANQ-47866      test
    Given user navigates to menu Master Data Management | Supervisor | Checklist
    When user creates checklist with random data
    Then checklist created successfully with message 'Record created successfully'
    When user searches created checklist in listing page
    Then record display in listing successfully

