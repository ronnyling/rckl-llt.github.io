*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Uom/UomAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Uom/UomListPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

*** Test Cases ***
1 - Able to delete Uom created
    [Tags]     sysimp    9.0
    Given user navigates to menu Configuration | Reference Data | UOM
    When user creates uom with random data
    Then uom created successfully with message 'Record created successfully'
    When user selects uom to delete
    Then uom deleted successfully with message 'Record deleted'

2 - Able to delete Uom using distributor when multi principal = On
    [Tags]     distadm    9.1    NRSZUANQ-27221
    Given user switches On multi principal
    And user navigates to menu Configuration | Reference Data | UOM
    When user creates uom with random data
    Then uom created successfully with message 'Record created successfully'
    When user selects uom to delete
    Then uom deleted successfully with message 'Record deleted'
