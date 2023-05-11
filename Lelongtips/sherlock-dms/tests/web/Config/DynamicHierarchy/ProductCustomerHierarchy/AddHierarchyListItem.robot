*** Settings ***
Resource            ${EXECDIR}${/}tests/web/common.robot
Library             ${EXECDIR}${/}resources/web/Config/DynamicHierarchy/ProductCustomerHierarchy/ProductCustomerHierarchyList.py
Library             Collections


*** Test Cases ***
1 - HQ Admin add new customer type with random code and description
    [Documentation]    HQ Admin add new customer type with random code and description
    [Tags]    hqadm       NRSZUANQ-28052      9.1
    Given user retrieve test data from "HierarchyListValue.csv" located at "Config" folder
    ${hierarchy_details}=   get from dictionary   ${file_data}     HQ Admin
    When user navigates to menu Configuration | Dynamic Hierarchy | Product/Customer Hierarchy
    Then user creates new hierarchy list value with ${hierarchy_details}
    And created successfully with message 'New Entry Added successfully'
