*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CompTrx/CompanyInvoice/CompInvoiceAddPage.py
Library         ${EXECDIR}${/}resources/web/CompTrx/CompanyInvoice/CompInvoiceListPage.py

*** Test Cases ***
1 - Able to create company invoice and validate tax is calculated correct (tax on tax,net,gross)
    [Documentation]    Able to create company invoice
    [Tags]     distadm   9.2
    ${CIDetails}=    create dictionary
    ...    Warehouse=whtt
    ...    Supplier=taxsup
    set test variable     &{CIDetails}
    Given user navigates to menu Company Transaction | Company Invoice
    When user creates company invoice
    And user intends to insert product 'NikeShoes' with uom 'EAH', Invoice Qty. '10', Received Qty. '10'
    And insert price '100' and discount '2' then confirm company invoice
    Then Company Invoice created successfully with message 'Record created Successfully'
    And validated inventory movement from INVT_MASTER, INVT_MASTER_HIS, INVT_TEMP is correct

2 - Able to create company invoice and validate tax is calculated correct (accumulative tax)
    [Documentation]    Able to create company invoice
    [Tags]     distadm    9.2
    ${CIDetails}=    create dictionary
    ...    Warehouse=whtt
    ...    Supplier=taxsup
    set test variable     &{CIDetails}
    Given user navigates to menu Company Transaction | Company Invoice
    When user creates company invoice
    And user intends to insert product 'NikeWatch' with uom 'BOX', Invoice Qty. '10', Received Qty. '10'
    And insert price '100' and discount '2' then confirm company invoice
    Then Company Invoice created successfully with message 'Record created Successfully'