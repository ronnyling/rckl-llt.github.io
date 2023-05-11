*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/UserManagement/User/UserSetupPost.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py
*** Test Cases ***

1 - Able to create user setup using random data
    [Documentation]    Able to create user setup using random data
    [Tags]   sysimp    hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates user setup using random data
    Then expected return status code 201

2 - Able to create user setup using given data
    [Documentation]    Able to create user setup by using given data
    [Tags]    sysimp    hqadm    9.0
    Given user retrieves token access as ${user_role}
    ${setup_details}=   create dictionary
    ...    NAME=API CRUSER
    ...    CONTACT_NO=01212345671026
    set test variable     &{setup_details}
    When user creates user setup using given data
    Then expected return status code 201

#3 - Unable to create new Telesales user when Telesales = Off
#    [Documentation]    To unable to create Telesales user when setup is off
#    [Tags]     distadm    9.0      test
#    [Setup]    User sets the feature setup for telesales to off passing with 'telesales' value
#    ${role_details}=   create dictionary
#    ...    ROLE=TELESALES
#    set test variable     &{role_details}
#    Given user retrieves token access as ${user_role}
#    When user creates user setup using given data
#    Then expected return status code 201

