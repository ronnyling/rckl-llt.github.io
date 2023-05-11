*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/AppSetup/AccountReceivableEditPage.py

*** Test Cases ***
1 - Updates the field in Account Receivable with random data
    [Documentation]    Updates the field in Account Receivable
    [Tags]     hqadm    9.1   9.1.1
    Given user navigates to menu Configuration | Application Setup
    When user navigates to Accounts Receivable tab
    Then user updates account receivable using random data
    And account receivable updated successfully with message 'Record updated successfully'

2 - Updates the field in Account receivable with fixed data
    [Documentation]    Updates the field in Account receivable
    [Tags]     hqadm    9.1    9.1.1    NRSZUANQ-41905   NRSZUANQ-41903
    ${AccountReceivableDetails}=    create dictionary
    ...    Restrict Billing in Case of Outlet Type Changes=${False}
    ...    Allow to Toggle Cash/Credit=${True}
    ...    Ref No. Mandatory=${False}
    ...    Allow Return/CN from Single Invoice Only=${False}
    ...    Allow Editing Price in Return (SFA)=${True}
    set test variable    &{AccountReceivableDetails}
    Given user navigates to menu Configuration | Application Setup
    When user navigates to Accounts Receivable tab
    Then user updates account receivable using fixed data
    And account receivable updated successfully with message 'Record updated successfully'

#Not applicable to hqadm
3 - Updates the field in Account receivable with given data
    [Documentation]    Updates the field in Account receivable
    [Tags]     sysimp    9.1
    ${AccountReceivableDetails}=    create dictionary
    ...    Enable Partial Return Promo Benefit=${False}
    ...    Restrict Return More Than Invoice Qty (Track Balance Invoice Quantity)=${True}
    set test variable    &{AccountReceivableDetails}
    Given user navigates to menu Configuration | Application Setup
    When user navigates to Accounts Receivable tab
    Then user updates account receivable using fixed data
    And account receivable updated successfully with message 'Record updated successfully'

4 - Validate 'Allow Editing Price in Return (SFA)' is disabled using sys imp access
    [Documentation]    Toggle field is disabled in system implementer access
    [Tags]     sysimp    9.1.1    NRSZUANQ-41907
    Given user navigates to menu Configuration | Application Setup
    When user navigates to Accounts Receivable tab
    Then toggle 'Allow Editing Price in Return (SFA)' should be disabled
