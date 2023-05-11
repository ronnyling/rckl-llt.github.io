*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/InvoiceTerm/InvoiceTermPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/InvoiceTerm/InvoiceTermDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py

*** Test Cases ***
1 - Able to delete invoice term with created data
    [Documentation]  To delete invoice term by passing in id via API
    ...   Testing pipeline by Jessie T
    [Tags]    distadm     9.0
    [Setup]  run keywords
    ...    user retrieves token access as hqadm
    ...    user gets distributor by using code 'DistEgg'
    ...    user creates invoice term as prerequisite
    Given user retrieves token access as ${user_role}
    When user deletes invoice term with created data
    Then expected return status code 200

2 - Unable to delete invoice term with created data using HQ access
    [Documentation]  Unable to delete invoice term by passing in id via API
    [Tags]    hqadm     9.0
    [Setup]  run keywords
    ...    user retrieves token access as hqadm
    ...    AND    user gets distributor by using code 'DistEgg'
    ...    AND    user creates invoice term as prerequisite
    Given user retrieves token access as ${user_role}
    When user deletes invoice term with created data
    Then expected return status code 403

