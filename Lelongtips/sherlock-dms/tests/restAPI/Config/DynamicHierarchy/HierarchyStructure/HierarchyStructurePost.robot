*** Settings ***

Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/StructureGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/HierarchyStructurePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/HierarchyStructureDelete.py
Library           Collections


*** Test Cases ***
1 - Able to create prime hierarchy with hq admin
    [Documentation]    Able to create prime hierarchy with hq admin and expect return 200
    [Tags]     hqadm
    Given user retrieves token access as ${user_role}
    When user creates PRIME hierarchy structure with random data
    Then expected return status code 200
    When user retrieves created hierarchy structure
    Then expected return status code 200
    When user deletes created hierarchy structure
    Then expected return status code 200


