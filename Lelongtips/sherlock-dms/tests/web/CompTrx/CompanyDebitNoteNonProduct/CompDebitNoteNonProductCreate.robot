*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CompTrx/CompDebitNoteNonProduct/CompDebitNoteNonProductAddPage.py
Library         ${EXECDIR}${/}resources/web/CompTrx/CompCreditNoteNonProduct/CompCreditNoteNonProductAddPage.py
Library         ${EXECDIR}${/}resources/web/CompTrx/CompDebitNoteNonProduct/CompDebitNoteNonProductListPage.py
Library         ${EXECDIR}${/}resources/web/CompTrx/CompanyInvoice/CompInvoiceAddPage.py

*** Test Cases ***
1 - Able to create company debit note non product and validate tax is calculated correct (tax on tax,net,gross)
    [Documentation]    Able to create company debit note non product
    [Tags]     distadm   9.2
    ${DNNPDetails}=    create dictionary
    ...    Supplier=taxsup
    set test variable     &{DNNPDetails}
    Given user navigates to menu Company Transaction | Debit Note (Non Product)
    When user creates company debit note non product
    And user intends to select service 'SACptgacc' and enter amount '100'
    And user validate tax is calculated correctly
    Then company credit note non product created successfully with message 'Record created successfully'

2 - Able to create company debit note non product and validate tax is calculated correct (accumulative tax)
    [Documentation]    Able to create company credit note non product
    [Tags]     distadm    9.2
    ${DNNPDetails}=    create dictionary
    ...    Supplier=taxsup
    set test variable     &{DNNPDetails}
    Given user navigates to menu Company Transaction | Debit Note (Non Product)
    When user creates company debit note non product
    And user intends to select service 'sacnet' and enter amount '100'
    And user validate tax is calculated correctly
    Then company credit note non product created successfully with message 'Record created successfully'