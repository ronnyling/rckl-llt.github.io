*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Telesales/Dashboard/MSLProductAndPercentageGet.py

*** Test Cases ***
1 - Able to GET MSL Products and MSL percentage in Dashboard
    [Documentation]  To test get MSL Products and MSL percentage in Dashboard via API
    [Tags]    telesales      hqtelesales     9.3     NRSZUANQ-57997
     ${MSL_details}=    create dictionary
     ...     CUST_CD=CT0000001549
    set test variable   &{MSL_details}
    Given user retrieves token access as ${user_role}
    When user retrieves all MSL Products and MSL Percentage
    Then expected return status code 200