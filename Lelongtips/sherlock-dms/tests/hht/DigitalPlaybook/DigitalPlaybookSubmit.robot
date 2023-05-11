*** Settings ***
Resource        ${EXECDIR}/tests/hht/common.robot
Resource        ${EXECDIR}${/}tests/hht/common.robot
Library         ${EXECDIR}${/}resources/hht/DigitalPlaybook/DigitalPlaybookList.py
Library         ${EXECDIR}${/}resources/hht/DigitalPlaybook/DigitalPlaybookSubmit.py

*** Test Cases ***
1 - Able to submit playbook transaction
    [Documentation]    To test that user is able to submit playbook transaction
    [Tags]    salesperson     9.2
    Given user navigates to Hamburger Menu | My Playbook
    When user choose randomly from playbook listing
    And user choose randomly from content listing
    And validate playbook content displayed
    And user back to main menu
    Then user submits the device data
