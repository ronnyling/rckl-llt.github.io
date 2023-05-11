*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supervisor/AuditCategory/AuditCategoryAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supervisor/AuditCategory/AuditCategoryListPage.py

*** Test Cases ***
1 - Able to Create Audit Category using random data
    [Documentation]    Able to create audit category using given data
    [Tags]     hqadm   9.2
    Given user navigates to menu Master Data Management | Supervisor | Audit Category
    When user creates audit category with random data
    Then audit category create successfully with message 'Record created successfully'
    When user selects audit category to delete
    Then audit category delete successfully with message 'Record deleted'

2 - Able to delete created Audit Category
    [Documentation]    Able to delete audit category using given data
    [Tags]     hqadm   9.2
    Given user navigates to menu Master Data Management | Supervisor | Audit Category
    When user creates audit category with random data
    Then audit category create successfully with message 'Record created successfully'
    When user selects audit category to delete
    Then audit category delete successfully with message 'Record deleted'

3 - Able to edit created Audit Category
    [Documentation]    Able to edit created audit category
    [Tags]     hqadm   9.2
    Given user navigates to menu Master Data Management | Supervisor | Audit Category
    When user creates audit category with random data
    Then audit category create successfully with message 'Record created successfully'
    When user selects audit category to edit
    And user edits audit category desc into EDITEDACDESC
    Then audit category updated successfully with message 'Record updated successfully'
    When user selects audit category to delete
    Then audit category delete successfully with message 'Record deleted'

4 - Unable to save audit category code with empty code and desc
    [Documentation]    Unable to save audit category without enter code and desc
    [Tags]     hqadm   9.2
    Given user navigates to menu Master Data Management | Supervisor | Audit Category
    When user lands on audit category add mode
    And user save audit category
    Then user validated audit category fields is mandatory

5 - Unable to edit Audit Category Code
    [Documentation]    Unable to edit audit category code
    [Tags]     hqadm   9.2
    Given user navigates to menu Master Data Management | Supervisor | Audit Category
    When user creates audit category with random data
    Then audit category create successfully with message 'Record created successfully'
    When user selects audit category to edit
    Then verifies text field Audit Category Code is disabled
    And user back to listing page
    When user selects audit category to delete
    Then audit category delete successfully with message 'Record deleted'