*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/PosmFocusCustomers/PosmFocusCustomersPost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/MerchandisingSetup/PosmFocusCustomers/PosmFocusCustomersDelete.py

*** Test Cases ***
1 - Able to add posm focus customers
    [Documentation]  Able to add posm focus customers
    [Tags]    hqadm    9.2
    ${posm_details}=    create dictionary
    ...    CUSTOMER_GROUP_LEVEL=Channel
    ...    CUSTOMER_GROUP_VALUE=ChannelB19
    ...    POSM_VALUE=B19A
    set test variable  &{posm_details}
    Given user retrieves token access as hqadm
    When user adds posm focus customers using fixed data
    Then expected return status code 200
    When user deletes posm focus customers
    Then expected return status code 200



