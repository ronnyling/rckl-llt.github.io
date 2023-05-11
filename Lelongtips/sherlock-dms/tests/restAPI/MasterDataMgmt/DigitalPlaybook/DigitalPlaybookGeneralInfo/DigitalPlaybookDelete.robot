*** Settings ***
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookGeneralInfo/DigitalPlaybookPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookGeneralInfo/DigitalPlaybookDelete.py
Library         ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py

Test Setup    User sets the feature setup for playbook to on passing with 'playbk' value

*** Test Cases ***
1 - Able to DELETE Playbook and get 200
    [Documentation]  To delete Playbook using created data via api
    [Tags]    hqadm     9.2    NRSZUANQ-44760
    Given user retrieves token access as ${user_role}
    When user creates playbook with random data
    Then expected return status code 201
    When user deletes playbook with created data
    Then expected return status code 200

2 - Unable to DELETE Playbook using distributor access and get 403
    [Documentation]  To validate distributor unable to delete Playbook via api
    [Tags]    distadm     9.2    NRSZUANQ-44760
    Given user retrieves token access as hqadm
    When user creates playbook with random data
    Then expected return status code 201
    Given user retrieves token access as ${user_role}
    When user deletes playbook with created data
    Then expected return status code 403
    Given user retrieves token access as hqadm
    When user deletes playbook with created data
    Then expected return status code 200
