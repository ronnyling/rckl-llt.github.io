*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Uom/UomAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Uom/UomListPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

*** Test Cases ***
1 - Able to filter UOM using principal field
    [Documentation]    Able to filter Uom using principal field
    [Tags]     distadm    9.1    NRSZUANQ-27187
    Given user switches On multi principal
    And user navigates to menu Configuration | Reference Data | UOM
    When user creates uom with random data
    Then uom created successfully with message 'Record created successfully'
    When user filters uom using Non-Prime data
    Then principal listed successfully in uom
    When user selects uom to delete
    Then uom deleted successfully with message 'Record deleted'
