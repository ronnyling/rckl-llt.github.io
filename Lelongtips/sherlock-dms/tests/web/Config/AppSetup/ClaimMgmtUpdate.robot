*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/AppSetup/ClaimMgmtEditPage.py

*** Test Cases ***
1 - Updates the field in Claim management with random data
    [Documentation]    Updates the field in Claim management
    [Tags]     hqadm    9.1   9.1.1
    Given user navigates to menu Configuration | Application Setup
    When user navigates to Claim Management tab
    Then user updates claim management using random data
    And claim management updated successfully with message 'Record updated successfully'

2 - Updates the field in Claim management with fixed data
    [Documentation]    Updates the field in Claim management
    [Tags]     hqadm    9.1    9.1.1    NRSZUANQ-41904   NRSZUANQ-41902
    ${ClaimMgmtDetails}=    create dictionary
    ...    Enable Stock Out for Damage Claim=${True}
    ...    Enable Claim Acknowledgement=${True}
    ...    Restrict Claim Confirmation before Closure=${False}
    ...    Promotion Day of Claim Generation (Days)=${7}
    ...    Auto Promotion Claim Type=Single
    ...    Damage Day of Claim Generation (Days)=${3}
    ...    Others Day of Claim Generation (Days)=${7}
    ...    Auto Claim Status=Confirmed
    set test variable    &{ClaimMgmtDetails}
    Given user navigates to menu Configuration | Application Setup
    When user navigates to Claim Management tab
    Then user updates claim management using fixed data
    And claim management updated successfully with message 'Record updated successfully'

3 - Validate 'Restrict Claim Confirmation before Closure' is disabled using sys imp access
    [Documentation]    Validate 'Restrict Claim Confirmation before Closure' is disabled in system implementer access
    [Tags]     sysimp    9.1.1    NRSZUANQ-41906
    Given user navigates to menu Configuration | Application Setup
    When user navigates to Claim Management tab
    Then toggle 'Restrict Claim Confirmation before Closure' should be disabled
