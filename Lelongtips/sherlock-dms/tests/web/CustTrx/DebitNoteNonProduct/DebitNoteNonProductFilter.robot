*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/DebitNoteNonProduct/DebitNoteNonProductListPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

*** Test Cases ***
1 - Able to filter debit note non product with principal field
    [Documentation]    Able to filter debit note with principal field when multi principal = On
    ...    This is not applicable to hqadm, sysimp
    [Tags]    distadm    9.1
    ${FilterDetails}=    create dictionary
    ...    principal=Prime
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Debit Note (Non Product)
    When user filters debit note using fixed data
    Then principal listed successfully with Prime data



