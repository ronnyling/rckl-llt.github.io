*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/SFADashboardSetup/SFADashboardSetupListPage.py
Library         ${EXECDIR}${/}resources/web/Config/SFADashboardSetup/SFADashboardSetupAddPage.py
*** Test Cases ***
1-Able to delete setup for Delivery Rep
    [Documentation]    To test that user is able to delete setup for Delivery Rep
    [Tags]  hqadm    distadm    9.2    NRSZUANQ-46795
    ${DashboardDetails}=    create dictionary
    ...    profile=Delivery Rep
    ...    dashboard=Delivery Dashboard
    ...    card=0
    ...    graph=0
    set test variable     &{DashboardDetails}
    Given user navigates to menu Configuration | SFA Dashboard Setup
    And user creates dashboard using fixed data
    And dashboard created successfully with message 'Record successfully created'
    When user perform delete on dashboard
    Then dashboard deleted successfully with message 'Record deleted'


