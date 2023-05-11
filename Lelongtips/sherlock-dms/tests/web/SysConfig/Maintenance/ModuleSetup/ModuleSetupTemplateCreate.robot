*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/SysConfig/Maintenance/ModuleSetup/ModuleSetupAddPage.py
Library         ${EXECDIR}${/}resources/web/SysConfig/Maintenance/ModuleSetup/ModuleSetupRelationshipAddPage.py
Library         ${EXECDIR}${/}resources/web/SysConfig/Maintenance/ModuleSetup/ModuleSetupActionAddPage.py
Library         ${EXECDIR}${/}resources/web/SysConfig/Maintenance/ModuleSetup/ModuleSetupFieldAddPage.py
Library         ${EXECDIR}${/}resources/web/SysConfig/Maintenance/ModuleSetup/ModuleSetupTemplateAddPage.py

*** Test Cases ***
1 - Able to create module setup using random data
    [Documentation]    Able to create module setup using random data
    [Tags]    sysimp    9.0
    When user navigates to menu System Configuration | Maintenance | Module Setup
    Then user creates module setup using random data
    And module setup created successfully with message 'Record created successfully'

2 - Able to create module setup using fixed data
    [Documentation]    Able to create module setup using fixed data
    [Tags]    sysimp    9.0
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
    ${ModuleSetupFieldsDetails}=    create dictionary
    ...    FIELD_LABEL=Fieldlbl
    ...    FIELD_DESC=Field For Metadata
    ...    FIELD_NAME=FieldName
    ...    FIELD_TYPE=Text
    ...    DISPLAY_TYPE=Textarea Field
    set test variable    ${ModuleSetupFieldsDetails}
    ${ModuleSetupTemplateDetails}=    create dictionary
    ...    TEMPLATE_NAME=TempName
    ...    TEMPLATE_DESCRIPTION=Template Name for Metadata
    set test variable    ${ModuleSetupTemplateDetails}
    Then user creates module setup template using fixed data
