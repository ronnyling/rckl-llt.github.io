*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CompTrx/CompDebitNoteProduct/CompDebitNoteProductAddPage.py
Library         ${EXECDIR}${/}resources/web/CompTrx/CompDebitNoteProduct/CompDebitNoteProductListPage.py
Library         ${EXECDIR}${/}resources/web/CompTrx/CompanyInvoice/CompInvoiceAddPage.py


*** Test Cases ***
1 - Able to create company debit note product and validate tax is calculated correct (tax on tax,net,gross)
    [Documentation]    Able to create company debit note product
    [Tags]     distadm   9.2
    ${DNDetails}=    create dictionary
    ...    Warehouse=whtt
        ...    Supplier=taxsup
    set test variable     &{DNDetails}
    Given user navigates to menu Company Transaction | Debit Note (Product)
    When user creates company debit note product
    And user intends to insert product 'NikeShoes' with uom 'Each', Qty '10'
    And insert price '100' and discount '2'
    Then company debit note product created successfully with message 'Record created successfully'

2 - Able to create company debit note product and validate tax is calculated correct (accumulative tax)
    [Documentation]    Able to create company debit note product
    [Tags]     distadm    9.2
    ${CNDetails}=    create dictionary
    ...    Warehouse=whtt
    ...    Supplier=taxsup
    set test variable     &{CNDetails}
    Given user navigates to menu Company Transaction | Debit Note (Product)
    When user creates company debit note product
    And user intends to insert product 'NikeWatch' with uom 'BOX', Qty '10'
    And insert price '100' and discount '2'
    Then company debit note product created successfully with message 'Record created successfully'