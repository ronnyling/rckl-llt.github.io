*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/CreditNoteProduct/CreditNoteProductListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/CreditNoteProduct/CreditNoteProductAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

*** Test Cases ***
1 - Verify Principal default to Prime in Credit Note when Multi Principal = On
    [Documentation]    Verify Credit Note having Principal default to Prime when multi principal = On
    [Tags]     distadm    9.1     NRSZUANQ-31614
    #Switches off multi principal first to check if principal column showing
    Given user switches Off multi principal
    When user navigates to menu Customer Transaction | Credit Note (Product)
    Then user verify credit note defaults to prime

2 - Verify Principal not displaying in Credit Note when Multi Principal = Off
    [Documentation]    Verify Credit Note not having Principal field when multi principal = Off
    [Tags]     distadm    9.1     NRSZUANQ-31613
    Given user switches Off multi principal
    When user navigates to menu Customer Transaction | Credit Note (Product)
    Then principal column not visible in credit note listing
    And user switches On multi principal