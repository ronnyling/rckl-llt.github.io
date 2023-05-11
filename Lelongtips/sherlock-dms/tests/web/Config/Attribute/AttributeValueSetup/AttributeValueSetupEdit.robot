*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/Attribute/AttributeValueSetup/AttributeValueSetupAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/Attribute/AttributeValueSetup/AttributeValueSetupListPage.py
Library         ${EXECDIR}${/}resources/web/Config/Attribute/AttributeValueSetup/AttributeValueSetupEditPage.py

*** Test Cases ***
1 - Able to edit Attribute Value Setup data with fixed data
    [Tags]   distadm    9.0
    ${attribute_value_setup_details}=   create dictionary
    ...    attribute_value_setup_cd=ABCDGM
    set test variable    &attribute_value_setup_details
    Given user navigates to menu Configuration | Attributes | Attribute Value Setup
    When user creates attribute value setup with random data
    Then attribute value setup created successfully with message 'Record created successfully'
    When user selects attribute value setup to edit
    And user edits attribute value setup with fixed data
    Then attribute value setup edited successfully with message 'Record updated successfully'
    When user select created attribute to delete
    Then attribute value setup deleted successfully with message 'Record deleted'

2 - Able to edit attribute value setup data with random data
    [Tags]   distadm     9.0
    Given user navigates to menu Configuration | Attributes | Attribute Value Setup
    When user creates attribute value setup with random data
    Then attribute value setup created successfully with message 'Record created successfully'
    When user selects attribute value setup to edit
    And user edits attribute value setup with random data
    Then attribute value setup edited successfully with message 'Record updated successfully'
    When user select created attribute to delete
    Then attribute value setup deleted successfully with message 'Record deleted'
