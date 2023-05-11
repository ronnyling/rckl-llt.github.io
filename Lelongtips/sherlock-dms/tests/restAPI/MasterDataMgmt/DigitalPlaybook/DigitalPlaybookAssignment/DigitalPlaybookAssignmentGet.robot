*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookAssignment/DigitalPlayBookAssignmentPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookAssignment/DigitalPlaybookAssignmentGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookGeneralInfo/DigitalPlaybookPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookGeneralInfo/DigitalPlaybookDelete.py
Library          ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py

*** Test Cases ***

1 - Able to retrieve all digital playbook assignment and return 200 by using hq admin
    [Documentation]    Able to retrieve all digital playbook assignment and return 200
    [Tags]     hqadm    9.2
    [Setup]  User sets the feature setup for playbook to on passing with 'playbk' value
     ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=C
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    When user assigns playbook to Level:Sales Office, Node:Eggy Global Company, Dist:DistEgg
    And user create customer assignment for playbook to Customer:CT0000001549
    Then expected return status code 201
    When user retrieves all digital playbook assignment
    Then expected return status code 200
    When user deletes playbook with created data
    Then expected return status code 200

2 - Unable to retrieve digital playbook using dist when is not assigned to dist
    [Documentation]    Unable to retrieve all digital playbook assignment using dist when is not assigned to dist
    [Tags]     hqadm    9.2
    [Setup]  User sets the feature setup for playbook to on passing with 'playbk' value
     ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=C
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    Given user retrieves token access as distadm
    When user retrieves all digital playbook assignment
    Then expected return status code 204
    Given user retrieves token access as ${user_role}
    When user deletes playbook with created data
    Then expected return status code 200

3 - Unable to retrieve digital playbook assignment and return 204
    [Documentation]    Unable to retrieve digital playbook assignment and return 204
    [Tags]     hqadm    9.2
    [Setup]  User sets the feature setup for playbook to on passing with 'playbk' value
     ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=C
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    When user retrieves all digital playbook assignment
    Then expected return status code 204
    When user deletes playbook with created data
    Then expected return status code 200

4 - Able to retrieve created digital playbook assignment by id and return 200
    [Documentation]    Able to retrieve created digital playbook assignment and return 200
    [Tags]     hqadm    9.2
    [Setup]  User sets the feature setup for playbook to on passing with 'playbk' value
     ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=C
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    When user assigns playbook to Level:Sales Office, Node:Eggy Global Company, Dist:DistEgg
    And user create customer assignment for playbook to Customer:CT0000001549
    Then expected return status code 201
    When user retrieves created digital playbook assignment
    Then expected return status code 200
    When user deletes playbook with created data
    Then expected return status code 200

5 - Unable to retrieve digital playbook when feature setup is turned off and expect return 403
    [Documentation]    Unable to retrieve digital playbook when feature setup is turned off and expect return 403
    [Tags]     hqadm    9.2
    [Setup]  User sets the feature setup for playbook to on passing with 'playbk' value
     ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=C
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    When user assigns playbook to Level:Sales Office, Node:Eggy Global Company, Dist:DistEgg
    And user create customer assignment for playbook to Customer:CT0000001549
    Then expected return status code 201
    And User sets the feature setup for playbook to off passing with 'playbk' value
    Given user retrieves token access as ${user_role}
    When user retrieves all digital playbook assignment
    Then expected return status code 403
    And User sets the feature setup for playbook to on passing with 'playbk' value
    Given user retrieves token access as ${user_role}
    When user deletes playbook with created data
    Then expected return status code 200

6 - Able to retrieve assinged digital playbook assignment and return 200 by using dist admin
    [Documentation]    Able to retrieve assinged digital playbook assignment and return 200 by using dist admin
    [Tags]     hqadm    9.2
    [Setup]  User sets the feature setup for playbook to on passing with 'playbk' value
     ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=C
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    When user assigns playbook to Level:Sales Office, Node:Eggy Global Company, Dist:DistEgg
    And user create customer assignment for playbook to Customer:CT0000001549
    Then expected return status code 201
    Given user retrieves token access as distadm
    When user retrieves created digital playbook assignment
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user deletes playbook with created data
    Then expected return status code 200

7 - Unable to retrieve digital playbook which is not assinged to dist by dist adm and return 204
    [Documentation]    Unable to retrieve digital playbook which is not assinged to dist by dist adm
    [Tags]     hqadm    9.2
    [Setup]  User sets the feature setup for playbook to on passing with 'playbk' value
     ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=C
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    Given user retrieves token access as distadm
    When user retrieves all digital playbook assignment
    Then expected return status code 204
    Given user retrieves token access as ${user_role}
    When user deletes playbook with created data
    Then expected return status code 200

8 - Unable to retrieve invalid digital playbook by hq adm and return 204
    [Documentation]    Unable to retrieve digital playbook which is not assinged to dist by dist adm
    [Tags]     hqadm    9.2
    [Setup]  User sets the feature setup for playbook to on passing with 'playbk' value
     ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=C
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    When user retrieves all digital playbook assignment
    Then expected return status code 204
    When user deletes playbook with created data
    Then expected return status code 200