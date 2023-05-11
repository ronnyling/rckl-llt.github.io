*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supervisor/AuditCategory/AuditCategoryAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supervisor/AuditCategory/AuditCategoryListPage.py

*** Test Cases ***
1 - Able to filter audit category using given data
    [Documentation]    Able to filter audit category using given data
    [Tags]     hqadm  9.2
    Given user navigates to menu Master Data Management | Supervisor | Audit Category
    When user creates audit category with random data
    Then audit category create successfully with message 'Record created successfully'
    When user filters audit category using created data
    Then audit category record display in listing successfully
    When user selects audit category to delete
    Then audit category delete successfully with message 'Record deleted'
