*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supervisor/Objective/ObjectiveAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supervisor/Objective/ObjectiveListPage.py

*** Test Cases ***
1 - Able to Filter objective using given data
    [Documentation]    Able to filter objective using given data
    [Tags]     hqadm  9.2
    Given user navigates to menu Master Data Management | Supervisor | Objective
    When user creates objective with random data
    Then workplan create successfully with message 'Record created successfully'
    When user filters objective using created data
    Then objective record display in listing successfully
    When user selects objective to delete
    Then workplan delete successfully with message 'Record deleted'
