*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/CreditNoteNonProduct/CreditNoteNonProductListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/CreditNoteNonProduct/CreditNoteNonProductAddPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/CreditNoteNonProduct/CreditNoteNonProductViewPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesInvoice/SalesInvoiceListPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

*** Test Cases ***
1 - Able to view credit note non product using fixed data
    [Documentation]    To view credit note non product
    [Tags]    distadm    9.1
    ${CNNPDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Credit Note (Non Product)
    When user creates Prime credit note non product using fixed data
    Then credit note non product created successfully with message 'Record created successfully'
    When user selects credit note non product to check
    And confirm credit note
    And user selects credit note non product to view
    Then credit note non product displayed in View mode

