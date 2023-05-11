*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/SFADashboardSetup/SFADashboardSetupAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/SFADashboardSetup/SFADashboardSetupListPage.py
Library         ${EXECDIR}${/}resources/web/Config/SFADashboardSetup/SFADashboardSetupEditPage.py

Test Teardown   run keywords
...    user perform delete on dashboard
...    AND     dashboard deleted successfully with message 'Record deleted'
...    AND     user logouts and closes browser

*** Test Cases ***
1-Able to update setup for Delivery Rep
   [Documentation]    To test that user is able update setup for Delivery Rep
   [Tags]  hqadm    distadm    9.2    NRSZUANQ-46795
   ${DashboardDetails}=    create dictionary
    ...    profile=Delivery Rep
    ...    dashboard=Delivery Dashboard
    ...    card=0
    ...    graph=0
    ...    new_card=4
    set test variable     &{DashboardDetails}
    Given user navigates to menu Configuration | SFA Dashboard Setup
    And user creates dashboard using fixed data
    And dashboard created successfully with message 'Record successfully created'
    When user perform edit on dashboard
    And user edits dashboard data
    Then dashboard edited successfully with message 'Record successfully updated'

2-Validate KPI sequence is disabled when Delivery Rep is selected in during edit
   [Documentation]    To validate KPI sequence is disabled when Delivery Rep is selected on edit page
   [Tags]  hqadm    distadm    9.2    NRSZUANQ-46795
   ${dashboard_details}=    create dictionary
    ...    profile=Delivery Rep
    ...    dashboard=Delivery Dashboard
    ...    card=0
    ...    graph=0
    set test variable     &{dashboard_details}
    Given user navigates to menu Configuration | SFA Dashboard Setup
    And user creates dashboard using fixed data
    And dashboard created successfully with message 'Record successfully created'
    When user perform edit on dashboard
    Then user validate Sequence is disabled
    And user clicks on Cancel button

3-Validate KPI Code and Description when Delivery Rep is selected in during edit
   [Documentation]    To validate new KPI Code and Description is listed when Delivery Rep select during edit
   [Tags]  hqadm  distadm    9.2    NRSZUANQ-46795
   ${dashboard_details}=    create dictionary
    ...    profile=Delivery Rep
    ...    dashboard=Delivery Dashboard
    ...    card=0
    ...    graph=0
   set test variable     &{dashboard_details}
   Given user navigates to menu Configuration | SFA Dashboard Setup
   And user creates dashboard using fixed data
   And dashboard created successfully with message 'Record successfully created'
   When user perform edit on dashboard
   Then user validate KPI listing
   And user clicks on Cancel button


