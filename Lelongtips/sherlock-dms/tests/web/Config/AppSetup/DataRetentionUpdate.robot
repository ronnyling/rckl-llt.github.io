*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/AppSetup/DataRetentionEditPage.py
Library         ${EXECDIR}${/}resources/components/Tab.py


*** Test Cases ***
1 - Updates the field in Data Retention with random data
    [Documentation]    Updates the field in Data Retention
    [Tags]     hqadm    9.1
    Given user navigates to menu Configuration | Application Setup
    When user navigates to Data Retention tab
    Then user updates data retention using random data
    And Data Retention updated successfully with message 'Record updated successfully'

2 - Updates the field in Data Retention with fixed data
    [Documentation]    Updates the field in Data Retention
    [Tags]     hqadm    9.1
    ${DataRetentionDetails}=    create dictionary
     ...    Order Status (Days)=${7}
     ...    Sales History (Months)=${1}
     ...    Stock Take History (Days)=${90}
     ...    Past Route Plan (Days)=${7}
     ...    Future Route Plan (Days)=${7}
     ...    Missed Call (Days)=${5}
     ...    Missed Call Reminder (Days)=${5}
     ...    Average Visit Sales=${5}
     ...    No Distribution (Days)=${7}
     ...    Purge Batch Code (Days)=${180}
     ...    MSL Compliance (Days)=${60}
     ...    Load Invoice From Past Days=${3}
     ...    Ref. Doc. Period (DMS)=${90}
     ...    Ref. Doc. Period (SFA)=${90}
    set test variable    &{DataRetentionDetails}
    Given user navigates to menu Configuration | Application Setup
    When user navigates to Data Retention tab
    Then user updates data retention using fixed data
    And Data Retention updated successfully with message 'Record updated successfully'