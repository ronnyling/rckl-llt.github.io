*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/ClaimType/ClaimTypeAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/ClaimType/ClaimTypeListPage.py

*** Test Cases ***
1-Able to delete one promotion Claim Type
    [Documentation]    To test deleting new promotion Claim Type
    [Tags]   hqadm   hquser    9.0    NRSZUANQ-8636
    Given user navigates to menu Configuration | Reference Data | Claim Type
    When user creates claim type with random data
    Then claim type created successfully with message 'Record created successfully'
    When created claim type is verified successfully and selects to delete
    Then claim type deleted successfully with message 'Record deleted'

