*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/FacingSetup/FacingSetupAddPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/FacingSetup/FacingSetupListPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/FacingSetup/FacingSetupUpdatePage.py

*** Test Cases ***
1- User able to updates facing setup with random data
    [Documentation]  To validate user able to updates facing setup with random data
    [Tags]   9.1   hqadm    NRSZUANQ-19860
    Given user navigates to menu Merchandising | Merchandising Setup | Facing Setup
    When user creates facing setup using random data
    Then facing setup created successfully with message 'Record created successfully'
    When user validate created facing setup is listed in the table and select to edit
    And user updates facing setup using random data
    Then facing setup updated successfully with message 'Record updated'
    When user validate created facing setup is listed in the table and select to delete
    Then facing setup deleted successfully with message 'Has been deleted'

2- User unable to update facing setup with empty data
    [Documentation]  To validate user unable to update facing setup with empty data
    [Tags]   9.1   hqadm  NRSZUANQ-19865
    Given user navigates to menu Merchandising | Merchandising Setup | Facing Setup
    When user creates facing setup using random data
    Then facing setup created successfully with message 'Record created successfully'
    When user validate created facing setup is listed in the table and select to edit
    And user updates facing setup using empty data
    Then facing setup unable to update successfully with validation message on fields
    When user validate created facing setup is listed in the table and select to delete
    Then facing setup deleted successfully with message 'Has been deleted'

3- User unable to change the Brand Code during edit
    [Documentation]  To validate the Brand Code is none editable during edit
    [Tags]   9.1   hqadm   NRSZUANQ-19867
    Given user navigates to menu Merchandising | Merchandising Setup | Facing Setup
    When user creates facing setup using random data
    Then facing setup created successfully with message 'Record created successfully'
    When user validate created facing setup is listed in the table and select to edit
    And user validates brand code is not editable
    When user validate created facing setup is listed in the table and select to delete
    Then facing setup deleted successfully with message 'Has been deleted'