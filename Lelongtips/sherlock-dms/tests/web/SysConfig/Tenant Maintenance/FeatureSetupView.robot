*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/SysConfig/TenantMaintenance/FeatureSetup/FeatureSetupListPage.py

*** Test Cases ***
1 - Able to view feature setup for Claim
    [Documentation]    Able to view feature setup for claim
    [Tags]    sysimp    9.3
    When user navigates to menu System Configuration | Tenant Maintenance | Feature Setup
    And user selects Claim setup to view
    Then selected feature setup is displayed successfully

2 - Able to view feature setup for Customer Group
    [Documentation]    Able to view feature setup for customer group
    [Tags]    sysimp    9.3
    When user navigates to menu System Configuration | Tenant Maintenance | Feature Setup
    And user selects Customer Group Discount setup to view
    Then Customer Group Discount setup is displayed successfully

3 - Able to view feature setup for Delivery App
    [Documentation]    Able to view feature setup for delivery app
    [Tags]    sysimp    9.3
    When user navigates to menu System Configuration | Tenant Maintenance | Feature Setup
    And user selects Delivery App setup to view
    Then selected feature setup is displayed successfully

4 - Able to view feature setup for Digital Playbook
    [Documentation]    Able to view feature setup for digital playbook
    [Tags]    sysimp    9.3
    When user navigates to menu System Configuration | Tenant Maintenance | Feature Setup
    And user selects Digital Playbook setup to view
    Then selected feature setup is displayed successfully

5 - Able to view feature setup for Merchandising
    [Documentation]    Able to view feature setup for merchandising
    [Tags]    sysimp    9.3     test
    When user navigates to menu System Configuration | Tenant Maintenance | Feature Setup
    And user selects Merchandising setup to view
    Then selected feature setup is displayed successfully

6 - Able to view feature setup for Sampling
    [Documentation]    Able to view feature setup for sampling
    [Tags]    sysimp    9.3
    When user navigates to menu System Configuration | Tenant Maintenance | Feature Setup
    And user selects Sampling setup to view
    Then selected feature setup is displayed successfully

7 - Able to view feature setup for Supervisor
    [Documentation]    Able to view feature setup for supervisor
    [Tags]    sysimp    9.3
    When user navigates to menu System Configuration | Tenant Maintenance | Feature Setup
    And user selects Supervisor setup to view
    Then selected feature setup is displayed successfully

8 - Able to view feature setup for Trade Asset
    [Documentation]    Able to view feature setup for trade asset
    [Tags]    sysimp    9.3
    When user navigates to menu System Configuration | Tenant Maintenance | Feature Setup
    And user selects Trade Asset setup to view
    Then selected feature setup is displayed successfully

9 - Able to view feature setup for Trade Program
    [Documentation]    Able to view feature setup for trade program
    [Tags]    sysimp    9.3
    When user navigates to menu System Configuration | Tenant Maintenance | Feature Setup
    And user selects Trade Program setup to view
    Then selected feature setup is displayed successfully