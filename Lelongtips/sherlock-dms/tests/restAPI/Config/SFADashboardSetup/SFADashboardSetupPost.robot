*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/SFADashboardSetup/SFADashboardSetupDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/SFADashboardSetup/SFADashboardSetupPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/SFADashboardSetup/SFADashboardSetupGet.py

Test Setup    user validates is there any delivery dashboard

*** Test Cases ***
1 - Able to post SFA Dashboard Setup
    [Documentation]  To test able to post SFA Dashboard setup
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

2 - Unable to post SFA Dashboard Setup with Card > 4
    [Documentation]    To test unable to post delivery dashboard when card >4
    [Tags]    hqadm    distadm    9.2    NRSZUANQ-46796
    ${dashboard_details}=    create dictionary
    ...    DASHBOARD_NAME=Delivery Dashboard
    ...    PROFILE_CODE=PR07
    ...    PROFILE_DESC=Delivery Rep
    ...    DASHBOARD_CODE=DS07
    ...    DASHBOARD_DESC=DELIVERY
    ...    CARD=6
    ...    GRAPH=0
    set test variable   &{dashboard_details}
    Given user retrieves token access as ${user_role}
    When user creates dashboard with fixed data
    Then expected return status code 400


3 - Unable to post SFA Dashboard Setup with Graph>0
    [Documentation]    To test unable to post delivery dashboard when graph>0
    [Tags]    hqadm    distadm    9.2     NRSZUANQ-46796
    ${dashboard_details}=    create dictionary
    ...    DASHBOARD_NAME=Delivery Dashboard
    ...    PROFILE_CODE=PR07
    ...    PROFILE_DESC=Delivery Rep
    ...    DASHBOARD_CODE=DS07
    ...    DASHBOARD_DESC=DELIVERY
    ...    GRAPH=3
    ...    CARD=0
    set test variable   &{dashboard_details}
    Given user retrieves token access as ${user_role}
    When user creates dashboard with fixed data
    Then expected return status code 400

4 - Unable to post Delivery Profile with dashboard other than Delivery Dashboard
    [Documentation]  To test unable to post delivery dashboard with other type of dashboard
    [Tags]    hqadm    distadm    9.2    NRSZUANQ-46796
    ${dashboard_details}=    create dictionary
    ...    DASHBOARD_NAME=SFA Dashboard for Today
    ...    PROFILE_CODE=PR07
    ...    PROFILE_DESC=Delivery Rep
    ...    DASHBOARD_CODE=DS01
    ...    DASHBOARD_DESC=TODAY
    ...    CARD=0
    ...    GRAPH=0
    set test variable   &{dashboard_details}
    Given user retrieves token access as ${user_role}
    When user creates dashboard with fixed data
    Then expected return status code 400

5 - Unable to post Delivery Profile with KPI selection < Card
    [Documentation]    To test unable to post delivery profile when KPI selected less than card
    [Tags]    hqadm    distadm    9.2    NRSZUANQ-46796
    ${dashboard_details}=    create dictionary
    ...    DASHBOARD_NAME=Delivery Dashboard
    ...    PROFILE_CODE=PR07
    ...    PROFILE_DESC=Delivery Rep
    ...    DASHBOARD_CODE=DS07
    ...    DASHBOARD_DESC=DELIVERY
    ...    CARD=3
    ...    GRAPH=0
    set test variable   &{dashboard_details}
    Given user retrieves token access as ${user_role}
    When user creates dashboard with fixed data
    Then expected return status code 400


