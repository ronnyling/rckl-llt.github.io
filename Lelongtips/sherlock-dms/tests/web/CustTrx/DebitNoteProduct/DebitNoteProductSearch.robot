*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/DebitNoteProduct/DebitNoteProductListPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library         ${EXECDIR}${/}resources/components/Pagination.py

*** Test Cases ***
1 - Able to search debit note product with principal field
    [Documentation]    Able to search debit note product with principal field when multi principal = On
    ...    This is not applicable for hqadm, sysimp
    [Tags]    distadm    9.1
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Debit Note (Product)
    When user searches debit note using random data
    Then principal listed successfully with searched data
