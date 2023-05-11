*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/ServiceMaster/ServiceMasterAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/ServiceMaster/ServiceMasterListPage.py
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/ServiceMaster/ServiceMasterEditPage.py
*** Test Cases ***

1-Able to view service master details
    [Documentation]    To test that user able to view created service master
    [Tags]   hqadm    9.2
    [Teardown]    run keywords
    ...    user selects service master to delete
    ...    AND     service master deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Tax Management | Service Master
    When user creates service master with random data
    Then service master created successfully with message 'Success: Record Added'
    When user selects service master to edit
    Then service master viewed successfully

2-Able to update service master with fixed data
    [Documentation]    To test updating created service master with fixed data
    [Tags]   hqadm    9.2
    [Teardown]    run keywords
    ...    user selects service master to delete
    ...    AND     service master deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    ${new_svc_details}=    create dictionary
    ...    svc_desc=Service Master Automation
    set test variable     &{new_svc_details}
    Given user navigates to menu Configuration | Tax Management | Service Master
    When user creates service master with random data
    Then service master created successfully with message 'Success: Record Added'
    When user selects service master to edit
    And user edits service master with fixed data
    Then service master created successfully with message 'Success: Record Updated'

3-Able to update service master with random data
    [Documentation]    To test updating created service master with random data
    [Tags]   hqadm    9.2
    [Teardown]    run keywords
    ...    user selects service master to delete
    ...    AND     service master deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Tax Management | Service Master
    When user creates service master with random data
    Then service master created successfully with message 'Success: Record Added'
    When user selects service master to edit
    And user edits service master with random data
    Then service master created successfully with message 'Success: Record Updated'
