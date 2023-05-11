*** Settings ***

Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/HierarchyStructurePut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/StructureGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/HierarchyStructurePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/HierarchyStructureDelete.py

*** Test Cases ***

1 - Able to updates created hierarchy strcuture by hq admin
    [Documentation]    Able to updates created hierarchy strcuture with random data and expect return 200
    [Tags]     hqadm
    Given user retrieves token access as ${user_role}
    When user creates PRIME hierarchy structure with random data
    Then expected return status code 200
    When user retrieves created hierarchy structure
    Then expected return status code 200
    When user updates created hierarchy structure with valid data
    Then expected return status code 200
    When user deletes created hierarchy structure
    Then expected return status code 200

2 - Unable to updates invalid hierarchy strcuture by hq admin
    [Documentation]  Unable to updates invalid hierarchy strcuture and expect return 400
    [Tags]     hqadm
    Given user retrieves token access as ${user_role}
    When user creates PRIME hierarchy structure with random data
    Then expected return status code 200
    When user retrieves created hierarchy structure
    Then expected return status code 200
    When user updates invalid hierarchy structure with valid data
    Then expected return status code 400
    When user deletes created hierarchy structure
    Then expected return status code 200

3 - Able to updates created hierarchy strcuture with fix data by hq admin
    [Documentation]    Able to updates created hierarchy strcuture with fix data and expect return 200
    [Tags]     hqadm
    ${update_hier_details} =  create dictionary
    ...    hierDesc=updated
    Given user retrieves token access as ${user_role}
    When user creates PRIME hierarchy structure with random data
    Then expected return status code 200
    When user retrieves created hierarchy structure
    Then expected return status code 200
    When user updates created hierarchy structure with valid data
    Then expected return status code 200
    When user deletes created hierarchy structure
    Then expected return status code 200
