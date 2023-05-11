*** Settings ***
Resource        ${EXECDIR}/tests/hht/common.robot
Resource        ${EXECDIR}${/}tests/hht/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/hht/DigitalPlaybook/DigitalPlaybookList.py
Library         ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookGeneralInfo/DigitalPlaybookPost.py

*** Test Cases ***
1 - Able to list playbook
    [Documentation]    To test that user is able to view playbook listing
    [Tags]    salesperson     9.2    NRSZUANQ-44022
    Given user navigates to Hamburger Menu | My Playbook
    Then validate playbook listing

2 - Able to list playbook content
    [Documentation]    To test that user is able to view playbook content listing
    [Tags]    salesperson     9.2    NRSZUANQ-44023
    Given user navigates to Hamburger Menu | My Playbook
    When user choose randomly from playbook listing
    Then validate playbook content listing

3 - Able to view playbook content file length
    [Documentation]    To test that user is able to view playbook content file length for video and pdf
    [Tags]    salesperson     9.2    NRSZUANQ-44023
    Given user navigates to Hamburger Menu | My Playbook
    When user choose 6 from playbook listing
    Then validate playbook content listing
    And validate playbook content file length