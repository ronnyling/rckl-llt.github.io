*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/SysConfig/Maintenance/ModuleSetup/ModuleSetupAddPage.py
Library         ${EXECDIR}${/}resources/web/SysConfig/Maintenance/ModuleSetup/ModuleSetupListPage.py

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
    # fixme: when you are providing data above, but i have no idea where above data will be taken action at, so where is the step? like 'user creates module setup using fixed data'
    And user verified module setup is created  #fixme: is created? or created successfully (follow the standard)
