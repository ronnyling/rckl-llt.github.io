*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/PlaybookType/PlaybookTypeAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/PlaybookType/PlaybookTypeEditPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/PlaybookType/PlaybookTypeListPage.py

*** Test Cases ***
1 - Able to edit Playbook Type with random data
    [Tags]   hqadm    9.2    NRSZUANQ-43644
    Given user navigates to menu Configuration | Reference Data | Playbook Type
    When user creates playbook type with random data
    Then playbook type created successfully with message 'Record created successfully'
    When user selects playbook type to edit
    And user updates playbook type with random data
    Then playbook type updated successfully with message 'Record updated successfully'
    When user selects playbook type to delete
    Then playbook type deleted successfully with message 'Record deleted'

2 - Unable to edit Playbook Type code
    [Tags]   hqadm    9.2    NRSZUANQ-43678
    Given user navigates to menu Configuration | Reference Data | Playbook Type
    When user creates playbook type with random data
    Then playbook type created successfully with message 'Record created successfully'
    When user selects playbook type to edit
    Then verifies text field Playbook Type Code is disabled
    And user cancel creating playbook type
    When user selects playbook type to delete
    Then playbook type deleted successfully with message 'Record deleted'
