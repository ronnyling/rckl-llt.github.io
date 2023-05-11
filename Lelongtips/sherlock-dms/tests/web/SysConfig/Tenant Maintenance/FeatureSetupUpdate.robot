*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/SysConfig/TenantMaintenance/FeatureSetup/FeatureSetupListPage.py
Library         ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py

*** Test Cases ***
1 - Able to update feature setup for Claim
    [Documentation]    Able to update feature setup for claim
    [Tags]    sysimp    9.3
    [Setup]      run keywords
    ...    user sets the feature setup for sampling to off passing with 'CLAIM' value
    ...    AND    user open browser and logins using user role ${user_role}
    Given user navigates to menu System Configuration | Tenant Maintenance | Feature Setup
    ${setup_status}=   create dictionary
    ...    feature=${True}
    set test variable     &{setup_status}
    ${setup_details}=   create dictionary
    ...    visible=${True}
    ...    enabled=${True}
    set test variable     &{setup_details}
    When user selects Claim setup to update
    And user updates Claim setup
    And user updates the feature setup details
    Then feature setup updated successfully with message 'Record added.'

2 - Able to update feature setup for Customer Group Discount
    [Documentation]    Able to update feature setup for customer group
    [Tags]    sysimp    9.3
    [Setup]      run keywords
    ...    user sets the feature setup for sampling to off passing with 'CUST_GRP_DISC' value
    ...    AND    user open browser and logins using user role ${user_role}
    Given user navigates to menu System Configuration | Tenant Maintenance | Feature Setup
    ${setup_status}=   create dictionary
    ...    feature=${True}
    set test variable     &{setup_status}
    ${setup_details}=   create dictionary
    ...    visible=${True}
    ...    enabled=${True}
    set test variable     &{setup_details}
    When user selects Customer Group Discount setup to update
    And user updates Customer Group Discount setup
    And user updates the feature setup details
    Then feature setup updated successfully with message 'Record added.'

3 - Able to update feature setup for Delivery App
    [Documentation]    Able to update feature setup for delivery app
    [Tags]    sysimp    9.3
    [Setup]      run keywords
    ...    user sets the feature setup for sampling to off passing with 'DELIVERY_APP' value
    ...    AND    user open browser and logins using user role ${user_role}
    Given user navigates to menu System Configuration | Tenant Maintenance | Feature Setup
    ${setup_status}=   create dictionary
    ...    feature=${True}
    set test variable     &{setup_status}
    ${setup_details}=   create dictionary
    ...    visible=${True}
    ...    enabled=${True}
    set test variable     &{setup_details}
    When user selects Delivery App setup to update
    And user updates Delivery App setup
    And user updates the feature setup details
    Then feature setup updated successfully with message 'Record added.'

4 - Able to update feature setup for Digital Playbook
    [Documentation]    Able to update feature setup for digital playbook
    [Tags]    sysimp    9.3
    [Setup]      run keywords
    ...    user sets the feature setup for sampling to off passing with 'PLAYBK' value
    ...    AND    user open browser and logins using user role ${user_role}
    Given user navigates to menu System Configuration | Tenant Maintenance | Feature Setup
    ${setup_status}=   create dictionary
    ...    feature=${True}
    set test variable     &{setup_status}
    ${setup_details}=   create dictionary
    ...    visible=${True}
    ...    enabled=${True}
    set test variable     &{setup_details}
    When user selects Digital Playbook setup to update
    And user updates Digital Playbook setup
    And user updates the feature setup details
    Then feature setup updated successfully with message 'Record added.'

5 - Able to update feature setup for Merchandising
    [Documentation]    Able to update feature setup for merchandising
    [Tags]    sysimp    9.3
    [Setup]      run keywords
    ...    user sets the feature setup for sampling to off passing with 'MDSE' value
    ...    AND    user open browser and logins using user role ${user_role}
    Given user navigates to menu System Configuration | Tenant Maintenance | Feature Setup
    ${setup_status}=   create dictionary
    ...    feature=${True}
    set test variable     &{setup_status}
    ${setup_details}=   create dictionary
    ...    visible=${True}
    ...    enabled=${True}
    set test variable     &{setup_details}
    When user selects Merchandising setup to update
    And user updates Merchandising setup
    And user updates the feature setup details
    Then feature setup updated successfully with message 'Record added.'

6 - Able to update feature setup for Sampling
    [Documentation]    Able to update feature setup for sampling
    [Tags]    sysimp    9.3
    [Setup]      run keywords
    ...    user sets the feature setup for sampling to off passing with 'SAMPLING' value
    ...    AND    user open browser and logins using user role ${user_role}
    Given user navigates to menu System Configuration | Tenant Maintenance | Feature Setup
    ${setup_status}=   create dictionary
    ...    feature=${True}
    set test variable     &{setup_status}
    ${setup_details}=   create dictionary
    ...    visible=${True}
    ...    enabled=${True}
    set test variable     &{setup_details}
    When user selects Sampling setup to update
    And user updates Sampling setup
    And user updates the feature setup details
    Then feature setup updated successfully with message 'Record added.'

7 - Able to update feature setup for Supervisor
    [Documentation]    Able to update feature setup for supervisor
    [Tags]    sysimp    9.3
    [Setup]      run keywords
    ...    user sets the feature setup for sampling to off passing with 'SUPERVISOR' value
    ...    AND    user open browser and logins using user role ${user_role}
    Given user navigates to menu System Configuration | Tenant Maintenance | Feature Setup
    ${setup_status}=   create dictionary
    ...    feature=${True}
    set test variable     &{setup_status}
    ${setup_details}=   create dictionary
    ...    visible=${True}
    ...    enabled=${True}
    set test variable     &{setup_details}
    When user selects Supervisor setup to update
    And user updates Supervisor setup
    And user updates the feature setup details
    Then feature setup updated successfully with message 'Record added.'

8 - Able to update feature setup for Trade Asset
    [Documentation]    Able to update feature setup for trade asset
    [Tags]    sysimp    9.3
    [Setup]      run keywords
    ...    user sets the feature setup for sampling to off passing with 'TRADE_ASSET' value
    ...    AND    user open browser and logins using user role ${user_role}
    Given user navigates to menu System Configuration | Tenant Maintenance | Feature Setup
    ${setup_status}=   create dictionary
    ...    feature=${True}
    set test variable     &{setup_status}
    ${setup_details}=   create dictionary
    ...    visible=${True}
    ...    enabled=${True}
    set test variable     &{setup_details}
    When user selects Trade Asset setup to update
    And user updates Trade Asset setup
    And user updates the feature setup details
    Then feature setup updated successfully with message 'Record added.'

9 - Able to update feature setup for Trade Program
    [Documentation]    Able to update feature setup for trade program
    [Tags]    sysimp    9.3
    [Setup]      run keywords
    ...    user sets the feature setup for sampling to off passing with 'TRADE_PROGRAM' value
    ...    AND    user open browser and logins using user role ${user_role}
    Given user navigates to menu System Configuration | Tenant Maintenance | Feature Setup
    ${setup_status}=   create dictionary
    ...    feature=${True}
    set test variable     &{setup_status}
    ${setup_details}=   create dictionary
    ...    visible=${True}
    ...    enabled=${True}
    set test variable     &{setup_details}
    When user selects Trade Program setup to update
    And user updates Trade Program setup
    And user updates the feature setup details
    Then feature setup updated successfully with message 'Record added.'