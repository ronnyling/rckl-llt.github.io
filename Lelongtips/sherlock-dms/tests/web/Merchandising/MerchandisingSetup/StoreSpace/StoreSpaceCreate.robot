*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/StoreSpace/StoreSpaceAddPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/StoreSpace/StoreSpaceListPage.py

*** Test Cases ***
1- User able to create new store space with random data
    [Documentation]  To validate user able to add new store space with random data
    [Tags]      9.1    hqadm    NRSZUANQ-20802      BUG:NRSZUANQ-48566
    Given user navigates to menu Merchandising | Merchandising Setup | Store Space
    When user creates store space using random data
    Then store space created successfully with message 'Record created successfully'

2- Not able to add same store space code
    [Documentation]  To validate user unable to add new store space with same store space code
    [Tags]      9.1    hqadm    NRSZUANQ-20806       BUG:NRSZUANQ-48566
    ${setup_details}=    create dictionary
    ...    space_code=CDSTSP001
    ...    space_desc=DESC SP DESC
    set test variable     &{setup_details}
    Given user navigates to menu Merchandising | Merchandising Setup | Store Space
    When user creates store space using random data
    Then store space created successfully with message 'Record created successfully'
    When user creates store space using existing data
    Then expect pop up message : Conflict : Merc Store Space found with Space Code

3- Not able to add store space using empty store space code
    [Documentation]  To validate user unable to add store space using empty data
    [Tags]      9.1    hqadm    NRSZUANQ-20836      BUG:NRSZUANQ-48566
    ${setup_details}=    create dictionary
    ...    space_code=${Empty}
    ...    space_desc=${Empty}
    set test variable     &{setup_details}
    Given user navigates to menu Merchandising | Merchandising Setup | Store Space
    When user creates store space using fixed data
    Then expect pop up message: Invalid payload: SPACE_CD should not be shorter than 3 characters SPACE_DESC should not be shorter than 3 characters SPACE_DESC No leading spaces and double spaces is allowed.

4- Able to assign customer to store space
    [Documentation]  To validate user able to assign customer to store space
    [Tags]      9.1    hqadm   NRSZUANQ-27475      BUG:NRSZUANQ-48566
    Given user navigates to menu Merchandising | Merchandising Setup | Store Space
    When user creates store space using random data
    Then store space created successfully with message 'Record created successfully'
    When user assign customer assignment which is present
    Then customer assigned successfully with message 'Record created successfully'

5- User able to remove customer assignment from store space
    [Documentation]  To validate user able to remove customer assignment from store space
    [Tags]      9.1    hqadm      BUG:NRSZUANQ-48566
    Given user navigates to menu Merchandising | Merchandising Setup | Store Space
    When user creates store space using random data
    Then store space created successfully with message 'Record created successfully'
    When user assign customer assignment which is present
    Then customer assigned successfully with message 'Record created successfully'
    When user validate customer assigned is listed in the table and select to delete
    Then customer assigned deleted successfully with message 'Record deleted successfully'
    When user selects store space to delete
    Then store space deleted successfully with message 'Record deleted successfully'

6- User unable to select the same assigned customer from list
    [Documentation]  To validate user unable to select the same assigned customer from the list
    [Tags]      9.1    hqadm      BUG:NRSZUANQ-48566
    Given user navigates to menu Merchandising | Merchandising Setup | Store Space
    When user creates store space using random data
    Then store space created successfully with message 'Record created successfully'
    When user assign customer assignment which is present
    Then customer assigned successfully with message 'Record created successfully'
    When validate the assigned customer not in list
    And user validate customer assigned is listed in the table and select to delete
    Then customer assigned deleted successfully with message 'Record deleted successfully'
    When user selects store space to delete
    Then store space deleted successfully with message 'Record deleted successfully'

7- Verify the application setup data display at level dropdown
    [Documentation]  To validate user unable to uncheck the assigned customer from the list
    [Tags]      9.1    hqadm   DrpLevel      BUG:NRSZUANQ-48566
    Given user navigates to menu Configuration | Application Setup
    When user retrieves merchandising setup data
    And user navigates to menu Merchandising | Merchandising Setup | Store Space
    And user creates store space using random data
    Then store space created successfully with message 'Record created successfully'
    When user validates the dropdown customer data
    Then correct customer hierarchy displayed successfully

8- Verify the Store Space Code and description should have maximum length set
    [Documentation]  To validate user unable to insert length more than maximum length
    [Tags]      9.1    hqadm   NRSZUANQ-21000      BUG:NRSZUANQ-48566
    ${setup_details}=    create dictionary
    ...    space_code=abcdefghij1234567890klmnopqrst123456790
    ...    space_desc=12345abcde12345fghij12345klmno12345pqrst12345uvwxy12345
    set test variable  &{setup_details}
    Given user navigates to menu Merchandising | Merchandising Setup | Store Space
    When user creates store space using maximum data
    Then data will be limited to set length


