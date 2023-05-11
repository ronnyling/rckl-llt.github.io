*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/FacingSetup/FacingSetupAddPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/FacingSetup/FacingSetupListPage.py

*** Test Cases ***
1- User able to delete facing setup
    [Documentation]  To validate user able to delete facing setup
    [Tags]   9.1   hqadm   NRSZUANQ-19861
    Given user navigates to menu Merchandising | Merchandising Setup | Facing Setup
    When user creates facing setup using random data
    Then facing setup created successfully with message 'Record created successfully'
    When user validate created facing setup is listed in the table and select to delete
    Then facing setup deleted successfully with message 'Has been deleted'