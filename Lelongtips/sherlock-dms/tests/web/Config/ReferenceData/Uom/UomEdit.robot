*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Uom/UomAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Uom/UomListPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Uom/UomEditPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

*** Test Cases ***
1 - Able to edit Uom using fixed data
    [Tags]      sysimp    9.0
    ${uom_details}=   create dictionary
    ...    uom_desc=Bucket
    Given user navigates to menu Configuration | Reference Data | UOM
    When user creates uom with random data
    Then uom created successfully with message 'Record created successfully'
    When user selects uom to edit
    And user edits uom with fixed data
    Then uom edited successfully with message 'Record updated successfully'
    When user selects uom to delete
    Then uom deleted successfully with message 'Record deleted'

2 - Able to edit Uom data with random data
    [Tags]   sysimp     9.0
    Given user navigates to menu Configuration | Reference Data | UOM
    When user creates uom with random data
    Then uom created successfully with message 'Record created successfully'
    When user selects uom to edit
    And user edits uom with random data
    Then uom edited successfully with message 'Record updated successfully'
    When user selects uom to delete
    Then uom deleted successfully with message 'Record deleted'

3 - Distributor unable to edit the Principal radio buttons in UOM
    [Tags]   distadm     9.1    NRSZUANQ-27188
    Given user switches On multi principal
    And user navigates to menu Configuration | Reference Data | UOM
    When user creates uom with random data
    Then uom created successfully with message 'Record created successfully'
    When user selects uom to edit
    And user edits uom with random data
    Then uom edited successfully with message 'Record updated successfully'
    When user selects uom to delete
    Then uom deleted successfully with message 'Record deleted'
