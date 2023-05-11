*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/SysConfig/Maintenance/ModuleSetup/ModuleSetupAddPage.py
Library         ${EXECDIR}${/}resources/web/SysConfig/Maintenance/ModuleSetup/ModuleSetupRelationshipAddPage.py

*** Test Cases ***
1 - Able to create module setup relationship using random data
    [Documentation]    Able to create module setup relationship using random data
    [Tags]    sysimp    9.1
    When user navigates to menu System Configuration | Maintenance | Module Setup
    Then user creates module setup using random data
    And module setup created successfully with message 'Record created successfully'
    Then user creates module setup relationship using random data

2 - Able to create module setup relationship using fixed data
    [Documentation]    Able to create module setup relationship using fixed data
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
#    # fixme: when you are providing data above, but i have no idea where above data will be taken action at, so where is the step? like 'user creates module setup using fixed data'
#    And user verified module setup is created  #fixme: is created? or created successfully (follow the standard)
