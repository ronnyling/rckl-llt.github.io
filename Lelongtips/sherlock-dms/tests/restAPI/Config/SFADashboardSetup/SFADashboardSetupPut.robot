*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/SFADashboardSetup/SFADashboardSetupDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/SFADashboardSetup/SFADashboardSetupPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/SFADashboardSetup/SFADashboardSetupPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/SFADashboardSetup/SFADashboardSetupGet.py

Test Setup    user validates is there any delivery dashboard

*** Test Cases ***
1 - Able to put SFA Dashboard Setup
    [Documentation]  To test user is able to put dashboard setup
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
    ${new_dashboard_details}=    create dictionary
    ...    CARD=2
    ...    GRAPH=0
    set test variable   &{new_dashboard_details}
    Given user retrieves token access as ${user_role}
    When user creates dashboard with fixed data
    Then expected return status code 201
    When user gets dashboard by using valid id
    Then expected return status code 200
    When user edits dashboard with valid data using valid id
    Then expected return status code 200

2 - Able to put SFA Dashboard Setup (Delivery Dashboard)
    [Documentation]  To test user is able to put fixed dashboard setup - Delivery Rep
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
    ${new_dashboard_details}=    create dictionary
    ...    CARD=1
    ...    GRAPH=0
    set test variable   &{new_dashboard_details}
    Given user retrieves token access as ${user_role}
    When user creates dashboard with fixed data
    Then expected return status code 201
    When user gets dashboard by using valid id
    Then expected return status code 200
    When user edits dashboard with valid data using valid id
    Then expected return status code 200

3 - Unable to put SFA Dashboard Setup with Card > 4
    [Documentation]  To test user unable to put dashboard with card more than 4
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
    ${new_dashboard_details}=    create dictionary
    ...    CARD=5
    ...    GRAPH=0
    set test variable   &{new_dashboard_details}
    Given user retrieves token access as ${user_role}
    When user creates dashboard with fixed data
    Then expected return status code 201
    When user gets dashboard by using valid id
    Then expected return status code 200
    When user edits dashboard with card data using valid id
    Then expected return status code 400

4 - Unable to put SFA Dashboard Setup with Graph>0
    [Documentation]  To test user unable to put dashboard with graph value more than 0
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
    ${new_dashboard_details}=    create dictionary
    ...    CARD=0
    ...    GRAPH=1
    set test variable   &{new_dashboard_details}
    Given user retrieves token access as ${user_role}
    When user creates dashboard with fixed data
    Then expected return status code 201
    When user gets dashboard by using valid id
    Then expected return status code 200
    When user edits dashboard with graph data using valid id
    Then expected return status code 400

5 - Unable to put Delivery Profile with Sequence value
    [Documentation]  To test user unable to put delivery profile with sequence for KPI
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
    ${new_dashboard_details}=    create dictionary
    ...    CARD=0
    ...    GRAPH=1
    set test variable   &{new_dashboard_details}
    ${new_sequence_details}=    create dictionary
    ...    SEQ=1
    set test variable   &{new_sequence_details}
    Given user retrieves token access as ${user_role}
    When user creates dashboard with fixed data
    Then expected return status code 201
    When user gets dashboard by using valid id
    Then expected return status code 200
    When user edits dashboard with sequence data using valid id
    Then expected return status code 400

6 - Unable to put Delivery Profile with dashboard other than Delivery Dashboard
    [Documentation]  To test user unable put delivery profile with dashboard other than delivery dashboard
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
    ${new_dashboard_details}=    create dictionary
    ...    CARD=0
    ...    GRAPH=0
    set test variable   &{new_dashboard_details}
    ${new_sequence_details}=    create dictionary
    ...    SEQ=1
    set test variable   &{new_sequence_details}
    ${new_dashboard_type}=    create dictionary
    ...    DASHBOARD_NAME=SFA Dashboard for Today
    ...    DASHBOARD_CODE=DS01
    ...    DASHBOARD_DESC=TODAY
    set test variable   &{new_dashboard_type}
    Given user retrieves token access as ${user_role}
    When user creates dashboard with fixed data
    Then expected return status code 201
    When user gets dashboard by using valid id
    Then expected return status code 200
    When user edits dashboard with dashboard data using valid id
    Then expected return status code 400
