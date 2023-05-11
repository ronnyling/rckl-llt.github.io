*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/ActivitySetup/Checklist/ChecklistListPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/ActivitySetup/Checklist/ChecklistAddPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/ActivitySetup/Checklist/ChecklistUpdatePage.py


*** Test Cases ***
1 - User able to update merchandising checklist with random data
    [Documentation]  To validate user able to update merchandising checklist with random data
    [Tags]    hqadm    9.2
    Given user navigates to menu Merchandising | Activity Setup | Checklist
    When user creates merchandising checklist using random data
    Then merchandising checklist created successfully with message 'Record created successfully'
    When user selects merchandising checklist to edit
    And user updates merchandising checklist using random data
    Then merchandising checklist updated successfully with message 'Record updated successfully'
    When user selects merchandising checklist to delete
    Then merchandising checklist deleted successfully with message 'Record deleted'

2 - User able to update merchandising checklist with fixed data
    [Documentation]  To validate user able to update merchandising checklist with fixed data
    [Tags]    hqadm    9.2
    ${checklist_details}=    create dictionary
    ...    CHECKLIST_DESC=CLUPDATE
    ...    ACTIVITY_CODE=ACTUPDATE
    ...    ACTIVITY_DESC=Activity Update
    set test variable     &{checklist_details}
    Given user navigates to menu Merchandising | Activity Setup | Checklist
    When user creates merchandising checklist using random data
    Then merchandising checklist created successfully with message 'Record created successfully'
    When user selects merchandising checklist to edit
    And user updates merchandising checklist using fixed data
    Then merchandising checklist updated successfully with message 'Record updated successfully'
    When user selects merchandising checklist to delete
    Then merchandising checklist deleted successfully with message 'Record deleted'
