*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/Attribute/AttributeValueSetup/AttributeValueSetupAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/Attribute/AttributeValueSetup/AttributeValueSetupListPage.py

*** Test Cases ***
1 - Able to Create Attribute Value Setup using fixed data
    [Tags]   hqadm    9.0
    ${attribute_value_setup_details}=   create dictionary
    ...    attribute_value_setup_cd=ABCDFABWRE
    ...    attribute_value_setup_val=ABCDFABWRE
    set test variable    &attribute_value_setup_details
    Given user navigates to menu Configuration | Attributes | Attribute Value Setup
    When user creates attribute value setup with fixed data
    Then attribute value setup created successfully with message 'Record created successfully'
    When user select created attribute to delete
    Then attribute value setup deleted successfully with message 'Record deleted'

2 - Able to Create Attribute Value Setup using random data
    [Tags]  hqadm    9.0
    Given user navigates to menu Configuration | Attributes | Attribute Value Setup
    When user creates attribute value setup with random data
    Then attribute value setup created successfully with message 'Record created successfully'
    When user select created attribute to delete
    Then attribute value setup deleted successfully with message 'Record deleted'
