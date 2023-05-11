*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/PlaybookType/PlaybookTypeAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/PlaybookType/PlaybookTypeListPage.py

*** Test Cases ***
1 - Able to search playbook type successfully from all columns
    [Documentation]    Able to search playbook type using search field
    [Tags]     hqadm    9.2    NRSZUANQ-43673
    Given user navigates to menu Configuration | Reference Data | Playbook Type
    When user creates playbook type with random data
    Then playbook type created successfully with message 'Record created successfully'
    When user searches playbook type using created data
    Then playbook type listed successfully in listing
    When user selects playbook type to delete
    Then playbook type deleted successfully with message 'Record deleted'
