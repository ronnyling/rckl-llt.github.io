*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/Attribute/AttributeValueSetup/AttributeValueSetupAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/Attribute/AttributeValueSetup/AttributeValueSetupListPage.py

*** Test Cases ***
1 - Able to Delete Attribute Value Setup using random data
    [Tags]  hqadm    9.0
    Given user navigates to menu Configuration | Attributes | Attribute Value Setup
    When user creates attribute value setup with random data
    Then attribute value setup created successfully with message 'Record created successfully'
    When user select created attribute to delete
    Then attribute value setup deleted successfully with message 'Record deleted'
