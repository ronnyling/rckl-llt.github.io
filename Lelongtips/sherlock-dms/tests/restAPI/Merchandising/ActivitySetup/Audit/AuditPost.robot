*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/ActivitySetup/Audit/AuditPost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/ActivitySetup/Audit/AuditDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/StoreSpace/StoreSpaceGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/StructureGet.py

Test Setup    run keywords
...    user retrieves token access as ${user_role}
...    AND    user retrieves all store spaces
...    AND    user get hierarchy id by giving hierarchy structure name General Product Hierarchy
...    AND    user retrieves product hierarchy structure with valid data
...    AND    user retrieves Category hierarchy with Jam code

*** Test Cases ***
1 - Able to POST merchandising audit with random data
    [Documentation]  Able to add merchandising audit with random data
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user creates audit setup using random data
    Then expected return status code 201
    When user deletes created audit setup
    Then expected return status code 200

2 - Able to POST merchandising audit with fixed data
    [Documentation]  Able to add merchandising audit with random data
    [Tags]    hqadm    9.2
    ${audit_details}=    create dictionary
    ...    AUDIT_DESC=APIAUDDC
    ...    START_DATE=2023-02-01
    ...    END_DATE=2023-04-05
    set test variable  &{audit_details}
    Given user retrieves token access as hqadm
    When user creates audit setup using fixed data
    Then expected return status code 201
    When user deletes created audit setup
    Then expected return status code 200

3 - Unable to POST merchandising audit using distadm
    [Documentation]  Unable to add audit setup using distadm login
    [Tags]    distadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates audit setup using random data
    Then expected return status code 403
