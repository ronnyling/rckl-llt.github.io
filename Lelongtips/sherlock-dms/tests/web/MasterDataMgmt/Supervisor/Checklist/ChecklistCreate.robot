*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supervisor/Checklist/ChecklistAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supervisor/Checklist/ChecklistListPage.py

*** Test Cases ***
1-Able to save checklist setup
    [Documentation]    Able to create checklist
    [Tags]     hqadm   9.2     NRSZUANQ-47925
    Given user navigates to menu Master Data Management | Supervisor | Checklist
    When user creates checklist with random data
    Then checklist create successfully with message 'Record created successfully'
    When user validate created checklist is listed in the table and select to delete
    Then checklist delete successfully with message 'Record deleted'
    
2-Unable to save checklist setup without checklist item
    [Documentation]    Unable to create checklist without checklist item
    [Tags]     hqadm   9.2     NRSZUANQ-47926
    Given user navigates to menu Master Data Management | Supervisor | Checklist
    When user creates checklist with no checklist data
    Then expect pop up message: Add a Checklist Item to proceed

3-Unable to save checklist setup without workplan item
    [Documentation]    Unable to create checklist without workplan item
    [Tags]     hqadm   9.2     NRSZUANQ-47927
    Given user navigates to menu Master Data Management | Supervisor | Checklist
    When user creates checklist with no workplan data
    Then expect pop up message: Bad Request : Each Checklist must be tagged to atleast one Work Plan Item
    




    
    



