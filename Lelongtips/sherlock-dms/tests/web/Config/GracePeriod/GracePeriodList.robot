*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/GracePeriod/GracePeriodAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/GracePeriod/GracePeriodListPage.py

*** Test Cases ***
1 - Able to search garace period using distributor code
    [Documentation]    Able to search garace period using distributor code
    [Tags]      hqadm     9.2
    [Teardown]    run keywords
    ...    AND user selects grace period to delete
    ...    AND     grace period deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    ${period_details}=    create dictionary
    ...    transaction=Invoice
    ...    distributor_code=DISTK00001
    ...    start_date=18/09/49 00:00:00
    ...    end_date=20/10/49 00:00:00
    ...    transaction_back_date=5
    Given user navigates to menu Configuration | Grace Period
    When user creates grace period with fixed data
    And grace period created successfully with message 'Record created successfully'
    Then user searches created grace period in listing page by distributor code

2 - Able to search garace period using transaction type
    [Documentation]    Able to search garace period using transaction type
    [Tags]      hqadm     9.2
    [Teardown]    run keywords
    ...    AND user selects grace period to delete
    ...    AND     grace period deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    ${period_details}=    create dictionary
    ...    transaction=Invoice
    ...    distributor_code=DISTK00001
    ...    start_date=18/09/49 00:00:00
    ...    end_date=20/10/49 00:00:00
    ...    transaction_back_date=5
    Given user navigates to menu Configuration | Grace Period
    When user creates grace period with fixed data
    And grace period created successfully with message 'Record created successfully'
    Then user searches created grace period in listing page by transaction type

3 - Able to filter garace period using date
    [Documentation]    Able to search garace period using back date
    [Tags]      hqadm     9.2
    [Teardown]    run keywords
    ...    AND user selects grace period to delete
    ...    AND     grace period deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    ${period_details}=    create dictionary
    ...    transaction=Invoice
    ...    distributor_code=DISTK00001
    ...    start_date=18/09/49 00:00:00
    ...    end_date=20/10/49 00:00:00
    ...    transaction_back_date=5
    Given user navigates to menu Configuration | Grace Period
    When user creates grace period with fixed data
    And grace period created successfully with message 'Record created successfully'
    Then user filter grace period in listing page by date