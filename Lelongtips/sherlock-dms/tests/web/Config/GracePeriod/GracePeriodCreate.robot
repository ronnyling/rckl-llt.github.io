*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/GracePeriod/GracePeriodAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/GracePeriod/GracePeriodListPage.py

*** Test Cases ***
1 - Able to create new Grace Period with random data
    [Documentation]    Able to create new grace period with random data
    [Tags]      hqadm     9.2
    Given user navigates to menu Configuration | Grace Period
    When user creates grace period with random data
    Then grace period created successfully with message 'Record created successfully'
    When user selects grace period to delete
    Then grace period deleted successfully with message 'Record deleted'

2 - Able to create new Grace Period with fixed data
    [Documentation]    Able to create new grace period with fixed data
    [Tags]      hqadm     9.2
    ${period_details}=    create dictionary
    ...    transaction=Invoice
    ...    distributor_code=DISTK00001
    ...    start_date=18/09/49 00:00:00
    ...    end_date=20/10/49 00:00:00
    ...    transaction_back_date=5
    Given user navigates to menu Configuration | Grace Period
    When user creates grace period with random data
    Then grace period created successfully with message 'Record created successfully'
    When user selects grace period to delete
    Then grace period deleted successfully with message 'Record deleted'

3 - Validate error messages when Grace Period fields are left empty
    [Documentation]    Validate error messages when grace period fields are left empty
    [Tags]     hqadm    9.2
    Given user navigates to menu Configuration | Grace Period
    When user clicks on Add button
    And user clicks on Save button
    Then validate error message on empty fields

4 - Validate distributor is unable to add grace period
    [Documentation]    Validate distributor is unable to add grace period
    [Tags]     distadm    9.2     test
    Given user navigates to menu Configuration | Grace Period
    Then validates button Add is hidden from screen