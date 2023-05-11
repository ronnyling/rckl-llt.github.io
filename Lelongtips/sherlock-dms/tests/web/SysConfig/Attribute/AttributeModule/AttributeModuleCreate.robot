*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/SysConfig/Attribute/AttributeModule/AttributeModuleAddPage.py
Library         ${EXECDIR}${/}resources/web/SysConfig/Attribute/AttributeModule/AttributeModuleListPage.py
*** Test Cases ***
1 - Able to create attribute module to using given data
    [Documentation]    Able to create attribute Module To using given data
    [Tags]    sysimp    9.0
    ${AttributeModuleDetails}=   create dictionary
    ...    amModule=Test attribute module
    set test variable     &{AttributeModuleDetails}
    Given user navigates to menu System Configuration | Attribute | Attribute Module
    When user creates attribute module using given data
    Then attribute module created successfully with message 'Record created successfully'

2 - Able to create attribute module to using random data
    [Documentation]    Able to create attribute module using random data
    [Tags]    sysimp    9.0
    Given user navigates to menu System Configuration | Attribute | Attribute Module
    When user creates attribute module using random data
    Then attribute Module created successfully with message 'Record created successfully'