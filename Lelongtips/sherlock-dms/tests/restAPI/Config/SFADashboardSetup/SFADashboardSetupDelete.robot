*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/SFADashboardSetup/SFADashboardSetupDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/SFADashboardSetup/SFADashboardSetupPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/SFADashboardSetup/SFADashboardSetupGet.py

Test Setup    user validates is there any delivery dashboard

*** Test Cases ***
1 - Able to delete SFA Dashboard Setup
    [Documentation]  To delete dashboard setup via valid id using API
    [Tags]    hqadm    distadm    9.2    NRSZUANQ-46796
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
    When user deletes the created dashboard with valid id
    Then expected return status code 204

#2 - Unable to delete SFA Dashboard Setup with invalid id
#    [Documentation]  To delete dashboard setup via invalid id using API
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
#    When user deletes the created dashboard with invalid id
#    Then expected return status code 404
