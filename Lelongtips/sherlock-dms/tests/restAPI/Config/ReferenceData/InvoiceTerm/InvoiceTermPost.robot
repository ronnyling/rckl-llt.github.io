*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/InvoiceTerm/InvoiceTermPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/InvoiceTerm/InvoiceTermDelete.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py

Test Setup     run keywords
...    user retrieves token access as ${user_role}
...    AND    user gets distributor by using code 'DistEgg'
Test Teardown  user deletes invoice term as teardown
*** Test Cases ***
1 - Able to create Invoice Term with random data
    [Documentation]  To create invoice term with random generated data via API
    [Tags]    distadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates invoice term with random data
    Then expected return status code 200

2- Able to create Invoice term with fixed data
    [Documentation]  To create invoice term with random generated data via API
    [Tags]    distadm    9.0
    ${invoice_term_header}=    create dictionary
    ...     TERMS=TERM NUMBER
    ...     TERMS_DAYS=23
    ...     TERMS_DESC=Term description
    ${invoice_term_details}=    create dictionary
    ...     DISC_PERC=${5}
    ...     INV_DUE_DAYS=10
    Given user retrieves token access as ${user_role}
    When user creates invoice term with fixed data
    Then expected return status code 200

3- Unable to create invoice term using HQ Access and return 403
    [Documentation]  Unable to create invoice term using HQ Acess
    [Teardown]
    [Tags]     hqadm     9.0
    Given user retrieves token access as ${user_role}
    When user creates invoice term with random data
    Then expected return status code 403