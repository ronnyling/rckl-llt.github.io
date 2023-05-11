*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/SFADashboardSetup/SFADashboardSetupGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/SFADashboardSetup/SFADashboardSetupDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/SFADashboardSetup/SFADashboardSetupPost.py

Test Setup    user validates is there any delivery dashboard

*** Test Cases ***
1 - Able to get all SFA Dashboard Setup
    [Documentation]  To get all dashboard setup using API
    [Tags]    hqadm    distadm    9.2    NRSZUANQ-46796
    Given user retrieves token access as ${user_role}
    When user retrieves all dashboard data
    Then expected return status code 200

2 - Able to get SFA Dashboard by id
    [Documentation]  To test able to get dashboard via valid id using API
    [Tags]    hqadm    distadm    9.2    NRSZUANQ-46796
    [Teardown]    run keywords
    ...    user deletes the created dashboard with valid id
    ...    AND expected return status code 204
    ${dashboard_details}=    create dictionary
    ...    DASHBOARD_NAME=Delivery Dashboard
    ...    PROFILE_CODE=PR07
    ...    PROFILE_DESC=Delivery Rep
    ...    DASHBOARD_CODE=DS07
    ...    DASHBOARD_DESC=DELIVERY
    ...    CARD=0
    ...    GRAPH=0
    set test variable   &{dashboard_details}
    Given user retrieves token access as ${user_role}
    When user creates dashboard with fixed data
    Then expected return status code 201
    When user gets dashboard by using valid id
    Then expected return status code 200

#3 - Unable to get SFA Dashboard using invalid id
#    [Documentation]  To test unable to get dashboard using invalid id using API
#    [Tags]    hqadm    distadm    9.2    NRSZUANQ-46796
#    [Teardown]    run keywords
#    ...    user deletes the created dashboard with valid id
#    ...    AND expected return status code 204
#    ${dashboard_details}=    create dictionary
#    ...    DASHBOARD_NAME=Delivery Dashboard
#    ...    PROFILE_CODE=PR07
#    ...    PROFILE_DESC=Delivery Rep
#    ...    DASHBOARD_CODE=DS07
#    ...    DASHBOARD_DESC=DELIVERY
#    ...    CARD=0
#    ...    GRAPH=0
#    set test variable   &{dashboard_details}
#    Given user retrieves token access as ${user_role}
#    When user creates dashboard with fixed data
#    Then expected return status code 201
#    When user gets dashboard by using invalid id
#    Then expected return status code 404
