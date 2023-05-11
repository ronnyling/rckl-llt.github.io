*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/StoreSpace/StoreSpaceAddPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/StoreSpace/StoreSpaceUpdatePage.py

*** Test Cases ***
1- User able to edit store space with random data
    [Documentation]  To validate user able to edit store space with random data
    [Tags]      9.1    hqadm   NRSZUANQ-20804   NRSZUANQ-21667      BUG:NRSZUANQ-48566
    Given user navigates to menu Merchandising | Merchandising Setup | Store Space
    When user creates store space using random data
    Then store space created successfully with message 'Record created successfully'
    When user edits store space using random data
    Then store space updated successfully with message 'Record created successfully'

2- Not able to edit store space description using invalid data
    [Documentation]  To validate user unable to edit store space description using invalid data
    [Tags]      9.1   hqadm    NRSZUANQ-20807    NRSZUANQ-21900      BUG:NRSZUANQ-48566
    Given user navigates to menu Merchandising | Merchandising Setup | Store Space
    When user creates store space using random data
    Then store space created successfully with message 'Record created successfully'
    When user edits store space using invalid description
    Then expect pop up message : Invalid payload: SPACE_DESC should not be shorter than 3 characters SPACE_DESC No leading spaces and double spaces is allowed.


