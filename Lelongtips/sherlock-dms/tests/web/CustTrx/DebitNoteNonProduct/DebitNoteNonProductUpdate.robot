*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/DebitNoteNonProduct/DebitNoteNonProductListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/DebitNoteNonProduct/DebitNoteNonProductAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

*** Test Cases ***
1 - Unable to edit principal field in edit screen
    [Documentation]    To update debit note non product using fixed data
    [Tags]    distadm    9.1
    ${DNDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    product=ProdAde1
    ...    productUom=PCK:2,PC:4
    set test variable     ${DNDetails}
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Debit Note (Non Product)
    When user creates Prime debit note non product using fixed data
    Then debit note non product created successfully with message 'Record added'
    When user selects debit note non product to edit
    Then principal in debit note non product showing disabled
