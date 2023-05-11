*** Settings ***

Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/StructureGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/HierarchyStructurePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/HierarchyStructureDelete.py


*** Test Cases ***
1 - Able to delete created prime hierarchy with hq admin
    [Documentation]   Able to delete created prime hierarchy with hq admin and expect return 200
    [Tags]     hqadm
    Given user retrieves token access as ${user_role}
    When user creates PRIME hierarchy structure with random data
    Then expected return status code 200
    When user retrieves created hierarchy structure
    Then expected return status code 200
    When user deletes created hierarchy structure
    Then expected return status code 200

2 - Unble to delete invalid hierarchy with hq admin
    [Documentation]   Unble to delete invalid hierarchy structure and expect return 400
    [Tags]     hqadm
    Given user retrieves token access as ${user_role}
    When user deletes invalid hierarchy structure
    Then expected return status code 400

3 - Unable to delete deleted hierarchy with hq admin
    [Documentation]   Unable to delete deleted hierarchy and expect return 400
    [Tags]     hqadm
    Given user retrieves token access as ${user_role}
    When user creates PRIME hierarchy structure with random data
    Then expected return status code 200
    When user deletes created hierarchy structure
    Then expected return status code 200
    When user deletes created hierarchy structure
    Then expected return status code 400