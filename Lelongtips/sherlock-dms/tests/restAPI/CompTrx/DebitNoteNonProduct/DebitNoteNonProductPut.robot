*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/DebitNoteNonProduct/DebitNoteNonProductPost.py
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/DebitNoteNonProduct/DebitNoteNonProductPut.py

*** Test Cases ***
1 - Able to PUT debit note non product
    [Documentation]  Able to update debit note non product
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
    ${dnnp_details}=    create dictionary
    ...    DIST=DistEgg
    ...    SUPPLIER=hqtax
    ...    SVC_CD=ServiceGeo
    ...    AMOUNT=10
    ...    REASON=DebitReason
    set test variable  &{dnnp_details}
    When user updates debit note non product using fixed data
    Then expected return status code 200
