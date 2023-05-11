*** Settings ***
Resource          ${EXECDIR}${/}tests/web/common.robot
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library           ${EXECDIR}${/}resources/web/Telesales/OutletNote/OutletNoteAddPage.py
Library           ${EXECDIR}${/}resources/web/Telesales/OutletNote/OutletNoteListPage.py

*** Test Cases ***
1 - Able to view created outlet note
   [Documentation]    To test that user is able to view outlet note
   [Tags]    telesales    hqtelesales    9.3
   [Teardown]  run keywords
   ...    user clicks cancel button
   ...    AND       user logouts and closes browser
   ${note_details}=    create dictionary
    ...    customer=CT0000001549
    set test variable     &{note_details}
    Given user navigates to menu Telesales | My Stores
    And user selects customer for call
    And user clicks on Outlet Note tab
    When user selects outlet note to view

2 - Able to cancel outlet note selection
   [Documentation]    To test that user is able to cancel outlet note selection
   [Tags]    telesales    hqtelesales    9.3
   ${note_details}=    create dictionary
    ...    customer=CT0000001549
    set test variable     &{note_details}
    Given user navigates to menu Telesales | My Stores
    And user selects customer for call
    And user clicks on Outlet Note tab
    When user selects outlet note to view
    Then validate able to cancel the outlet note selection

