*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/AuditActivity/AuditActivityAddPage.py
Library         ${EXECDIR}${/}resources/web/Merchandising/MerchandisingSetup/AuditActivity/AuditActivityListPage.py

*** Test Cases ***
1- User able to create audit activity with random data
    [Documentation]  To  create audit activity with random data
    [Tags]  9.1   hqadm
    Given user navigates to menu Merchandising | Activity Setup | Audit
    When user creates audit activity using random data
    Then facing setup created successfully with message 'Record created successfully'
    When user back to listing page
    And user selects audit activity to delete
    Then audit activity deleted successfully with message 'Record Deleted Successfully'

2- User able to create audit activity with fix data
    [Documentation]  To  create audit activity with fix data
    [Tags]  9.1   hqadm
    ${AuditDetails} =   create dictionary
    ...   StoreSpace=SpaceF
    ...   Category=NikeCat1
    set test variable  &{AuditDetails}
    Given user navigates to menu Merchandising | Activity Setup | Audit
    When user creates audit activity using random data
    Then facing setup created successfully with message 'Record created successfully'
    When user back to listing page
    And user selects audit activity to delete
    Then audit activity deleted successfully with message 'Record Deleted Successfully'

3- User able to add facing audit activity
    [Documentation]  To  delete created audit activity
    [Tags]  9.1   hqadm
    Given user navigates to menu Merchandising | Activity Setup | Audit
    When user creates audit activity using random data
    Then facing setup created successfully with message 'Record created successfully'
    When user add facing audit activity
    Then facing audit added successfully with message 'Record created successfully'
    When user back to listing page
    And user selects audit activity to delete
    Then audit activity deleted successfully with message 'Record Deleted Successfully'

4- User able to add price audit activity
    [Documentation]  To  add price audit activity
    [Tags]  9.1   hqadm
     ${AuditDetails} =   create dictionary
    ...   StoreSpace=SpaceF
    ...   Category=NikeCat1
    set test variable  &{AuditDetails}
    Given user navigates to menu Merchandising | Activity Setup | Audit
    When user creates audit activity using random data
    Then facing setup created successfully with message 'Record created successfully'
    And user add price audit activity
    Then price audit activity created successfully with message 'Recored created successfully'
    When user back to listing page
    And user selects audit activity to delete
    Then audit activity deleted successfully with message 'Record Deleted Successfully'

5- User able to add promo compliance audit activity
    [Documentation]  To  add promo compliance audit activity
    [Tags]  9.1   hqadm
     ${AuditDetails} =   create dictionary
    ...   StoreSpace=SpaceF
    ...   Category=NikeCat1
    set test variable  &{AuditDetails}
    Given user navigates to menu Merchandising | Activity Setup | Audit
    When user creates audit activity using random data
    Then facing setup created successfully with message 'Record created successfully'
    And user selects audit activity to edit
    And user_add promo compliance activity
    Then promo compliance activity created successfully with message 'Records saved successfully'
    When user back to listing page
    And user selects audit activity to delete
    Then audit activity deleted successfully with message 'Record Deleted Successfully'

6- User able to add dist check audit activity
    [Documentation]  To  add dist check audit activity
    [Tags]  9.1   hqadm
     ${AuditDetails} =   create dictionary
    ...   StoreSpace=SpaceF
    ...   Category=NikeCat1
    set test variable  &{AuditDetails}
    Given user navigates to menu Merchandising | Activity Setup | Audit
    When user creates audit activity using random data
    Then facing setup created successfully with message 'Record created successfully'
    And user selects audit activity to edit
    And user add distribution check activity
    Then distribution check activity created successfully with message 'Record created successfully'
    When user back to listing page
    And user selects audit activity to delete
    Then audit activity deleted successfully with message 'Record Deleted Successfully'

7- User able to add planogram audit activity
    [Documentation]  To  add planogram audit activity
    [Tags]  9.1   hqadm
     ${AuditDetails} =   create dictionary
    ...   StoreSpace=SpaceF
    ...   Category=NikeCat1
    set test variable  &{AuditDetails}
    Given user navigates to menu Merchandising | Activity Setup | Audit
    When user creates audit activity using random data
    Then facing setup created successfully with message 'Record created successfully'
    And user selects audit activity to edit
    And user add planogram activity
    Then add planogram activity created successfully with message 'Record created successfully'
    When user back to listing page
    And user selects audit activity to delete
    Then audit activity deleted successfully with message 'Record Deleted Successfully'