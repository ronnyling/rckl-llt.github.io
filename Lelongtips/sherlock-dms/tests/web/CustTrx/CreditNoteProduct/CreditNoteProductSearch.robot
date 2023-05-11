*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/CreditNoteProduct/CreditNoteProductListPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

*** Test Cases ***
1 - Able to search Credit Note using principal field
    [Documentation]    Able to search Credit Note with principal field when multi principal = On
    [Tags]     distadm  9.1    NRSZUANQ-31612
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Credit Note (Product)
    When user searches credit note with random data
    And principal listed successfully with searched data
