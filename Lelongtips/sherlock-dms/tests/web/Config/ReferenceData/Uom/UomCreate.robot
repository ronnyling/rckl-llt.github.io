*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Uom/UomAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Uom/UomListPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

*** Test Cases ***
1 - Able to Create Uom using fixed data
    [Documentation]    Able to create uom by using fixed data
    [Tags]      sysimp    9.0
    ${uom_details}=   create dictionary
    ...    uom_cd=BCT
    ...    uom_desc=Bucsket
    Given user navigates to menu Configuration | Reference Data | UOM
    When user creates uom with fixed data
    Then uom created successfully with message 'Record created successfully'
    When user selects uom to delete
    Then uom deleted successfully with message 'Record deleted'

2 - Able to Create Uom using random data
    [Documentation]    Able to create uom by using random generated data
    [Tags]     sysimp    9.0
    Given user navigates to menu Configuration | Reference Data | UOM
    When user creates uom with random data
    Then uom created successfully with message 'Record created successfully'
    When user selects uom to delete
    Then uom deleted successfully with message 'Record deleted'

3 - Able to Create Non prime Uom
    [Documentation]    Able to create non-prime uom using distributor login when multi principal = On
    [Tags]    distadm    9.1    NRSZUANQ-27179
    Given user switches On multi principal
    And user navigates to menu Configuration | Reference Data | UOM
    When user creates uom with random data
    Then uom created successfully with message 'Record created successfully'
    When user selects uom to delete
    Then uom deleted successfully with message 'Record deleted'

4 - Validate the Principal = Non Prime and Disable when create UOM using Distributor
    [Tags]    distadm    9.1    NRSZUANQ-27181
    Given user switches On multi principal
    And user navigates to menu Configuration | Reference Data | UOM
    When user creates new uom
    Then user validates principal field is disabled

5 - Distributor created UOM should not be visible from HQ User
    [Tags]    distadm    9.1    NRSZUANQ-27185
    [Setup]       run keywords
    ...    user open browser and logins using user role ${user_role}
    ...    AND  user switches On multi principal
    ...    AND  user navigates to menu Configuration | Reference Data | UOM
    ...    AND  user creates uom with random data
    ...    AND  uom created successfully with message 'Record created successfully'
    ...    AND  user logouts and closes browser
    [Teardown]    run keywords
    ...    user open browser and logins using user role ${user_role}
    ...    AND  user navigates to menu Configuration | Reference Data | UOM
    ...    AND  user selects uom to delete
    ...    AND  uom deleted successfully with message 'Record deleted'
    ...    AND  user logouts and closes browser
    Given user open browser and logins using user role hqadm
    When user navigates to menu Configuration | Reference Data | UOM
    And user filters uom using created data
    Then record not displaying in uom list
    And user logouts and closes browser

6 - Unable to Create Non prime Uom when multi principal = Off
    [Tags]    distadm    9.1    NRSZUANQ-27190
    Given user switches Off multi principal
    And user navigates to menu Configuration | Reference Data | UOM
    When verify add uom button not visible
    Then user switches On multi principal
