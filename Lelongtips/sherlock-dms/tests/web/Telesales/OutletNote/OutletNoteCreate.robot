*** Settings ***
Resource          ${EXECDIR}${/}tests/web/common.robot
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library           ${EXECDIR}${/}resources/web/Telesales/OutletNote/OutletNoteAddPage.py

*** Test Cases ***
1 - Able to create new outlet note with fixed data
   [Documentation]    To test that user is able to create new outlet note
   [Tags]    telesales    hqtelesales    9.3
   ${note_details}=    create dictionary
    ...    spokeTo=Bruce Wayne
    ...    note=This note is created from UI automation
    ...    customer=CT0000001549
    set test variable     &{note_details}
    Given user navigates to menu Telesales | My Stores
    And user selects customer for call
    And user clicks on Outlet Note tab
    When user creates new outlet note with fixed data
    Then outlet note created successfully with message 'Record created successfully'

2 - Able to create new outlet note with random data
   [Documentation]    To test that user is able to create new outlet note
   [Tags]    telesales    hqtelesales    9.3
   ${note_details}=    create dictionary
    ...    spokeTo=Bruce Wayne
    ...    note=This note is created from UI automation
    ...    customer=CT0000001549
    set test variable     &{note_details}
    Given user navigates to menu Telesales | My Stores
    And user selects customer for call
    And user clicks on Outlet Note tab
    When user creates new outlet note with fixed data
    Then outlet note created successfully with message 'Record created successfully'

3- Validate unable to save the outlet note without note details
   [Documentation]    To test that user is unable to save without note details
   [Tags]    telesales    hqtelesales    9.3
   [Teardown]  run keywords
   ...    user clicks on Cancel button
   ...    AND       user logouts and closes browser
   ${note_details}=    create dictionary
    ...    customer=CT0000001549
    set test variable     &{note_details}
    Given user navigates to menu Telesales | My Stores
    And user selects customer for call
    And user clicks on Outlet Note tab
    When user clicks on Add button
    And user clicks on Save button
    Then validate the message on outlet note field

4- Able to cancel the outlet note details creation
   [Documentation]    To test that user is able to cancel the note creation
   [Tags]    telesales    hqtelesales    9.3
      ${note_details}=    create dictionary
    ...    customer=CT0000001549
    set test variable     &{note_details}
    Given user navigates to menu Telesales | My Stores
    And user selects customer for call
    And user clicks on Outlet Note tab
    When user clicks on Add button
    And user clicks on Cancel button