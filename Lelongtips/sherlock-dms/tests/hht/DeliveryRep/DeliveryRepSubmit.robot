*** Settings ***
Resource        ${EXECDIR}/tests/hht/common.robot
Resource        ${EXECDIR}${/}tests/hht/common.robot
Library         ${EXECDIR}${/}resources/hht/DeliveryRep/DeliveryRepSubmit.py

*** Test Cases ***

1 - Able to submit data for Picklist Product Summary and Van Stock Count
    [Documentation]    To test user able to submit data for table TXN_DELIVERY_VANCOUNT and TXN_PRDVANINV_PICKLIST
    [Tags]    deliveryperson     9.2    NRSZUANQ-46631    NRSZUANQ-47381
    Given pull emulator db into local
    Then validate data is submitted