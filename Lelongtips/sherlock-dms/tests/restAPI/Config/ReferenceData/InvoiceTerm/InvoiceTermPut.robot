*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/InvoiceTerm/InvoiceTermPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/InvoiceTerm/InvoiceTermDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/InvoiceTerm/InvoiceTermPut.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py

*** Test Cases ***
1 - Able to edit invoice term with random data
    [Documentation]  To edit invoice term with random generated data by passing in id via API
    [Tags]    distadm     9.0
    Given user retrieves token access as hqadm
    And user gets distributor by using code 'DistEgg'
    When user creates invoice term as prerequisite
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user edits invoice term with random data
    Then expected return status code 200
    When user deletes invoice term as teardown
    Then expected return status code 200

2- Able to edit Invoice Term with fixed data
    [Documentation]  To edit invoice term with fixed data by passing in id via API
    [Tags]    distadm     9.0
    Given user retrieves token access as hqadm
    And user gets distributor by using code 'DistEgg'
    When user creates invoice term as prerequisite
    Then expected return status code 200
    ${invoice_term_header}=    create dictionary
    ...     TERMS=TERM NUMBER
    ...     TERMS_DAYS=30
    ...     TERMS_DESC=Term is description
    ${invoice_term_details}=    create dictionary
    ...     DISC_PERC=${2}
    ...     INV_DUE_DAYS=15
    Given user retrieves token access as ${user_role}
    When user edits invoice term with fixed data
    Then expected return status code 200
    When user deletes invoice term as teardown
    Then expected return status code 200