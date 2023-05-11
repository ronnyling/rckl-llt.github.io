*** Settings ***

Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/ProductCustomerHierarchy/ValuePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/ProductCustomerHierarchy/ValuePut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/StructureGet.py
Library           Collections


*** Test Cases ***
1 - HQ user able to create new sales org structure
    [Documentation]    HQ user create new random node value for General Product Hierarchy at Brand level
    [Tags]     hqadm2    9.1    NRSZUANQ-29713
    Given user retrieve test data from "HierarchyListValueAPI.csv" located at "Config" folder
    ${hierarchy_details}=   get from dictionary   ${file_data}     HQ Admin
    Set test variable   &{hierarchy_details}
    And user retrieves token access as ${user_role}
    And user get hierarchy id by giving hierarchy structure name
    When user sends details to create new hierarchy node value from data
    ${Expected_Status_Code}=     get from dictionary    ${hierarchy_details}    Expected_Status_Code
    ${Expected_Status_Code}=     Convert to string   ${Expected_Status_Code}
    Then expected return status code ${Expected_Status_Code}     # assertion is performed on string values
    When user deletes node value
    Then expected return status code 200
