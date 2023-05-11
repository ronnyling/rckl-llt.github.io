*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supervisor/WorkPlan/WorkPlanAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supervisor/WorkPlan/WorkPlanListPage.py

*** Test Cases ***
1 - Able to Create Work Plan using random data
    [Documentation]    Able to create work plan using given data
    [Tags]     hqadm   9.2
    Given user navigates to menu Master Data Management | Supervisor | Work Plan Item
    When user creates work plan with random data
    Then workplan create successfully with message 'Record created successfully'
    When user selects work plan to delete
    Then workplan delete successfully with message 'Record deleted'

2 - Able to delete created Work Plan
    [Documentation]    Able to delete created work plan
    [Tags]     hqadm   9.2
    Given user navigates to menu Master Data Management | Supervisor | Work Plan Item
    When user creates work plan with random data
    Then workplan create successfully with message 'Record created successfully'
    When user selects work plan to delete
    Then workplan delete successfully with message 'Record deleted'

3 - Able to edit created Work Plan
    [Documentation]    Able to edit work plan using given data
    [Tags]     hqadm   9.2
    Given user navigates to menu Master Data Management | Supervisor | Work Plan Item
    When user creates work plan with random data
    Then workplan create successfully with message 'Record created successfully'
    When user selects work plan to edit
    And user edits work plan desc into EDITEDWORKPLANDESC
    Then workplan updated successfully with message 'Record updated successfully'
    When user selects work plan to delete
    Then workplan delete successfully with message 'Record deleted'

4 - Unable to save work plan code with empty code and desc
    [Documentation]    Unable to save work plan code with empty code and desc
    [Tags]     hqadm   9.2
    Given user navigates to menu Master Data Management | Supervisor | Work Plan Item
    When user lands on work plan add mode
    And user save work plan
    Then user validated work plan fields is mandatory

5 - Unable to edit Work Plan Code
    [Documentation]    Unable to edit Work Plan Code
    [Tags]     hqadm   9.2
    Given user navigates to menu Master Data Management | Supervisor | Work Plan Item
    When user creates work plan with random data
    Then workplan created successfully with message 'Record created successfully'
    When user selects work plan to edit
    Then verifies text field Work Plan Item Code is disabled
    And user back to listing page
    When user selects work plan to delete
    Then workplan delete successfully with message 'Record deleted'