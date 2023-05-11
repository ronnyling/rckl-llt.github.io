*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/CreditNoteProduct/CreditNoteProductListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/CreditNoteProduct/CreditNoteProductAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

*** Test Cases ***
1 - Unable to edit Principal field in edit screen
    [Documentation]    To update Credit Note with fixed data
    [Tags]     distadm    9.1     NRSZUANQ-31637
    ${CNDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    product=ProdAde1
    ...    productUom=PCK:2,PC:4
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Credit Note (Product)
    When user creates Prime credit note with fixed data
    Then credit note created successfully with message 'Record created'
    When user selects credit note to edit
    Then principal in credit note showing disabled
