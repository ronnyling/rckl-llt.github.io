*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookGeneralInfo/DigitalPlaybookGet.py
Library          ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py

Test Setup    User sets the feature setup for playbook to on passing with 'playbk' value


*** Test Cases ***
1 - Able to retrieve all Playbook
    [Documentation]    Able to retrieve all playbook
    [Tags]    distadm    hqadm    9.2     NRSZUANQ-44795
    Given user retrieves token access as ${user_role}
    When user retrieves all playbook
    Then expected return status code 200

2 - Able to retrieve playbook using valid ID
    [Documentation]    Able to retrieve playbook using valid id
    [Tags]    distadm    hqadm    9.2     NNRSZUANQ-44795
    Given user retrieves token access as ${user_role}
    When user retrieves all playbook
    Then expected return status code 200
    When user retrieves playbook by valid id
    Then expected return status code 200

3 - Unable to retrieve playbook using invalid ID
    [Documentation]    Unable to retrieve playbook using invalid id
    [Tags]    distadm    hqadm    9.2     NNRSZUANQ-44795
    Given user retrieves token access as ${user_role}
    When user retrieves all playbook
    Then expected return status code 200
    When user retrieves playbook by invalid id
    Then expected return status code 404
