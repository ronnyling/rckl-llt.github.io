*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/SysConfig/Maintenance/ModuleSetup/ModuleSetupAddPage.py
Library         ${EXECDIR}${/}resources/web/SysConfig/Maintenance/ModuleSetup/ModuleSetupRelationshipAddPage.py
Library         ${EXECDIR}${/}resources/web/SysConfig/Maintenance/ModuleSetup/ModuleSetupActionAddPage.py

*** Test Cases ***
*** Test Cases ***
1 - Able to create module setup using random data
    [Documentation]    Able to create module setup using random data
    [Tags]    sysimp    9.1
    When user navigates to menu System Configuration | Maintenance | Module Setup
    Then user creates module setup using random data
    And module setup created successfully with message 'Record created successfully'

2 - Able to create module setup using fixed data
    [Documentation]    Able to create module setup using fixed data
    [Tags]    sysimp    9.1
    When user navigates to menu System Configuration | Maintenance | Module Setup
        ${ModuleSetupDetails}=    create dictionary
    ...    LOGICAL_ID=TestingFixedDataWithWeb
    ...    TITLE=TestingGivenDataWithWeb
    set test variable    ${ModuleSetupDetails}
    Then user creates module setup using fixed data
    ${ModuleSetupRelationshipDetails}=    create dictionary
    ...    LOGICAL_ID=ShamModuleId
    ...    RELATIONSHIP_TYPE=Contains
    set test variable    ${ModuleSetupRelationshipDetails}
    Then user creates module setup relationship using fixed data
     ${ModuleSetupActionsDetails}=    create dictionary
    ...    ACTION_TITLE=ActionTitle
    ...    ACTION_DESC=ActionDesc
    ...    ACTION_DISPLAY=Detail
    ...    ACTION_NAME=ActionName
    set test variable    ${ModuleSetupActionsDetails}
    Then user creates module setup actions using fixed data


3 - Able to edit action into module setup
    [Documentation]     Able to edit action into module setup
    [Tags]    sysimp    9.1
    When user navigates to menu System Configuration | Maintenance | Module Setup
    Then user click on list metadata configuration
    And user edit action
    Then action updated successfully with message 'Record updated successfully'

