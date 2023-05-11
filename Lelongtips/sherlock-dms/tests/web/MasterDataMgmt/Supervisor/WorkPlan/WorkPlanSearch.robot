*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supervisor/WorkPlan/WorkPlanAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supervisor/WorkPlan/WorkPlanListPage.py


*** Test Cases ***
1 - Able to search created work plan
    [Documentation]    Able to search created work plan
    [Tags]     hqadm  9.2
   Given user navigates to menu Master Data Management | Supervisor | Work Plan Item
    When user creates work plan with random data
    Then workplan create successfully with message 'Record created successfully'
    When user searches work plan using created data
    Then work plan record display in listing successfully
    When user selects work plan to delete
    Then workplan delete successfully with message 'Record deleted'