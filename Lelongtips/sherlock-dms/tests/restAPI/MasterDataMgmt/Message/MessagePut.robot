*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Message/MessagePost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Message/MessagePut.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Message/MessageDelete.py

Test Setup      user creates prerequisite for message
Test Teardown   user deletes prerequisite for message

*** Test Cases ***
1 - Able to update msg setup by hq using random data
    [Documentation]    This test is to update msg setup by hq using random data
    [Tags]     hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Distributor with random data
    Then expected return status code 201
    When user updates message as HQ and send to Route:Presales,Vansales with random data
    Then expected return status code 200
    When user deletes message with created data
    Then expected return status code 200

2 - Able to PUT message URL and get status code 200
    [Documentation]    This test is to update msg setup by passing in URL data
    [Tags]     hqadm    9.1.1    NRSZUANQ-39357
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Distributor with random data
    Then expected return status code 201
    ${link_details}=   create dictionary
    ...    ACTION=create
    ...    URL=https://accentureacme-qa-dms-approuter-qa.cfapps.jp10.hana.ondemand.com/
    ...    URL_DESC=Acme QA
    ${link_list}=   create list
    ...    ${link_details}
    ${msg_details}=   create dictionary
    ...   LINKS=${link_list}
    When user updates message as HQ and send to Distributor with given data
    Then expected return status code 200
    When user deletes message with created data
    Then expected return status code 200

3 - Able to PUT message URL by removing it and get status code 200
    [Documentation]    This test is to update msg setup by removing URL data
    [Tags]     hqadm    9.1.1    NRSZUANQ-39358
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
    set test variable     ${update_action}     delete
    When user updates message as HQ and send to Distributor with given data
    Then expected return status code 200
    When user deletes message with created data
    Then expected return status code 200

4 - Unable to PUT message with invalid URL and get status code 400
    [Documentation]    This test is to update msg setup by using invalid URL data
    [Tags]     hqadm    9.1.1    NRSZUANQ-39360
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Distributor with random data
    Then expected return status code 201
    ${link_details}=   create dictionary
    ...    ACTION=create
    ...    URL=htp.abc
    ...    URL_DESC=Acme QA
    ${link_list}=   create list
    ...    ${link_details}
    ${msg_details}=   create dictionary
    ...   LINKS=${link_list}
    When user updates message as HQ and send to Distributor with given data
    Then expected return status code 400
    When user deletes message with created data
    Then expected return status code 200

5 - Able to PUT message attachment and get status code 200
    [Documentation]    This test is to update msg setup by using valid attachment data
    [Tags]     hqadm    9.1.1    NRSZUANQ-39417
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Distributor with random data
    Then expected return status code 201
    set test variable    ${file_type}     jpg
    When user updates message as HQ and send to Distributor with given data
    Then expected return status code 200
    When user deletes message with created data
    Then expected return status code 200

6 - Able to PUT message attachment by removing it and get status code 200
    [Documentation]    This test is to update msg setup by using removing attachment data
    [Tags]     hqadm    9.1.1    NRSZUANQ-39418
    set test variable    ${file_type}     jpg
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Distributor with random data
    Then expected return status code 201
    set test variable     ${update_action}     delete
    When user updates message as HQ and send to Distributor with given data
    Then expected return status code 200
    When user deletes message with created data
    Then expected return status code 200

7 - Unable to PUT message with invalid attachment type and get status code 400
    [Documentation]    This test is to update msg setup by using invalid attachment type
    [Tags]     hqadm    9.1.1    NRSZUANQ-39420
    Given user retrieves token access as ${user_role}
    When user creates message as HQ and send to Distributor with random data
    Then expected return status code 201
    set test variable    ${file_type}     mp3
    When user updates message as HQ and send to Distributor with given data
    Then expected return status code 400
    When user deletes message with created data
    Then expected return status code 200