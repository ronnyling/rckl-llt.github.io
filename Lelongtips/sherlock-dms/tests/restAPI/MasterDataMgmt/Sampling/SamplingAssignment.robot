*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Sampling/SamplingPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Sampling/SamplingDelete.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Sampling/SamplingAssignment.py
Library          ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py

Test Setup    User sets the feature setup for sampling to on passing with 'sampling' value

*** Test Cases ***
1 - Able to POST Sampling assignment with Customer and return 201
    [Documentation]    Able to create sampling assignment with customer and return 201 via API
    [Tags]    hqadm    distadm    9.3
    Given user retrieves token access as ${user_role}
    When ${user_role} creates sampling with random data
    Then expected return status code 201
    When user assigns sampling to Level:Sales Office, Node:Eggy Global Company, Dist:DistEgg
    And user create customer assignment for sampling to Customer:CT0000001549
    Then expected return status code 201
    When user deletes sampling
    Then expected return status code 200

2 - Able to POST Sampling assignment with Customer Hierarchy and return 201
    [Documentation]     Able to create sampling assignment with Customer Hierarchy and return 201 via API
    [Tags]     hqadm    distadm    9.3
    Given user retrieves token access as ${user_role}
    When ${user_role} creates sampling with random data
    Then expected return status code 201
    When user assigns sampling to Level:Region, Node:North, Dist:DistEgg
    And user create customer assignment for sampling to Customer_Hierarchy_And_value:Channel,S6RightChannel
    Then expected return status code 201
    When user deletes sampling
    Then expected return status code 200

3 - Able to GET Sampling assignment and return 200
    [Documentation]    Able to retrieve sampling assignment and return 200 via API
    [Tags]    hqadm    distadm    9.3
    Given user retrieves token access as ${user_role}
    When ${user_role} creates sampling with random data
    Then expected return status code 201
    When user assigns sampling to Level:Sales Office, Node:Eggy Global Company, Dist:DistEgg
    And user create customer assignment for sampling to Customer:CT0000001549
    Then expected return status code 201
    When user retrieves sampling assignment
    Then expected return status code 200
    When user deletes sampling
    Then expected return status code 200

4 - Unable to GET Sampling assignment which is empty and return 204
    [Documentation]    Unable to retrieve sampling assignment which is empty and return 204 via API
    [Tags]    hqadm    distadm    9.3
    Given user retrieves token access as ${user_role}
    When ${user_role} creates sampling with random data
    Then expected return status code 201
    When user retrieves sampling assignment
    Then expected return status code 204
    When user deletes sampling
    Then expected return status code 200