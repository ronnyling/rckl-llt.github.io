*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/ServiceMaster/ServiceMasterAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/TaxMgmt/ServiceMaster/ServiceMasterListPage.py

*** Test Cases ***
1 - Able to create service master using random data
    [Documentation]    Able to create service master using random data
    [Tags]     hqadm    9.2
    [Teardown]    run keywords
    ...    user selects service master to delete
    ...    AND     service master deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Tax Management | Service Master
    When user creates service master with random data
    Then service master created successfully with message 'Success: Record Added'

2 - Able to create service master using fixed data
    [Documentation]    Able to create service master using fixed data
    [Tags]     hqadm    9.2
    [Teardown]    run keywords
    ...    user selects service master to delete
    ...    AND     service master deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    ${svc_details}=    create dictionary
    ...    svc_code=SVCMS01
    ...    svc_desc=SVC MST 01
    ...    svc_tax_code=SVCCD01
    set test variable     &{svc_details}
    Given user navigates to menu Configuration | Tax Management | Service Master
    When user creates service master with fixed data
    Then service master created successfully with message 'Success: Record Added'

3 - Validate distributor only able to create non prime service master
    [Documentation]    Unable to create when mandatory fields are left blank
    [Tags]     distadm    9.2
    Given user navigates to menu Configuration | Tax Management | Service Master
    When user clicks on Add button
    Then validate principal field for service master