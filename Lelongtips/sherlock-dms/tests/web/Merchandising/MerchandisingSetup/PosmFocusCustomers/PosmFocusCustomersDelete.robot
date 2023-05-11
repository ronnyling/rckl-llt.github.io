*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/PosmFocusCustomers/PosmFocusCustomersAddPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/PosmFocusCustomers/PosmFocusCustomersListPage.py

*** Test Cases ***
1 - User able to delete posm from customer group
    [Documentation]  To validate user able to delete posm from customer group
    [Tags]    hqadm    9.2
    ${posm_details}=    create dictionary
    ...    LEVEL=APRPosm1
    ...    POSM_VALUE_CODE=AP1001
    set test variable     &{posm_details}
    Given user navigates to menu Merchandising | Merchandising Setup | POSM Focus Customers
    When user navigates to ChannelB19 tab
    And user adds posm
    Then user deletes posm
