*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supplier/SupplierListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supplier/SupplierAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supplier/SupplierGet.py
*** Test Cases ***
1-Able to add new supplier with random data
    [Documentation]    To ensure user able to add supplier
    [Tags]  distadm    9.0
    Given user navigates to menu Master Data Management | Supplier
    When user creates supplier with randomData
    Then supplier created successfully with message 'Record created successfully'
    When user validate created supplier is listed in the table and select to delete
    Then supplier deleted successfully with message 'Record deleted'

2-Able to set Principal Flag to Prime-Default and save successfully
    [Documentation]    To ensure user able to add supplier
    [Tags]   distadm    9.1    NRSZUANQ-27057    NRSZUANQ-27077    NRSZUANQ-27063
    [Setup]    run keywords
    ...    user switches On multi principal
    ...    AND    user open browser and logins using user role ${user_role}
    ${supplier_details}=    create dictionary
    ...    principal=Prime
    ...    default=true
    set test variable    ${supplier_details}
    Given user navigates to menu Master Data Management | Supplier
    And user validates is there any default supplier
    When user creates supplier with multi principal on
    Then supplier created successfully with message 'Record created successfully'
    When user validate created supplier is listed in the table and select to delete
    Then supplier deleted successfully with message 'Record deleted'

3-Validate Principal Flag not displaying when Multi Principal = No
    [Documentation]    To ensure user unable to view principal field in supplier when multi principal = no
    [Tags]   distadm    9.1    NRSZUANQ-27066
    [Setup]    run keywords
    ...    user switches Off multi principal
    ...    AND    user open browser and logins using user role ${user_role}
    Given user navigates to menu Master Data Management | Supplier
    When user validates principal field is not visible
    Then principal field not visible on screen

4-Default = No and Disabled when Principal Flag = Non-Prime
    [Documentation]    To ensure user validates default set to no and disable when principal = non prime
    [Tags]   distadm    9.1    NRSZUANQ-27068
    [Setup]    run keywords
    ...    user switches On multi principal
    ...    AND    user open browser and logins using user role ${user_role}
    ${supplier_details}=    create dictionary
    ...    principal=Non-Prime
    ...    default=False
    set test variable    ${supplier_details}
    Given user navigates to menu Master Data Management | Supplier
    When user creates supplier with multi principal on
    Then supplier created successfully with message 'Record created successfully'
    When user validate created supplier is listed in the table and select to delete
    Then supplier deleted successfully with message 'Record deleted'

5-Unable to set Principal Flag = Prime and Default when there is existing default Supplier
    [Documentation]    To ensure user unable to create more than 1 default supplier
    [Tags]   distadm    9.1    NRSZUANQ-27073
    [Setup]    run keywords
    ...    user switches On multi principal
    ...    AND    user open browser and logins using user role ${user_role}
    [Teardown]  run keywords
    ...    user clicks on Cancel button
    ...    AND    user validate created supplier is listed in the table and select to delete
    ...    AND    supplier deleted successfully with message 'Record deleted'
    ...    AND    user logouts and closes browser
    ${supplier_details}=    create dictionary
    ...    principal=Prime
    ...    default=True
    set test variable    ${supplier_details}
    Given user navigates to menu Master Data Management | Supplier
    And user validates is there any default supplier
    When user creates supplier with multi principal on
    Then supplier created successfully with message 'Record created successfully'
    When user creates supplier with duplicate multi principal on
    Then expect pop up message: Default Supplier already exist.

6-HQ User unable to View Supplier screen
    [Documentation]    To ensure user unable to view supplier menu
    [Tags]   hquser   hqadm    9.1    NRSZUANQ-27080
    When user validates the Supplier module is not visible
    Then menu Supplier not found



