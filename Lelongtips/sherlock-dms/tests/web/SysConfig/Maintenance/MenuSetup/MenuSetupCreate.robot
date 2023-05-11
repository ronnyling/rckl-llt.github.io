*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/SysConfig/Maintenance/MenuSetup/MenuSetupAddPage.py
Library         ${EXECDIR}${/}resources/web/SysConfig/Maintenance/MenuSetup/MenuSetupListPage.py

*** Test Cases ***
1 - Able to create menu setup using random data
    [Documentation]    Able to create menu setup using random data
    [Tags]    sysimp    9.0
    When user navigates to menu System Configuration | Maintenance | Menu Setup
    Then user creates menu setup using random data
    And module setup created successfully with message 'Record created successfully'

2 - Able to create folder menu setup using fixed data
    [Documentation]    Able to create folder menu setup using fixed data
    [Tags]    sysimp    9.0
    When user navigates to menu System Configuration | Maintenance | Menu Setup
    ${MenuSetupDetails}=    create dictionary
    ...    LABEL=TestingFolder
    ...    TYPE=0
    ...    SEQ_NUMBER=9999999
    set test variable    &{MenuSetupDetails}
    #  fixme: where is the middle step? where is Then user creates menu setup using fixed data?
    Then user verified menu setup is created    #fixme: is created? or created successfully (follow the standard)

3 - Able to create node menu setup using fixed data
    [Documentation]    Able to create node menu setup using fixed data
    [Tags]    sysimp    9.0
    When user navigates to menu System Configuration | Maintenance | Menu Setup
    ${MenuSetupDetails}=    create dictionary
    ...    LABEL=TestingNode
    ...    TYPE=1
    ...    SEQ_NUMBER=9999998
    ...    URL=/testingUrl
    set test variable    &{MenuSetupDetails}
    #  fixme: where is the middle step? where is Then user creates menu setup using fixed data?
    Then user verified menu setup is created    #fixme: is created? or created successfully (follow the standard)