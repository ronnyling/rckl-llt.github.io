*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supervisor/AuditCategory/AuditCategoryAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supervisor/AuditCategory/AuditCategoryListPage.py


*** Test Cases ***
1 - Able to search created audit category with inline search
    [Documentation]    Able to search created audit category with inline search
    [Tags]     hqadm  9.2
   Given user navigates to menu Master Data Management | Supervisor | Audit Category
    When user creates work plan with random data
    Then audit category create successfully with message 'Record created successfully'
    When user searches work plan using created data
    Then audit category record display in listing successfully
    When user selects work plan to delete
    Then audit category delete successfully with message 'Record deleted'