*** Settings ***
Resource            ${EXECDIR}${/}tests/web/common.robot
Library             ${EXECDIR}${/}resources/web/Config/ReferenceData/StockAgeing/StockAgeingAddPage.py
Library             ${EXECDIR}${/}resources/web/Config/ReferenceData/StockAgeing/StockAgeingListingPage.py

*** Test Cases ***
1 - Able to Delete an Aging Period using random data
    [Documentation]    Able to Delete an Aging Period
    [Tags]     sysimp    hqadm    9.0    NRSZUANQ-25450
    Given user navigates to menu Configuration | Reference Data | Stock Ageing
    When user creates and saves the aging period with fixed data
    Then aging period is created successfully with message 'Record created successfully'
    When user deletes the created aging period
    Then aging period is deleted successfully with message 'Record deleted'



