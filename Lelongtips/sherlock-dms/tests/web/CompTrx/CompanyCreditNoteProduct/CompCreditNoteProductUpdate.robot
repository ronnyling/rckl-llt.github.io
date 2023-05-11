*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CompTrx/CompDebitNoteProduct/CompDebitNoteProductAddPage.py
Library         ${EXECDIR}${/}resources/web/CompTrx/CompCreditNoteProduct/CompCreditNoteProductAddPage.py
Library         ${EXECDIR}${/}resources/web/CompTrx/CompCreditNoteProduct/CompCreditNoteProductListPage.py
Library         ${EXECDIR}${/}resources/web/CompTrx/CompanyInvoice/CompInvoiceAddPage.py

*** Test Cases ***
1 - Able to create company credit note product and validate tax is calculated correct (tax on tax,net,gross)
    [Documentation]    Able to create company credit note product
    [Tags]     distadm    9.2
    ${CNDetails}=    create dictionary
    ...    Warehouse=whtt
    ...    Supplier=taxsup
    set test variable     &{CNDetails}
    Given user navigates to menu Company Transaction | Credit Note (Product)
    When user creates company credit note product
    And user intends to insert product 'NikeShoes' with uom 'Each', Qty '10'
    And insert price '100' and discount '2'
    Then company credit note product created successfully with message 'Record created successfully'
    When user selects company credit note product to edit
    And user removes existing record
    And user intends to insert product 'NikeShoes' with uom 'Each', Qty '5'
    And insert price '200' and discount '3'
    Then company credit note product created successfully with message 'Record updated successfully'

2 - Able to create company credit note product and validate tax is calculated correct (accumulative tax)
    [Documentation]    Able to create company credit note product
    [Tags]     distadm    9.2
    ${CNDetails}=    create dictionary
    ...    Warehouse=whtt
    ...    Supplier=taxsup
    set test variable     &{CNDetails}
    Given user navigates to menu Company Transaction | Credit Note (Product)
    When user creates company credit note product
    And user intends to insert product 'NikeWatch' with uom 'BOX', Qty '10'
    And insert price '100' and discount '2'
    Then company credit note product created successfully with message 'Record created successfully'
    When user selects company credit note product to edit
    And user removes existing record
    And user intends to insert product 'NikeWatch' with uom 'BOX', Qty '5'
    And insert price '200' and discount '3'
    Then company credit note product created successfully with message 'Record updated successfully'

