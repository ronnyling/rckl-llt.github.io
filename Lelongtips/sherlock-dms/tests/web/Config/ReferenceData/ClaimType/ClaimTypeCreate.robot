*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/ClaimType/ClaimTypeAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/ClaimType/ClaimTypeListPage.py

*** Test Cases ***
1-Able to Create new promotion Claim Type with RandomData
    [Documentation]    To test creating new promotion Claim Type with Random Data
    [Tags]   hqadm    hquser    9.0    NRSZUANQ-4450    NRSZUANQ-8636    NRSZUANQ-8878
    Given user navigates to menu Configuration | Reference Data | Claim Type
    When user creates claim type with random data
    Then claim type created successfully with message 'Record created successfully'
    When created claim type is verified successfully and selects to delete
    Then claim type deleted successfully with message 'Record deleted'

2-To ensure all the error message is showing correctly and standardize
    [Documentation]    Ensure the error message for the empty fields should shows correctly
    [Tags]    hqadm   hquser     9.0    NRSZUANQ-8636
    Given user navigates to menu Configuration | Reference Data | Claim Type
    When user clicks on Add button
    And user clicks on Save button
    Then validate error message on empty fields

3-Not able to create new promotion Claim Type with Deleted Data
    [Documentation]    To test not able to create new promotion Claim Type with deleted Data
    [Tags]   hqadm   hquser   9.0    NRSZUANQ-2896    NRSZUANQ-8636
    Given user navigates to menu Configuration | Reference Data | Claim Type
    When user creates claim type with random data
    Then claim type created successfully with message 'Record created successfully'
    When created claim type is verified successfully and selects to delete
    Then claim type deleted successfully with message 'Record deleted'
    When user creates claim type with deleted data
    Then error message shown already exists

4-Not able to create new promotion Claim Type with existing claim type code and promotion type
    [Documentation]    To test not able to create new promotion claim type using existing claim type code and promotion type
    [Tags]    hqadm   hquser     9.0     NRSZUANQ-8636
    Given user navigates to menu Configuration | Reference Data | Claim Type
    When user creates claim type with random data
    Then claim type created successfully with message 'Record created successfully'
    When user creates claim type with existing data
    Then error message shown already exists
    When user clicks on Cancel button
    And created claim type is verified successfully and selects to delete
    Then claim type deleted successfully with message 'Record deleted'

5-Not able to create new promotion Claim Type with empty data
    [Documentation]    To test not able to create new promotion claim type using empty data
    [Tags]     hqadm   hquser   9.0
     ${claim_details}=    create dictionary
    ...    claim_code=${Empty}
    ...    claim_desc=${Empty}
    set test variable     &{claim_details}
    Given user navigates to menu Configuration | Reference Data | Claim Type
    When user creates claim type with empty data
    Then validate error message on empty fields



