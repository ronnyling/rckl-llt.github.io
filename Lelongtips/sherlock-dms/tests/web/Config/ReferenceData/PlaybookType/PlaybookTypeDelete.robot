*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/PlaybookType/PlaybookTypeAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/PlaybookType/PlaybookTypeListPage.py

*** Test Cases ***
1 - Able to delete Playbook Type which haven been used
    [Tags]   hqadm    9.2    NRSZUANQ-43672
    Given user navigates to menu Configuration | Reference Data | Playbook Type
    When user creates playbook type with random data
    Then playbook type created successfully with message 'Record created successfully'
    When user selects playbook type to delete
    Then playbook type deleted successfully with message 'Record deleted'
