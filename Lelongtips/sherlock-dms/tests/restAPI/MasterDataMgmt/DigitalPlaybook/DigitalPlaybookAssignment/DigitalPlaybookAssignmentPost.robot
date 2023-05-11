*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookAssignment/DigitalPlayBookAssignmentPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookAssignment/DigitalPlaybookAssignmentGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookGeneralInfo/DigitalPlaybookPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookGeneralInfo/DigitalPlaybookDelete.py
Library          ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py

*** Test Cases ***
1 - Able to create digital playbook assignment with customer and return 201
    [Documentation]    To assign digital playbook to specific customer
    [Tags]     hqadm    9.2
     ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=C
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    When user assigns playbook to Level:Sales Office, Node:Eggy Global Company, Dist:DistEgg
    And user create customer assignment for playbook to Customer:CT0000001549
    Then expected return status code 201
    When user deletes playbook with created data
    Then expected return status code 200


2 - Able to create digital playbook assignment with Customer Hierarchy and return 201
    [Documentation]     Able to create digital playbook assignment with Customer Hierarchy and return 201
    [Tags]     hqadm    9.2
    ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=C
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    When user assigns playbook to Level:Region, Node:North, Dist:DistEgg
    And user create customer assignment for playbook to Customer_Hierarchy_And_value:Channel,S6RightChannel
    Then expected return status code 201
    When user deletes playbook with created data
    Then expected return status code 200

3 - Able to create digital playbook assignment with dist and route assignment then return 201
    [Documentation]    To assign digital playbook to Sales office with Distributor and Route
    [Tags]     hqadm    9.2
    ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=R
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    When user assigns playbook to Level:Region, Node:North, Dist:DistEgg
    And user assign Route:RouteBB to digital playbook
    Then expected return status code 201
    When user deletes playbook with created data
    Then expected return status code 200

4 - Able to post route assignment with geo level but without dist and return 201
    [Documentation]   Able to post route assignment with geo level but without dist and return 201
    [Tags]     hqadm    9.2
    ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=R
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    When user assigns playbook to Level:Region, Node:North, Dist:Without
    And user assign Route:RouteBB to digital playbook
    Then expected return status code 201
    When user deletes playbook with created data
    Then expected return status code 200

5 - Able to create route assignment with sales office level and route then return 201
    [Documentation]    Able to create route assignment with sales office level and return 201
    [Tags]     hqadm    9.2
    ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=R
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    When user assigns playbook to Level:Sales Office, Node:Eggy Global Company, Dist:DistEgg
    And user assign Route:RouteBB to digital playbook
    Then expected return status code 201
    When user deletes playbook with created data
    Then expected return status code 200

6 - Unable to post digital playbook route assignment when digital playbook assign to = customer then return 400
    [Documentation]    To assign route when digital playbook assign to = customer and expect return 400
    [Tags]     hqadm    9.2
    ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=C
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    When user assigns playbook to Level:Region, Node:North, Dist:DistEgg
    And user assign Route:RouteBB to digital playbook
    Then expected return status code 400
    When user deletes playbook with created data
    Then expected return status code 200

7 - Able to create digital playbook assignment with customer and return 201
    [Documentation]    To assign digital playbook to specific customer
    [Tags]     hqadm    9.2
    ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=R
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    When user assigns playbook to Level:Region, Node:North, Dist:DistEgg
    And user create customer assignment for playbook to Customer:CT0000001549
    Then expected return status code 400
    When user deletes playbook with created data
    Then expected return status code 200

8 - Unable to create digital playbook with customer assignment with feature setup is turned off
    [Documentation]     Post digital playbook with customer assignment when feature setup is turned off and expect return 403
    [Tags]     hqadm    9.2
    [Teardown]  User sets the feature setup for playbook to on passing with 'playbk' value
    ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=C
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    When User sets the feature setup for playbook to off passing with 'playbk' value
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    And user assigns playbook to Level:Region, Node:North, Dist:DistEgg
    And user create customer assignment for playbook to Customer_Hierarchy_And_value:Channel,S6RightChannel
    Then expected return status code 403
    And user deletes playbook with created data
    Then expected return status code 200

9 - Unable to create digital playbook assignment when using dist token
    [Documentation]     expect return 403 when dist trying to post assignment
    [Tags]     hqadm    9.2
    [Teardown]  User sets the feature setup for playbook to on passing with 'playbk' value
    ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=C
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    Given user retrieves token access as distadm
    And User sets the feature setup for playbook to off passing with 'playbk' value
    When user assigns playbook to Level:Region, Node:North, Dist:DistEgg
    And user create customer assignment for playbook to Customer_Hierarchy_And_value:Channel,S6RightChannel
    Then expected return status code 403
    Given user retrieves token access as ${user_role}
    When user deletes playbook with created data
    Then expected return status code 200

10 - Able to delete assigned customer on digital playbook assignment using post method and return 201
    [Documentation]    To assign digital playbook to specific customer
    [Tags]     hqadm    9.2
     ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=C
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    When user assigns playbook to Level:Sales Office, Node:Eggy Global Company, Dist:DistEgg
    And user create customer assignment for playbook to Customer:CT0000001549
    Then expected return status code 201
    When user assigns playbook to Level:Sales Office, Node:Eggy Global Company, Dist:DistEgg
    And user create customer assignment for playbook to Customer:without
    Then expected return status code 201
    When user deletes playbook with created data
    Then expected return status code 200