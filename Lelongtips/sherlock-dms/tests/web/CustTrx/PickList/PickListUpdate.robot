*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/PickList/PickListListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/PickList/PickListAddPage.py


*** Test Cases ***
1 - Able to create pick list
    [Documentation]  To validate user able to create picklist
    [Tags]    distadm
    ${picklist_details}=    create dictionary
    ...    WAREHOUSE=whtt
    ...    DATE_FROM=2012/12/01
    ...    DATE_TO=2012/12/30
    ...    ACTUAL_DATE=2012/12/30
    ...    DELIVERY=REgg6
    set test variable    ${picklist_details}
    Given user navigates to Customer Transaction | Pick List
    And user navigates to Pick List tab
    And user creates pick list using random data
    Then pick list created successfully with message 'Record created successfully'
    When user selects created pick list
    And user updates pick list using random data
    Then pick list created successfully with message 'Record updated successfully'
