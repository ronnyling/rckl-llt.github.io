*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/SFADashboardSetup/SFADashboardSetupListPage.py
Library         ${EXECDIR}${/}resources/web/Config/SFADashboardSetup/SFADashboardSetupAddPage.py

*** Test Cases ***
1- Able to create random setup for SFA Dashboard
   [Documentation]    To test that user is able to create random setup for SFA Dashboard
   [Tags]  hqadm    distadm    9.2    NRSZUANQ-46795
   [Teardown]    run keywords
    ...    user perform delete on dashboard
    ...    AND     dashboard deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | SFA Dashboard Setup
    And user creates dashboard using random data
    Then dashboard created successfully with message 'Record successfully created'

2- Able to create setup for Delivery Rep
   [Documentation]    To test that user is able to create Delivery Rep setup for SFA Dashboard
   [Tags]  hqadm    distadm    9.2    NRSZUANQ-46795
   [Teardown]    run keywords
    ...    user perform delete on dashboard
    ...    AND     dashboard deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
   ${dashboard_details}=    create dictionary
    ...    profile=Delivery Rep
    ...    dashboard=Delivery Dashboard
    ...    card=0
    ...    graph=0
    set test variable     &dashboard_details
    Given user navigates to menu Configuration | SFA Dashboard Setup
    And user creates dashboard using fixed data
    Then dashboard created successfully with message 'Record successfully created'


3-Validate that only Delivery Dashboard is available Delivery Rep selected
    [Documentation]    To validate that only Delivery Dashboard is listed when Delivery Rep is selected
   [Tags]  hqadm    distadm    9.2    NRSZUANQ-46795
    ${dashboard_details}=    create dictionary
    ...    profile=Delivery Rep
    set test variable     &{dashboard_details}
    Given user navigates to menu Configuration | SFA Dashboard Setup
    When user clicks on Add button
    And user selects Profile
    Then user validate dashboard

4-Validate Card option range is between 0-4 when Delivery Rep selected
   [Documentation]    To validate that Card selection only display 0-4 when Delivery Rep selected
   [Tags]  hqadm    distadm    9.2    NRSZUANQ-46795
   ${dashboard_details}=    create dictionary
    ...    profile=Delivery Rep
    ...    dashboard=Delivery Dashboard
    ...    card=0
    set test variable     &{dashboard_details}
    Given user navigates to menu Configuration | SFA Dashboard Setup
    When user clicks on Add button
    And user selects Profile
    And user selects Dashboard
    Then user validate Card drop down have following value:0,1,2,3,4

5-Validate KPI sequence is disabled when Delivery Rep is selected in during add
   [Documentation]    To validate KPI sequence is disabled for Delivery Rep in add page
   [Tags]  hqadm    distadm    9.2 NRSZUANQ-46795
   ${dashboard_details}=    create dictionary
    ...    profile=Delivery Rep
    ...    dashboard=Delivery Dashboard
    ...    card=4
    ...    graph=0
    set test variable     &{dashboard_details}
    Given user navigates to menu Configuration | SFA Dashboard Setup
    When user clicks on Add button
    And user selects header selections
    Then user validate Sequence is disabled

6-Validate KPI Code and Description when Delivery Rep is selected in during add
   [Documentation]    To validate new KPI Code and Description is listed for Delivery Rep setup
   [Tags]  hqadm    distadm    9.2    NRSZUANQ-46795
   ${DashboardDetails}=    create dictionary
    ...    profile=Delivery Rep
    ...    dashboard=Delivery Dashboard
    ...    card=0
    ...    graph=0
    set test variable     &{DashboardDetails}
    Given user navigates to menu Configuration | SFA Dashboard Setup
    When user clicks on Add button
    And user selects header selections
    Then user validate KPI listing

7-Validate Graph option is 0 when Delivery Rep selected
   [Documentation]    To test Graph selection only display 0 when Delivery Rep selected
   [Tags]  hqadm    distadm    9.2    NRSZUANQ-46795
   ${dashboard_details}=    create dictionary
    ...    profile=Delivery Rep
    ...    dashboard=Delivery Dashboard
    set test variable     &{dashboard_details}
    Given user navigates to menu Configuration | SFA Dashboard Setup
    When user clicks on Add button
    And user selects Profile
    And user selects Dashboard
    Then user validate Graph drop down have following value:0

8-Unable to create duplicate setup for Delivery Dashboard
   [Documentation]    To test that user is unable to create duplicating Delivery Dashboard
   [Tags]  hqadm    distadm    9.2    NRSZUANQ-46795
   [Teardown]    run keywords
    ...    user clicks on Cancel button
    ...    AND     user perform delete on dashboard
    ...    AND     dashboard deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    ${dashboard_details}=    create dictionary
    ...    profile=Delivery Rep
    ...    dashboard=Delivery Dashboard
    ...    card=0
    ...    graph=0
    set test variable     &dashboard_details
    Given user navigates to menu Configuration | SFA Dashboard Setup
    When user creates dashboard using fixed data
    Then dashboard created successfully with message 'Record successfully created'
    When user creates dashboard using fixed data
    Then expect pop up message: Profile 'Delivery Rep' and dashboard 'Delivery Dashboard' existed.



9-Unable to save setup when selected KPI is not the same as card selection
   [Documentation]    To test that user is unable to save when KPI and card selection are not the same
   [Tags]  hqadm    distadm    9.2    NRSZUANQ-46795
   ${dashboard_details}=    create dictionary
    ...    profile=Delivery Rep
    ...    dashboard=Delivery Dashboard
    ...    card=4
    ...    graph=0
    set test variable     &{dashboard_details}
    Given user navigates to menu Configuration | SFA Dashboard Setup
    When user clicks on Add button
    And user selects header selections
    And user clicks on Save button
    Then dashboard not created successfully with message 'Please check the card and graph'








