*** Settings ***
Resource            ${EXECDIR}${/}tests/web/common.robot
Library             ${EXECDIR}${/}resources/web/Config/ReferenceData/StockAgeing/StockAgeingAddPage.py
Library             ${EXECDIR}${/}resources/web/Config/ReferenceData/StockAgeing/StockAgeingListingPage.py
Library             Collections

*** Test Cases ***
1 - Able to Create an Aging Period using random data
    [Documentation]    Able to Create an Aging Period
    [Tags]     sysimp    hqadm    9.0    NRSZUANQ-25450
    Given user navigates to menu Configuration | Reference Data | Stock Ageing
    When user creates and saves the aging period with fixed data
    Then aging period is created successfully with message 'Record created successfully'
    When user deletes the created aging period
    Then aging period is deleted successfully with message 'Record deleted'

2 - Able to create an Aging Period with given data
    [Documentation]    To create an Aging Period with given data
    [Tags]     sysimp   hqadm    9.1    NRSZUANQ-25450
    ${aging_period_details}=    create dictionary
    ...    PERIOD_CD=PeriodCodeGivenData
    ...    PERIOD_DESC=Period Description by given data
    set test variable   &{aging_period_details}
    Given user navigates to menu Configuration | Reference Data | Stock Ageing
    When user creates and saves the aging period with fixed data
    Then aging period is created successfully with message 'Record created successfully'
    When user deletes the created aging period
    Then aging period is deleted successfully with message 'Record deleted'