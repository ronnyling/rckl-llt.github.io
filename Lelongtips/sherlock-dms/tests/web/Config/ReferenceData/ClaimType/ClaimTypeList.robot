*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/ClaimType/ClaimTypeAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/ClaimType/ClaimTypeListPage.py

*** Test Cases ***
1-Able to search Claim Type using search method
    [Documentation]    To test searching for claim type using search function
    [Tags]   hqadm   hquser   9.0     NRSZUANQ-12618
    Given user navigates to menu Configuration | Reference Data | Claim Type
    When user creates claim type with random data
    Then claim type created successfully with message 'Record created successfully'
    When user searches created claim type
    Then record display in listing successfully
    When created claim type is verified successfully and selects to delete
    Then claim type deleted successfully with message 'Record deleted'

2-Able to filter promotion Claim Type with valid input
    [Documentation]    To test filtering promotion Claim Type with valid data
    [Tags]   hqadm   hquser    9.0    NRSZUANQ-8636   NRSZUANQ-12617    NRSZUANQ-12663
    Given user navigates to menu Configuration | Reference Data | Claim Type
    When user creates claim type with random data
    Then claim type created successfully with message 'Record created successfully'
    When user filters created claim type
    Then record display in listing successfully
    When created claim type is verified successfully and selects to delete
    Then claim type deleted successfully with message 'Record deleted'