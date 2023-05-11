*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/InvoiceTerm/InvoiceTermAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/InvoiceTerm/InvoiceTermListPage.py

*** Test Cases ***
1 - Able to Delete invoice term using random data
    [Tags]    distadm
    Given user navigates to menu Configuration | Reference Data | Invoice Terms
    When user creates invoice term with random data
    Then invoice term created successfully with message 'Record created successfully'
    When user selects invoice term to delete
    Then invoice term deleted successfully with message 'Record deleted'
