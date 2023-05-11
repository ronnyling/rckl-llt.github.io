*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxStructure/TaxStructurePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxStructure/TaxStructurePut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxStructure/TaxStructureGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxStructure/TaxStructureDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxGroup/TaxGroupPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

Test Teardown    user deletes tax structure prerequisite

*** Test Cases ***
1 - Able to edit tax structure using random data
    [Documentation]    Able to edit tax structure and return status code 201
    [Tags]   distadm    9.1
    [Setup]  run keywords
    ...   user switches On multi principal
    ...   AND   user creates supplier tax group prerequisite
    ...   AND   user retrieves token access as distadm
    ...   AND   user creates product tax group prerequisite
    When user creates tax structure with random data
    Then expected return status code 201
    ${TS_details} =  create dictionary
    ...    TAX_STRUCTURE_DESC=edited text
    set test variable  &{TS_details}
    When user edits created tax structure
    Then expected return status code 200
    When user deletes created tax structure
    Then expected return status code 200

2 - Unable to edit dist created tax structure when using hq credential
    [Documentation]
    [Tags]        distadm    9.1
    [Setup]  run keywords
    ...   user switches On multi principal
    ...   AND   user creates supplier tax group prerequisite
    ...   AND   user retrieves token access as distadm
    ...   AND   user creates product tax group prerequisite
    Given user retrieves token access as distadm
    When user creates tax structure with random data
    Then expected return status code 201
    ${TS_details} =  create dictionary
    ...    TAX_STRUCTURE_DESC=edited text
    set test variable  &{TS_details}
    Given user retrieves token access as hqadm
    When user edits created tax structure
    Then expected return status code 404
    Given user retrieves token access as distadm
    When user deletes created tax structure
    Then expected return status code 200

3 - Unable to edit tax structure when setup is turned off
    [Documentation]    Able to edit tax structure and return status code 201
    [Tags]       distadm    9.1
    [Setup]  run keywords
    ...   user switches On multi principal
    ...   AND   user creates supplier tax group prerequisite
    ...   AND   user retrieves token access as distadm
    ...   AND   user creates product tax group prerequisite
    [Teardown]  run keywords
    ...   user switches on multi principal
    Given user retrieves token access as distadm
    When user creates tax structure with random data
    Then expected return status code 201
    ${TS_details} =  create dictionary
    ...    TAX_STRUCTURE_DESC=edited text
    set test variable  &{TS_details}
    When user switches off multi principal
    And user edits created tax structure
    Then expected return status code 404
    When user switches On multi principal
    And user deletes created tax structure
    Then expected return status code 200