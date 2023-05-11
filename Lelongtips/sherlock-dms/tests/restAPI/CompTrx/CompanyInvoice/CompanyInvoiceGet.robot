*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/CompanyInvoice/CompanyInvoiceGet.py


*** Test Cases ***
1 - Able to retrieve all company invoice
    [Documentation]  Able to retrieve company invoice
    [Tags]    distadm    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves all company invoice
    Then expected return status code 200

2 - Able to retrieve company invoice using ID
    [Documentation]    Able to retrieve company invoice using id
    [Tags]    distadm
    Given user retrieves token access as ${user_role}
    When user retrieves company invoice by id
    Then expected return status code 200

3 - Unable to retrieve company invoice using invalid ID and get 404
    [Documentation]    Unable to retrieve picklist using invalid ID
    [Tags]    distadm
    Given user retrieves token access as ${user_role}
    set test variable   ${inv_id}      32D316B7:CECF2E0C-9DCD-4667-B7AA-CD8EDBB3B000
    When user retrieves company invoice by id
    Then expected return status code 404

4 - Unable to retrieve all company invoice using HQ access and get 403
    [Documentation]  Unable to retrieve company invoice using other than distributor user
    [Tags]    hqadm
    Given user retrieves token access as hqadm
    When user retrieves all company invoice
    Then expected return status code 403

5 - Able to retrieve company invoice by ID using HQ access and get 403
    [Documentation]   Unable to retrieve company invoice by id using other than distributor user
    [Tags]    hqadm
    Given user retrieves token access as hqadm
    When user retrieves company invoice by id
    Then expected return status code 403