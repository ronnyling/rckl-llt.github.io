*** Settings ***
Resource            ${EXECDIR}${/}tests/web/common.robot
Library             ${EXECDIR}${/}resources/web/Config/DynamicHierarchy/DynamicHierarchyTree/DynamicHierarchyTreeListPage.py
Library             ${EXECDIR}${/}resources/web/Config/DynamicHierarchy/DynamicHierarchyTree/DynamicHierarchyTreeAddPage.py
Library             Collections


*** Test Cases ***
1 - HQ Admin able to create new hierarchy structure
    [Documentation]    HQ Admin able to create new hierarchy structure
    [Tags]    hqadm       NRSZUANQ-28051      9.1
    Given user retrieve test data from "HierarchyStructure.csv" located at "Config" folder
    ${hierarchy_details}=   get from dictionary   ${file_data}     HQ Admin
    When user navigates to menu Configuration | Dynamic Hierarchy | Hierarchy Structure
    Then user creates new hierarchy structure with ${hierarchy_details}
    And created successfully with message 'Record updated successfully'
    Then user searches the newly created hierarchy structure with ${hierarchy_details}
    Then user deletes the newly created hierarchy structure with ${hierarchy_details}
#    And deleted successfully with message '1 record(s) deleted'
