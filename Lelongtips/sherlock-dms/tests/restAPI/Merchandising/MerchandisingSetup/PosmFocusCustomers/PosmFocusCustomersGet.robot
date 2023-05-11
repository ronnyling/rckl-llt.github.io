*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/PosmFocusCustomers/PosmFocusCustomersGet.py


*** Test Cases ***
1 - Able to retrieve posm focus customers
    [Documentation]  Able to retrieve posm focus customers
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user retrieves posm focus customers
    Then expected return status code 200