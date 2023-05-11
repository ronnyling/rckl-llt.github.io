*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/CreditNoteNonProduct/CreditNoteNonProductListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/CreditNoteNonProduct/CreditNoteNonProductAddPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/CreditNoteNonProduct/CreditNoteNonProductEditPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesInvoice/SalesInvoiceListPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

*** Test Cases ***
1 - Able to updates credit note non product using fixed data
    [Documentation]    To update credit note non product using fixed data
    [Tags]    distadm    9.1
    ${CNNPDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Credit Note (Non Product)
    When user creates Prime credit note non product using fixed data
    Then credit note non product created successfully with message 'Record created successfully'
    ${CNNPDetails}=    create dictionary
    ...    ItemRefNo=RefEdited
    ...    ItemRemark=Edit Remark
    ...    ItemAmt=5
    set test variable     ${CNNPDetails}
    When user selects credit note non product to edit
    And user updates Prime credit note non product using fixed data
    Then credit note non product updated successfully with message 'Record updated successfully'
