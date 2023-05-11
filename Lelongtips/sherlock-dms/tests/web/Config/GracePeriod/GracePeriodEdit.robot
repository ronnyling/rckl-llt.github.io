*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/GracePeriod/GracePeriodAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/GracePeriod/GracePeriodListPage.py
Library         ${EXECDIR}${/}resources/web/Config/GracePeriod/GracePeriodEditPage.py

*** Test Cases ***
1 - Able to edit an existing Grace Period with random data
    [Documentation]    Able to edit a grace period with random data
    [Tags]     hqadm     9.2
    [Teardown]    run keywords
    ...    AND user selects grace period to delete
    ...    AND     grace period deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Grace Period
    When user creates grace period with random data
    Then grace period created successfully with message 'Record created successfully'
    When user selects grace period to edit
    And user edit grace period with random data
    Then grace period edited successfully with message 'Record updated successfully'

2 - Able to edit an existing Grace Period with fixed data
    [Documentation]    Able to edit a grace period with fixed data
    [Tags]     hqadm     9.2
    [Teardown]    run keywords
    ...    AND user selects grace period to delete
    ...    AND     grace period deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Grace Period
    When user creates grace period with random data
    Then grace period created successfully with message 'Record created successfully'
    When user selects grace period to edit
    ${edit_grace_period_details}=    create dictionary
    ...    transaction_back_date=8
    And user edit grace period with fixed data
    Then grace period edited successfully with message 'Record updated successfully'

3 - Validate distributor is unable to edit grace period
    [Documentation]    Validate distributor is unable to edit grace period
    [Tags]     distadm    9.2
    Given user navigates to menu Configuration | Grace Period
    When user opens a grace period record
    Then validates button Save is hidden from screen