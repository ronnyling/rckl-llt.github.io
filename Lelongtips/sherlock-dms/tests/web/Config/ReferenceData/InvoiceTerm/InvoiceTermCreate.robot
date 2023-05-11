*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/InvoiceTerm/InvoiceTermAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/InvoiceTerm/InvoiceTermListPage.py

*** Test Cases ***
1 - Able to Create Invoice Term using fixed data
    [Tags]   distadm
    ${invterm_details}=   create dictionary
    ...    invterm_cd=ABCDFA
    ...    invterm_desc=ABCDEFG8
    ...    invterm_days=12
    Given user navigates to menu Configuration | Reference Data | Invoice Terms
    When user creates invoice term with fixed data
    Then locality created successfully with message 'Record created successfully'
    When user selects invoice term to delete
    Then invoice term deleted successfully with message 'Record deleted'

2 - Able to Create Invoice Term using random data
    [Tags]   distadm
    Given user navigates to menu Configuration | Reference Data | Invoice Terms
    When user creates invoice term with random data
    Then locality created successfully with message 'Record created successfully'
    When user selects invoice term to delete
    Then invoice term deleted successfully with message 'Record deleted'