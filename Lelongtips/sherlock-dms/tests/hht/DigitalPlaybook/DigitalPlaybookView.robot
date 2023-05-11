*** Settings ***
Resource        ${EXECDIR}/tests/hht/common.robot
Resource        ${EXECDIR}${/}tests/hht/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/hht/DigitalPlaybook/DigitalPlaybookList.py
Library         ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookGeneralInfo/DigitalPlaybookPost.py

*** Test Cases ***
1 - Able to view playbook content
    [Documentation]    To test that user is able to view playbook content
    [Tags]    salesperson     9.2    NRSZUANQ-44025
    Given user navigates to Hamburger Menu | My Playbook
    When user choose randomly from playbook listing
    And user choose randomly from content listing
    Then validate playbook content displayed

2 - Able to zoom playbook image content
    [Documentation]    To test that user is able to zoom image type playbook content
    [Tags]    salesperson     9.2    NRSZUANQ-45187
    Given user navigates to Hamburger Menu | My Playbook
    When user choose 7 from playbook listing
    And user choose 1 from content listing
    And user zoom and move the image
    Then validate playbook content displayed

3 - Able to update and view completion status
    [Documentation]    To test that user is able to update and view the playbook completion status (green tick mark)
    [Tags]    salesperson     9.2    NRSZUANQ-44776    NRSZUANQ-44656
    Given user navigates to Hamburger Menu | My Playbook
    When user choose randomly from playbook listing
    And user choose randomly from content listing
    And user back to content page
    And user back to playbook page
    Then validate completed status

4 - Able to view content file type
    [Documentation]    To test that user is able to update and view the playbook completion status (green tick mark)
    [Tags]    salesperson     9.2    NRSZUANQ-47518
    Given pull emulator db into local
    Given user navigates to Hamburger Menu | My Playbook
    And user choose randomly from playbook listing
    And validate playbook content listing
    Then user validates content file type

5 - Able to view playbook module when feature setup is enabled
    [Documentation]    To test that user is able to view playbook module when feature setup is enabled
    [Tags]    salesperson     9.2    NRSZUANQ-44776
    Given User sets the feature setup for playbook to on passing with 'playbk' value
    When user syncs the device data
    And user navigates to Hamburger Menu
    Then user validates My Playbook is on

6 - Unable to view playbook module when feature setup is disabled
    [Documentation]    To test that user is unable to view playbook module when feature setup is disabled
    [Tags]    salesperson     9.2    NRSZUANQ-44776
    [Teardown]    run keywords
    ...    User sets the feature setup for playbook to on passing with 'playbk' value
    ...    And user syncs the device data
    Given User sets the feature setup for playbook to off passing with 'playbk' value
    When user syncs the device data
    And user navigates to Hamburger Menu
    Then user validates My Playbook is off

7 - Able to show last updated date for playbook
    [Documentation]    To test that user is able to view playbook last updated date
    [Tags]    salesperson     9.2    NRSZUANQ-44656
    Given user navigates to Hamburger Menu | My Playbook
    Then validate playbook listing
    And validate last updated date

8 - Able to show last played date for playbook
    [Documentation]    To test that user is able to view playbook last played date
    [Tags]    salesperson     9.2    NRSZUANQ-44656
    Given user navigates to Hamburger Menu | My Playbook
    When user choose 1 from playbook listing
    And user choose 0 from content listing
    And user back to content page
    And user back to playbook page
    Then validate last played date

9 - Able to generate visit ID during time in
    [Documentation]    To test that user is able to generate visit ID during time in
    [Tags]    salesperson     9.2    NRSZUANQ-44656    TODO
    [Setup]  run keywords
    ...    user retrieves token access as hqadm
    ...    user creates playbook with random data
    Given user syncs the device data
    Given user navigates to Hamburger Menu | My Playbook
    When user choose randomly from playbook listing
    And user choose randomly from content listing
    And user back to content page
    And user back to playbook page
    Then validate visit id