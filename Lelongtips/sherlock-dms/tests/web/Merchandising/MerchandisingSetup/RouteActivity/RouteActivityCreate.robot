*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/RouteActivity/RouteActivityAddPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/RouteActivity/RouteActivityListPage.py


*** Test Cases ***
1 - User able to create new route activity with random data
    [Documentation]  To validate user able to create new route activity with random data
    [Tags]    hqadm    9.2
    Given user navigates to menu Merchandising | Merchandising Setup | Route Activity
    When user creates route activity using random data
    Then route activity created successfully with message 'Record added'
    When user selects route activity to delete
    Then route activity deleted successfully with message 'Record deleted'

2 - User able to create new route activity with fixed data
    [Documentation]  To validate user able to create new route activity with random data
    [Tags]    hqadm    9.2
    ${activity_details}=    create dictionary
    ...    ACTIVITY_CODE=RATEST001
    ...    ACTIVITY_DESC=Route Activity Test 001
    set test variable     &{activity_details}
    Given user navigates to menu Merchandising | Merchandising Setup | Route Activity
    When user creates route activity using fixed data
    Then route activity created successfully with message 'Record added'
    When user selects route activity to delete
    Then route activity deleted successfully with message 'Record deleted'
