*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/ClaimType/ClaimTypeAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/ClaimType/ClaimTypeEditPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/ClaimType/ClaimTypeListPage.py

*** Test Cases ***
1-Able to view Claim Type details
    [Documentation]    To test that user able to view claim type details
    [Tags]   hqadm   hquser    9.0     NRSZUANQ-11399
    Given user navigates to menu Configuration | Reference Data | Claim Type
    When user creates claim type with random data
    Then claim type created successfully with message 'Record created successfully'
    When created claim type is verified successfully and selects to edit
    Then claim type viewed successfully
    When created claim type is verified successfully and selects to delete
    Then claim type deleted successfully with message 'Record deleted'

2-Able to update promotion Claim Type with all valid input
    [Documentation]    To test updating new promotion Claim Type with all valid input
    [Tags]   hqadm   hquser    9.0    NRSZUANQ-8636      test
    Given user navigates to menu Configuration | Reference Data | Claim Type
    When user creates claim type with random data
    Then claim type created successfully with message 'Record created successfully'
    When created claim type is verified successfully and selects to edit
    And user edits claim type with random data
    Then claim type updated successfully with message 'Record updated successfully'
    When created claim type is verified successfully and selects to delete
    Then claim type deleted successfully with message 'Record deleted'