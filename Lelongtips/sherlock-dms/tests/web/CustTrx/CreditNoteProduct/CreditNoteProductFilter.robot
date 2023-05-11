*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/CreditNoteProduct/CreditNoteProductListPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

*** Test Cases ***
1 - Able to filter credit note using principal field
    [Documentation]    Able to filter Credit note with principal field when multi principal = On
    [Tags]     distadm  9.1    NRSZUANQ-31611
    ${FilterDetails}=    create dictionary
    ...    principal=Prime
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Credit Note (Product)
    When user filters credit note with fixed data
    Then principal listed successfully with Prime data



