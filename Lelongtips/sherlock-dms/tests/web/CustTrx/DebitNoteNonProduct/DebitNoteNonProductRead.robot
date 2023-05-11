*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/DebitNoteNonProduct/DebitNoteNonProductListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/DebitNoteNonProduct/DebitNoteNonProductAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

*** Test Cases ***
1 - Verify principal default to prime in debit note non product when multi principal = On
    [Documentation]    Verify debit note non product having principal default to Prime when multi principal = On
    ...    This is not applicable to hqadm, sysimp
    [Tags]    distadm    9.1
    Given user switches On multi principal
    When user navigates to menu Customer Transaction | Debit Note (Non Product)
    And user creates new debit note non product
    Then principal field displaying in debit note non product

2 - Verify principal not displaying in debit note non product when multi principal = Off
    [Documentation]    Verify debit note non product not having Principal field when multi principal = Off
    ...    This is not applicable to hqadm, sysimp
    [Tags]     distadm    9.1
    Given user switches Off multi principal
    When user navigates to menu Customer Transaction | Debit Note (Non Product)
    And user creates new debit note non product
    Then principal field not displaying in debit note non product