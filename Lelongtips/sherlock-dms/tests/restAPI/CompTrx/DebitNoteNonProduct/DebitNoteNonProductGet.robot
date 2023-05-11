*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/DebitNoteNonProduct/DebitNoteNonProductGet.py
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/DebitNoteNonProduct/DebitNoteNonProductPost.py


*** Test Cases ***
1 - Able to GET all debit note non product
    [Documentation]  Able to retrieve all debit note non product
    [Tags]    distadm    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves debit note non product
    Then expected return status code 200

2 - Able to GET debit note non product by ID
    [Documentation]  Able to retrieve debit note non product by ID
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
    When user retrieves debit note non product
    Then expected return status code 200