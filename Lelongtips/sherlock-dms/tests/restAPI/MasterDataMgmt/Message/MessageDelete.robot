*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Message/MessagePost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Message/MessageDelete.py

Test Setup      user creates prerequisite for message
Test Teardown   user deletes prerequisite for message

*** Test Cases ***
1 - Able to delete newly created message setup by hq
    [Documentation]    This test is to delete message setup by hq
    [Tags]     hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Distributor with random data
    Then expected return status code 201
    When user deletes message with created data
    Then expected return status code 200
