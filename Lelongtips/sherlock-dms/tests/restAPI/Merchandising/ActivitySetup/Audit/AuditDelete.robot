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
...    AND    user retrieves Brand hierarchy with Hero code

*** Test Cases ***
1 - Able to delete created audit setup
    [Documentation]  Able to delete created audit setup
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user creates audit setup using random data
    Then expected return status code 201
    When user deletes created audit setup
    Then expected return status code 200

2 - Unable to delete created audit setup using distadm
    [Documentation]  Unable to add merchandising audit with random data
    [Tags]    distadm   9.2
    [Teardown]  run keywords
    ...    user retrieves token access as hqadm
    ...    user deletes created audit setup
    Given user retrieves token access as hqadm
    When user creates audit setup using random data
    Then expected return status code 201
    When user retrieves token access as ${user_role}
    And user deletes created audit setup
    Then expected return status code 403