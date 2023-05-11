*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/RouteActivity/RouteActivityListPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/RouteActivity/RouteActivityAddPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/RouteActivity/RouteActivityAssignmentPage.py

*** Test Cases ***
1 - User able to do customer assignment for route activity
    [Documentation]  To validate user able to do customer assignment for route activity with random data
    [Tags]    hqadm   9.2
    ${activity_details}=    create dictionary
    ...    CODE=ChannelB19
    ...    VISIT_FREQUENCY=Weekly
    ...    TARGET_DURATION=1
    set test variable     &{activity_details}
    Given user navigates to menu Merchandising | Merchandising Setup | Route Activity
    When user creates route activity using random data
    Then route activity created successfully with message 'Record added'
    When user selects route activity to edit
    And user assigns customer to Promotion Compliance using fixed data
    Then customer assigned successfully with message 'Record Added'

2 - User able to do route assignment for route activity
    [Documentation]  To validate user able to do route assignment for route activity with random data
    [Tags]    hqadm   9.2
    Given user navigates to menu Merchandising | Merchandising Setup | Route Activity
    When user creates route activity using random data
    Then route activity created successfully with message 'Record added'
    When user selects route activity to edit
    And user adds Level:Country assignment to route activity
    Then route assigned successfully with message 'Record Added'
