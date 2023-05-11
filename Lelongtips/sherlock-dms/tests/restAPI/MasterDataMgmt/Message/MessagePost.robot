*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Message/MessagePost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Message/MessageDelete.py

Test Setup      user creates prerequisite for message
Test Teardown   user deletes prerequisite for message

*** Test Cases ***
1 - Able to create new msg setup by hq using random data
    [Documentation]    This test is to create msg setup by hq using random data
    [Tags]     hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Distributor with random data
    Then expected return status code 201
    When user deletes message with created data
    Then expected return status code 200

2 - Able to create new msg setup by hq using fixed data
    [Documentation]    This test is to create msg setup by hq using fixed data
    [Tags]     hqadm    9.0
    ${msg_details}=   create dictionary
    ...   SUBJECT=Testing MessageSub
    ...   SEND_TO=D
    ...   START_DT=2025-08-01
    ...   END_DT=2025-09-01
    ...   CONTENT=Testing message body content
    ...   MSG_PRIORITY=alert
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Distributor with fixed data
    Then expected return status code 201
    When user deletes message with created data
    Then expected return status code 200

3 - Able to create new msg setup by Hq to spefic Route
    [Documentation]    This test is to create msg setup by hq to specific route which
    ...    contains of Presales,Vansales,Merchandiser,HQ Merchandiser,HQ Salesman
    [Tags]     hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Route:Presales,Vansales with random data
    Then expected return status code 201
    When user deletes message with created data
    Then expected return status code 200

4 - Able to create new msg setup by Dist to Route
    [Documentation]    This test is to create msg setup by dist to route
    [Tags]     distadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates message as Distributor and send to Route with random data
    Then expected return status code 201
    When user deletes message with created data
    Then expected return status code 200

5 - Not Able to create msg setup with Invalid Start Date
    [Documentation]    This test is to validate start date cannot be past date
    [Tags]     hqadm    9.0
    ${msg_details}=   create dictionary
    ...   START_DT=2017-08-01
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Distributor with fixed data
    Then expected return status code 400

6 - Not Able to create msg setup with Invalid Operator Type
    [Documentation]    This test is to test using invalid operator type
    [Tags]     hqadm    9.0
    ${msg_details}=   create dictionary
    ...   OP_TYPE=invalid
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Route:Presales with fixed data
    Then expected return status code 400

7 - Unable to create msg setup with Subject more than 100 characters
    [Documentation]    This test is to test unable to create msg setup with Subject more than 100 characters
    [Tags]     hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Distributor with InvalidSubject data
    Then expected return status code 400

8 - Unable to create msg setup with Content more than 500 characters
    [Documentation]    This test is to test unable to create msg setup with Content more than 500 characters
    [Tags]     hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Distributor with InvalidContent data
    Then expected return status code 400

9 - Unable to create msg setup with Subject with empty String
    [Documentation]    This test is to test unable to create msg setup with empty title
    [Tags]     hqadm    9.0
    ${msg_details}=   create dictionary
    ...   SUBJECT=${EMPTY}
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Distributor with fixed data
    Then expected return status code 400

10 - Able to POST message with single/multiple URL and get status code 201
    [Documentation]    This test is to create msg setup with URL
    [Tags]     hqadm     hquser     9.1.1    NRSZUANQ-39355   NRSZUANQ-39361
    ${link_details}=   create dictionary
    ...    ACTION=create
    ...    URL=https://accentureacme-qa-dms-approuter-qa.cfapps.jp10.hana.ondemand.com/
    ...    URL_DESC=Acme QA
    ${link_list}=   create list
    ...    ${link_details}
    ${msg_details}=   create dictionary
    ...   LINKS=${link_list}
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Distributor with given data
    Then expected return status code 201
    When user deletes message with created data
    Then expected return status code 200

11 - Able to POST message with single/multiple Attachment and get status code 201
    [Documentation]    This test is to create msg setup with attachment (jpg, png, ppt, pdf, mp4)
    [Tags]     hqadm     hquser     9.1.1    NRSZUANQ-39356
    set test variable    ${file_type}     jpg
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Distributor with random data
    Then expected return status code 201
    When user deletes message with created data
    Then expected return status code 200

12 - Unable to POST message with invalid URL and get status code 400
    [Documentation]    This test is to create msg setup with using invalid URL
    [Tags]     hqadm     hquser     9.1.1    NRSZUANQ-39359
    ${link_details}=   create dictionary
    ...    ACTION=create
    ...    URL=htp.abc
    ...    URL_DESC=Acme QA
    ${link_list}=   create list
    ...    ${link_details}
    ${msg_details}=   create dictionary
    ...   LINKS=${link_list}
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Distributor with fixed data
    Then expected return status code 400

13 - Unable to POST message with invalid attachment type and get status code 400
    [Documentation]    This test is to create msg setup with using invalid attachment type
    [Tags]     hqadm     hquser     9.1.1    NRSZUANQ-39419    NRSZUANQ-45081
    set test variable    ${file_type}     docx
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Distributor with random data
    Then expected return status code 400