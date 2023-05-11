*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/SFADashboardSetup/SFADashboardSetupListPage.py
Library         ${EXECDIR}${/}resources/web/Config/SFADashboardSetup/SFADashboardSetupAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/SFADashboardSetup/SFADashboardSetupEditPage.py
Test Teardown   run keywords
...    user perform delete on dashboard
...    AND     dashboard deleted successfully with message 'Record deleted'
...    AND     user logouts and closes browser

*** Test Cases ***
1-Able to filter existing content based on Profile
   [Documentation]    To test that user is able to filter dashboard based on Delivery Rep profile
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
    When user filters created dashboard in listing page
    Then record display in listing successfully

2-Able to search existing content based on Profile and Dashboard
   [Documentation]    To test that user is able to search dashboard based on profile and dashboard
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
    When user searches created dashboard in listing page
    Then record display in listing successfully

3-Able to view setup for Delivery Rep
   [Documentation]    To test that user is able view created setup for Delivery Rep
   [Tags]  hqadm  distadm  9.2  NRSZUANQ-46795
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
   Then user is able to navigate to EDIT | SFA Dashboard Setup



