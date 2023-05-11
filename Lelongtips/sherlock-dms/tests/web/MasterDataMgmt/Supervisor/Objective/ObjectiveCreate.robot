*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supervisor/Objective/ObjectiveAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supervisor/Objective/ObjectiveListPage.py

*** Test Cases ***
1 - Able to Create Objective using random data
    [Documentation]    Able to create Objective using given data
    [Tags]     hqadm   9.2    asdasdsasdzxcadasd
    Given user navigates to menu Master Data Management | Supervisor | Objective
    When user creates objective with random data
    Then objective create successfully with message 'Record created successfully'
    When user selects objective to delete
    Then objective delete successfully with message 'Record deleted'

2 - Able to delete created Objective
    [Documentation]    Able to delete Objective using given data
    [Tags]     hqadm   9.2
    Given user navigates to menu Master Data Management | Supervisor | Objective
    When user creates objective with random data
    Then objective create successfully with message 'Record created successfully'
    When user selects objective to delete
    Then objective delete successfully with message 'Record deleted'

3 - Able to edit created Objective
    [Documentation]    Able to edit Objective using given data
    [Tags]     hqadm   9.2
    Given user navigates to menu Master Data Management | Supervisor | Objective
    When user creates objective with random data
    Then objective create successfully with message 'Record created successfully'
    When user selects objective to edit
    And user edits objective desc into EDITEDObjNDESC
    Then objective updated successfully with message 'Record updated successfully'
    When user selects objective to delete
    Then objective delete successfully with message 'Record deleted'

4 - Unable to save Objective code with empty code and desc
    [Documentation]    Unable to save Objective code with empty code and desc
    [Tags]     hqadm   9.2
    Given user navigates to menu Master Data Management | Supervisor | Objective
    When user lands on objective add mode
    And user save objective
    Then user validated objective fields is mandatory

5 - Unable to edit Objective Code
    [Documentation]    Unable to edit Objective Code
    [Tags]     hqadm   9.2
    Given user navigates to menu Master Data Management | Supervisor | Objective
    When user creates Objective with random data
    Then objective create successfully with message 'Record created successfully'
    When user selects Objective to edit
    Then verifies text field Objective Item Code is disabled
    And user back to listing page
    When user selects Objective to delete
    Then objective delete successfully with message 'Record deleted'