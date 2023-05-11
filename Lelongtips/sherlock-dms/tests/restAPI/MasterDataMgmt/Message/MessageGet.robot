*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Message/MessagePost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Message/MessageGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Message/MessageDelete.py

Test Setup      user creates prerequisite for message
Test Teardown   user deletes prerequisite for message

*** Test Cases ***
1 - Able to retrieve newly created message setup by hq
    [Documentation]    This test is to retrieve message setup by ID using hq
    [Tags]     hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Distributor with random data
    Then expected return status code 201
    When user gets message by using id
    Then expected return status code 200
    When user deletes message with created data
    Then expected return status code 200

2 - Able to retrieve all message setup by hq
    [Documentation]    This test is to retrieve all message setup using hq
    [Tags]     hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Distributor with random data
    Then expected return status code 201
    When user gets all message data
    Then expected return status code 200
    When user deletes message with created data
    Then expected return status code 200

3 - Able to GET ALL message and verify URL in respond and get status code 200
    [Documentation]    This test is to retrieve all message setup using hq and verify the URL in payload
    [Tags]     hqadm    9.1.1     NRSZUANQ-39362
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Distributor with random data
    Then expected return status code 201
    When user gets all message to validate url
    Then expected return status code 200
    When user deletes message with created data
    Then expected return status code 200

4 - Able to GET message by ID and verify URL in respond and get status code 200
    [Documentation]    This test is to retrieve message setup using hq and verify the URL in payload
    [Tags]     hqadm    9.1.1     NRSZUANQ-39364
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Distributor with random data
    Then expected return status code 201
    When user gets message by id to validate url
    Then expected return status code 200
    When user deletes message with created data
    Then expected return status code 200

5 - Able to GET ALL message and verify attachment in respond and get status code 200
    [Documentation]    This test is to retrieve all message setup using hq and verify the attachment in payload
    [Tags]     hqadm    9.1.1     NRSZUANQ-39422
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Distributor with random data
    Then expected return status code 201
    When user gets all message to validate attachment
    Then expected return status code 200
    When user deletes message with created data
    Then expected return status code 200

6 - Able to GET message by ID and verify attachment in respond and get status code 200
    [Documentation]    This test is to retrieve message setup using hq and verify the attachment in payload
    [Tags]     hqadm    9.1.1     NRSZUANQ-39423
    set test variable    ${file_type}     jpg
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Distributor with random data
    Then expected return status code 201
    When user gets message by id to validate attachment
    Then expected return status code 200
    When user deletes message with created data
    Then expected return status code 200
