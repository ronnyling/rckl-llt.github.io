*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/PlaybookType/PlaybookTypeAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/PlaybookType/PlaybookTypeListPage.py

*** Test Cases ***
1 - Able to create Playbook Type with all fields with random data
    [Tags]   hqadm    9.2    NRSZUANQ-43643
    Given user navigates to menu Configuration | Reference Data | Playbook Type
    When user creates playbook type with random data
    Then playbook type created successfully with message 'Record created successfully'
    When user selects playbook type to delete
    Then playbook type deleted successfully with message 'Record deleted'

2 - Able to create Playbook Type with all fields with fixed data
    [Tags]   hqadm    9.2
    ${playbook_details}    create dictionary
    ...    PLAYBOOK_TYPE_DESC=Playbook Auto 001
    ...    PLAYBOOK_PRD_HIER_REQ=Yes                #either No or Yes
    Given user navigates to menu Configuration | Reference Data | Playbook Type
    When user creates playbook type with fixed data
    Then playbook type created successfully with message 'Record created successfully'
    When user selects playbook type to delete
    Then playbook type deleted successfully with message 'Record deleted'

3 - Able to cancel creating Playbook Type and back to listing successfully
    [Tags]   hqadm    9.2    NRSZUANQ-43645
    Given user navigates to menu Configuration | Reference Data | Playbook Type
    When user cancel creating playbook type
    Then user landed on page PlaybookTypeListPage

4 - Unable to create Playbook Type with empty data
    [Tags]   hqadm    9.2    NRSZUANQ-43676    NRSZUANQ-43675
    ${playbook_details}    create dictionary
    ...    PLAYBOOK_TYPE_CD=${EMPTY}
    ...    PLAYBOOK_TYPE_DESC=${EMPTY}
    ...    PLAYBOOK_PRD_HIER_REQ=Yes
    Given user navigates to menu Configuration | Reference Data | Playbook Type
    When user creates playbook type with fixed data
    Then unable to create successfully with validation message on fields

5 - Unable to create Playbook Type with existing code
    [Tags]   hqadm    9.2    NRSZUANQ-43677
    Given user navigates to menu Configuration | Reference Data | Playbook Type
    When user creates playbook type with random data
    Then playbook type created successfully with message 'Record created successfully'
    When user creates playbook type with existing data
    Then validate pop up message shows 'already exists'
    And confirm pop up message
    When user cancel creating playbook type
    And user selects playbook type to delete
    Then playbook type deleted successfully with message 'Record deleted'

6 - Distributor should only able to View Playbook Type
    [Tags]   distadm    9.2    NRSZUANQ-43679
    Given user navigates to menu Configuration | Reference Data | Playbook Type
    When validates button Add is hidden from screen
    And user selects playbook type to edit
    Then validates button Save is hidden from screen
