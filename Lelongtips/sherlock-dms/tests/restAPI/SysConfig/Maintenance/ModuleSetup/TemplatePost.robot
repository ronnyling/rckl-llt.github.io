*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Maintenance/ModuleSetup/FieldsPost.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Maintenance/ModuleSetup/TemplatePost.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Maintenance/ModuleSetup/ModuleSetupPost.py

*** Test Cases ***
1 - Able to create template in module setup using random data
    [Documentation]    Able to create template in module setup using random data
    ...    This is not applicable to distadm, hqadm
    [Tags]    sysimp    9.0
    Given user retrieves token access as ${user_role}
    When user creates module setup using random data
    Then expected return status code 201
    When user creates fields in module setup using random data
    Then expected return status code 201
    When user creates template in module setup using random data
    Then expected return status code 201

2 - Able to create template in module setup using fixed data panel
    [Documentation]    Able to create template in module setup using fixed data panel
    ...    This is not applicable to distadm, hqadm
    [Tags]    sysimp1    9.0
    Given user retrieves token access as ${user_role}
    When user creates module setup using random data
    Then expected return status code 201
    When user creates fields in module setup using random data
    Then expected return status code 201
    ${TemplateDetails}=    create dictionary
    ...    TYPE=TestPanel
    ...    DESCRIPTION=TestPanel
    ...    CONTENT=[{\"display_type\":\"panel\",\"columns\":2,\"title\":\"ab\",\"fields\":[\"test_field\"]}]
    set test variable    ${TemplateDetails}
    When user creates template in module setup using fixed data
    Then expected return status code 201

3 - Able to create template in module setup using fixed data tabs
    [Documentation]    Able to create template in module setup using fixed data
    ...    This is not applicable to distadm, hqadm
    [Tags]    sysimp    9.1
    Given user retrieves token access as ${user_role}
    When user creates module setup using random data
    Then expected return status code 201
    ${TemplateDetails}=    create dictionary
    ...    TYPE=TestTabs
    ...    DESCRIPTION=TestTabs
    ...    CONTENT=[{"display_type":"tabs","children":[{"display_type":"tab","title":"ShamTest","children":[{"display_type":null,"title":null,"fields":[]}]}]}]
    set test variable    ${TemplateDetails}
    When user creates template in module setup using fixed data
    Then expected return status code 201

4 - Able to create template in module setup using fixed data vertical tabs
    [Documentation]    Able to create template in module setup using fixed data vertical tabs
    ...    This is not applicable to distadm, hqadm
    [Tags]    sysimp    9.1
    Given user retrieves token access as ${user_role}
    When user creates module setup using random data
    Then expected return status code 201
    ${TemplateDetails}=    create dictionary
    ...    TYPE=TestVerticalTabs
    ...    DESCRIPTION=TestVerticalTabs
    ...    CONTENT=[{"display_type":"vertical-tabs","children":[{"display_type":"tab","title":"TestVertical","children":[{"display_type":null,"title":null,"fields":[]}]},{"display_type":"tab","title":"Tab 2","children":[{"display_type":null,"title":null,"fields":[]}]}]}]
    set test variable    ${TemplateDetails}
    When user creates template in module setup using fixed data
    Then expected return status code 201

4 - Able to create template in module setup using fixed data Master
    [Documentation]    Able to create template in module setup using fixed data Master
    ...    This is not applicable to distadm, hqadm
    [Tags]    sysimp    9.1
    Given user retrieves token access as ${user_role}
    When user creates module setup using random data
    Then expected return status code 201
    ${TemplateDetails}=    create dictionary
    ...    TYPE=TestMaster
    ...    DESCRIPTION=TestMaster
    ...    CONTENT=[{"display_type":"master","content":{"customComponent":"TestMaster"}}]
    set test variable    ${TemplateDetails}
    When user creates template in module setup using fixed data
    Then expected return status code 201

5 - Able to create template in module setup using fixed data Summary
    [Documentation]    Able to create template in module setup using fixed data Summary
    ...    This is not applicable to distadm, hqadm
    [Tags]    sysimp    9.1
    Given user retrieves token access as ${user_role}
    When user creates module setup using random data
    Then expected return status code 201
    ${TemplateDetails}=    create dictionary
    ...    TYPE=TestSummary
    ...    DESCRIPTION=TestSummary
    ...    CONTENT=[{"display_type":"summary","field_delimiter":"new_line","fields":[]}]
    set test variable    ${TemplateDetails}
    When user creates template in module setup using fixed data
    Then expected return status code 201
