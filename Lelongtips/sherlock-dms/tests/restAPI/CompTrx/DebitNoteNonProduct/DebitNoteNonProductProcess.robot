*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/DebitNoteNonProduct/DebitNoteNonProductPost.py
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/DebitNoteNonProduct/DebitNoteNonProductProcess.py

*** Test Cases ***
1 - Able to confirm debit note non product
    [Documentation]  Able to confirm debit note non product
    [Tags]    distadm    9.2
    ${dnnp_details}=    create dictionary
    ...    DIST=DistEgg
    ...    SUPPLIER=hqtax
    ...    SVC_CD=PrimeHQ001
    ...    AMOUNT=10
    ...    REASON=DebitReason
    set test variable  &{dnnp_details}
    Given user retrieves token access as ${user_role}
    When user creates debit note non product using fixed data
    Then expected return status code 201
    When user confirms debit note non product
    Then expected return status code 200
