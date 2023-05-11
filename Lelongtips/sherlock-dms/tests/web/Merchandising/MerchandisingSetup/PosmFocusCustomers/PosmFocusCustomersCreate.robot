*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/PosmFocusCustomers/PosmFocusCustomersAddPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/PosmFocusCustomers/PosmFocusCustomersListPage.py

*** Test Cases ***
1 - User able to add new posm to customer group
    [Documentation]  To validate user able to add new posm to customer group
    [Tags]    hqadm    9.2
    ${posm_details}=    create dictionary
    ...    LEVEL=B19
    ...    POSM_VALUE_CODE=B19A
    set test variable     &{posm_details}
    Given user navigates to menu Merchandising | Merchandising Setup | POSM Focus Customers
    When user navigates to ChannelB19 tab
    Then user adds posm
