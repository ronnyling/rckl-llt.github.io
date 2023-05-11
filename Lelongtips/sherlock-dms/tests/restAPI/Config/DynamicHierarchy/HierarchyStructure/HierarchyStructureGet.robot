*** Settings ***

Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/StructureGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/HierarchyStructurePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/HierarchyStructureDelete.py


*** Test Cases ***
1 - Able to retrieves created prime hierarchy with hq admin
    [Documentation]    Able to retrieves created prime hierarchy with hq admin and expect return 200
    [Tags]     hqadm
    Given user retrieves token access as ${user_role}
    When user creates PRIME hierarchy structure with random data
    Then expected return status code 200
    When user retrieves created hierarchy structure
    Then expected return status code 200
    When user deletes created hierarchy structure
    Then expected return status code 200

2 - Unble to retrieves invalid hierarchy with hq admin
    [Documentation]   Unble to retrieves invalid hierarchy with hq admin and expect return 400
    [Tags]     hqadm
    Given user retrieves token access as ${user_role}
    When user retrieves invalid hierarchy structure
    Then expected return status code 400

3 - Unable to retrieves deleted hierarchy with hq admin
    [Documentation]   Unable to retrieves deleted hierarchy with hq admin and expect return 400
    [Tags]     hqadm
    Given user retrieves token access as ${user_role}
    When user creates PRIME hierarchy structure with random data
    Then expected return status code 200
    When user deletes created hierarchy structure
    Then expected return status code 200
    When user retrieves created hierarchy structure
    Then expected return status code 400

4 - Able to retrieves all node that created under product hierarchy structure
    [Documentation]    Able to retrieves all node that created under product hierarchy structure
    [Tags]     hqadm
    Given user retrieves token access as ${user_role}
    When user get hierarchy id by giving hierarchy structure name General Product Hierarchy
    Then expected return status code 200
    When user retrieves product hierarchy structure with valid data
    Then expected return status code 200

5 - Able to retrieves all node that created under customer hierarchy structure
    [Documentation]    Able to retrieves all node that created under customer hierarchy structure
    [Tags]     hqadm
    Given user retrieves token access as ${user_role}
    When user get hierarchy id by giving hierarchy structure name General Customer Hierarchy
    Then expected return status code 200
    When user retrieves product hierarchy structure with valid data
    Then expected return status code 200

6 - Unable to retrieve details when hierarchy structure is invalid
    [Documentation]    Unable to retrieve details when hierarchy structure is invalid and expect return 400
    [Tags]     hqadm
    Given user retrieves token access as ${user_role}
    When user retrieves details of hierarchy structure with invalid data
    Then expected return status code 204