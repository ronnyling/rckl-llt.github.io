*** Settings ***
Resource          ${EXECDIR}${/}tests/web/common.robot
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library           ${EXECDIR}${/}resources/web/Telesales/OutletNote/OutletNoteListPage.py

*** Test Cases ***
1 - Able to search outlet note
   [Documentation]    To test that user is able to search outlet note
   [Tags]    telesales    hqtelesales    9.3
   ${note_details}=    create dictionary
    ...    spokeTo=Bruce Wayne
    ...    note=CXTESTTAX OutletNote Dist
    ...    customer=CT0000001549
    set test variable     &{note_details}
    Given user navigates to menu Telesales | My Stores
    And user selects customer for call
    And user clicks on Outlet Note tab
    When user searches outlet note in listing
    Then record display in listing successfully

2 - Able to filter outlet note
   [Documentation]    To test that user is able to filter outlet note
   [Tags]    telesales    hqtelesales    9.3
   ${note_details}=    create dictionary
    ...    spokeTo=Bruce Wayne
    ...    note=CXTESTTAX OutletNote Dist
    ...    customer=CT0000001549
    set test variable     &{note_details}
    Given user navigates to menu Telesales | My Stores
    And user selects customer for call
    And user clicks on Outlet Note tab
    When user filters outlet note in listing
    Then record display in listing successfully

3- Validate outlet note columns displayed correctly
   [Documentation]    To validate the column display of outlet note listing
   [Tags]    telesales    hqtelesales    9.3
      ${note_details}=    create dictionary
    ...    customer=CT0000001549
    set test variable     &{note_details}
    Given user navigates to menu Telesales | My Stores
    And user selects customer for call
    And user clicks on Outlet Note tab
    Then validate the column display for outlet note
