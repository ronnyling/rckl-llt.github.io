*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/Attribute/AttributeCreation/AttributeCreationAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/Attribute/AttributeCreation/AttributeCreationListPage.py

*** Test Cases ***
1 - Able to Create Attribute Creation using fixed data
    [Tags]   hqadm    9.0
    ${attribute_creation_details}=   create dictionary
    ...    attribute_creation_cd=ABCDFABWRE
    set test variable    &attribute_creation_details
    Given user navigates to menu Configuration | Attributes | Attribute Creation
    When user creates attribute creation with fixed data
    Then attribute creation created successfully with message 'Record created successfully'
    When user select created attribute to delete
    Then attribute creation deleted successfully with message 'Record deleted'

2 - Able to Create Attribute Creation using random data
    [Tags]  hqadm    9.0
    Given user navigates to menu Configuration | Attributes | Attribute Creation
    When user creates attribute creation with random data
    Then attribute creation created successfully with message 'Record created successfully'
    When user select created attribute to delete
    Then attribute creation deleted successfully with message 'Record deleted'
