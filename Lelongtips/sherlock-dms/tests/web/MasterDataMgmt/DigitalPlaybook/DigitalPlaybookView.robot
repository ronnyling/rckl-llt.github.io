*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookView.py


*** Test Cases ***

1 - Able to View Digital Playbook
    [Documentation]    Able to view digital playbook
    [Tags]    distadm
    Given user navigates to menu Master Data Management | Digital Playbook
    When user selects digital playbook:PB0000002476 to view
    Then validates view mode