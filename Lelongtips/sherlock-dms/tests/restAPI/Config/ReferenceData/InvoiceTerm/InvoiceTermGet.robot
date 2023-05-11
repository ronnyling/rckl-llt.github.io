*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/InvoiceTerm/InvoiceTermPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/InvoiceTerm/InvoiceTermGet.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/InvoiceTerm/InvoiceTermDelete.py

*** Test Cases ***
1 - Able to retrieve all invoice term data and get 200
    [Documentation]  To retrieve all invoice term record via API
    [Tags]    distadm     9.0
    [Setup]   run keywords
    ...    user retrieves token access as hqadm
    ...    AND    user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user gets all invoice term data
    Then expected return status code 200

2 - Able to retrieve invoice term by using id
    [Documentation]  To retrieve locality by passing in ID via API
    [Tags]    distadm     9.0
    [Setup]  run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND    user gets distributor by using code 'DistEgg'
    ...    AND    user creates invoice term as prerequisite
    [Teardown]  user deletes invoice term as teardown
    Given user retrieves token access as ${user_role}
    When user gets invoice term by using id
    Then expected return status code 200
