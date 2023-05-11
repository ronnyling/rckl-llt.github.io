*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/AuditActivity/AuditActivityAddPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/AuditActivity/AuditActivityListPage.py

*** Test Cases ***
1- User able to delete created audit activity
    [Documentation]  To  delete created audit activity
    [Tags]  9.1   hqadm
    ${AuditDetails} =   create dictionary
    ...   StoreSpace=SpaceF
    ...   Category=wd
    set test variable  &{AuditDetails}
    Given user navigates to menu Merchandising | Activity Setup | Audit
    When user creates audit activity using random data
    Then facing setup created successfully with message 'Record created successfully'
    When user back to listing page
    And user selects audit activity to delete
    Then audit activity deleted successfully with message 'Record Deleted Successfully'