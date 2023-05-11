*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CompTrx/CompanyInvoice/CompInvoiceAddPage.py
Library         ${EXECDIR}${/}resources/web/CompTrx/CompanyInvoice/CompInvoiceListPage.py

*** Test Cases ***
1 - Able to update company invoice and validate tax is calculated correct (tax on tax,net,gross)
    [Documentation]    Able to create company invoice
    [Tags]     distadm   9.2
    ${CIDetails}=    create dictionary
    ...    Warehouse=whtt
    ...    Supplier=taxsup
    set test variable     &{CIDetails}
    Given user navigates to menu Company Transaction | Company Invoice
    When user creates company invoice
    And user intends to insert product 'NikeShoes' with uom 'EAH', Invoice Qty. '10', Received Qty. '10'
    And insert price '100' and discount '2' then save company invoice
    Then Company Invoice created successfully with message 'Record created Successfully'
    Then user selects company invoice to edit
    And user intends to insert product 'NikeShirt' with uom 'EAH', Invoice Qty. '10', Received Qty. '10'
    And insert price '100' and discount '2' then save company invoice
    Then Company Invoice updated successfully with message 'Record created Successfully'


2 - Able to update company invoice and validate tax is calculated correct (accumulative tax)
    [Documentation]    Able to create company invoice
    [Tags]     distadm    9.2
    ${CIDetails}=    create dictionary
    ...    Warehouse=whtt
    ...    Supplier=taxsup
    set test variable     &{CIDetails}
    Given user navigates to menu Company Transaction | Company Invoice
    When user creates company invoice
    And user intends to insert product 'NikeWatch' with uom 'BOX', Invoice Qty. '10', Received Qty. '10'
    And insert price '100' and discount '2' then save company invoice
    Then Company Invoice created successfully with message 'Record created Successfully'
    Then user selects company invoice to edit
    And user intends to insert product 'NikeWatch' with uom 'BOX', Invoice Qty. '10', Received Qty. '10'
    And insert price '100' and discount '2' then save company invoice
    Then Company Invoice updated successfully with message 'Record created Successfully'