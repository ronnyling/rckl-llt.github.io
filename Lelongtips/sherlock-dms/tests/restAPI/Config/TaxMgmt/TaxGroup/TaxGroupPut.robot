*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxGroup/TaxGroupPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxGroup/TaxGroupDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxGroup/TaxGroupPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigGet.py

*** Test Cases ***
1 - Able to edit created tax group using random data
    [Documentation]    Able to edit tax group when login as dist adm
    [Tags]     distadm    9.1
    Given user retrieves token access as ${user_role}
    When user creates tax group using random data
    Then expected return status code 201
    ${tax_group_details}=    create dictionary
    ...    TAX_GRP_DESC=Edited tax group text
    set test variable  &{tax_group_details}
    When user edits tax group by given data
    Then expected return status code 200
    When user deletes created tax group
    Then expected return status code 200

2 - Dist unable to edit hq created tax group using random data
    [Documentation]    Dist unable to edit tax group that created by hqadm
    [Tags]     hqadm    9.1
    Given user retrieves token access as hqadm
    When user creates tax group using random data
    Then expected return status code 201
    ${tax_group_details}=    create dictionary
    ...    TAX_GRP_DESC=Edited tax group text
    set test variable  &{tax_group_details}
    Given user retrieves token access as distadm
    When user edits tax group by given data
    Then expected return status code 403
    Given user retrieves token access as hqadm
    When user deletes created tax group
    Then expected return status code 200

3 - Unable to update tax group while dist config is turned off
    [Documentation]   Unable to update tax group while dist config is turned off and api return 403
    [Tags]     distadm    9.1
    [Setup]  run keywords
    ...   user switches On multi principal
    [Teardown]  run keywords
    ...   user switches on multi principal
    Given user retrieves token access as ${user_role}
    When user creates tax group using random data
    Then expected return status code 201
    And user switches off multi principal
    Given user retrieves token access as distadm
     ${tax_group_details}=    create dictionary
    ...    TAX_GRP_DESC=Edited tax group text
    set test variable  &{tax_group_details}
    When user edits tax group by given data
    Then expected return status code 403
    Given user retrieves token access as hqadm
    And user switches On multi principal
    And user retrieves token access as distadm
    When user deletes created tax group
    Then expected return status code 200