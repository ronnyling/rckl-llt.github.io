*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/CreditNoteNonProduct/CreditNoteNonProductPost.py
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/CreditNoteNonProduct/CreditNoteNonProductPut.py

*** Test Cases ***
1 - Able to PUT credit note non product
    [Documentation]  Able to update credit note non product
    [Tags]    distadm    9.2    cnnpPut
    ${cnnp_details}=    create dictionary
    ...    DIST=DistEgg
    ...    SUPPLIER=hqtax
    ...    SVC_CD=PrimeHQ001
    ...    AMOUNT=10
    ...    REASON=Reasoncode
    set test variable  &{cnnp_details}
    Given user retrieves token access as ${user_role}
    When user creates credit note non product using fixed data
    Then expected return status code 201
    ${cnnp_details}=    create dictionary
    ...    DIST=DistEgg
    ...    SUPPLIER=hqtax
    ...    SVC_CD=ServiceGeo
    ...    AMOUNT=10
    ...    REASON=Reasoncode
    set test variable  &{cnnp_details}
    When user updates credit note non product using fixed data
    Then expected return status code 200
