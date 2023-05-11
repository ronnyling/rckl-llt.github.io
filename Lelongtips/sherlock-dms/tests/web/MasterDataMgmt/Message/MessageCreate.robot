*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Message/MessageListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Message/MessageAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Message/MessageAssignmentPage.py

*** Test Cases ***
1 - Able to Create Message with given data for one attachment
    [Documentation]    Able to create message with fixed data
    [Tags]     distadm    9.1.1
    ${message_details}=    create dictionary
    ...    messageTo=Route & Distributor
    set test variable     &{message_details}
    Given user navigates to menu Master Data Management | Message
    When user creates Message with attachment
    When user selects message and open attachment
    Then user selects message to download
    And user selects message and delete

2 - Able to Create Message with random data
    [Documentation]    Able to create message with random data
    [Tags]     distadm    9.1.1
    Given user navigates to menu Master Data Management | Message
    When user creates message with attachment
    When user selects message and open attachment
    Then user selects message to download
    And user selects message and delete

3 - Able to Create Message with given data for multiple attachment
    [Documentation]    Able to create message with fixed data
    [Tags]     distadm    9.1.1
    set test variable     ${count}     5
    Given user navigates to menu Master Data Management | Message
    When user creates Message with attachment
    Then user assigns distributor in the assignment
    When user selects message and open attachment
    Then user selects message to download
    And user selects message and delete


#------------------------------ Add Links -----------------------------#
4 - Able to add single Display Text and URL to message
    [Documentation]    Able to create message with URL using random data
    [Tags]     hqadm    9.1.1    NRSZUANQ-39286     NRSZUANQ-39348
    Given user navigates to menu Master Data Management | Message
    When user creates message with url
    Then message created successfully with message 'Record added'
    When user selects message and delete
    Then message deleted successfully with message 'Record deleted'

5 - Able to add multiple Display Text and URL to message
    [Documentation]    Able to create message with multiple URL using random data
    [Tags]     hqadm    9.1.1    NRSZUANQ-39323     NRSZUANQ-39339
    set test variable    ${no_url}    5
    Given user navigates to menu Master Data Management | Message
    When user creates message with url
    Then message created successfully with message 'Record added'
    When user selects message and delete
    Then message deleted successfully with message 'Record deleted'

6 - Able to cancel adding Link and closing add screen
    [Documentation]    Able to create message by cancelling the Link add screen
    [Tags]     hqadm    9.1.1    NRSZUANQ-39326
    Given user navigates to menu Master Data Management | Message
    When user cancels link add screen
    Then link add screen closed successfully

7 - Able to delete Link by clicking delete icon
    [Documentation]    Able to delete message Link using delete icon in pop up
    [Tags]     hqadm    9.1.1    NRSZUANQ-39344   NRSZUANQ-39350
    set test variable    ${no_url}    3
    Given user navigates to menu Master Data Management | Message
    When user creates message with url
    Then message created successfully with message 'Record added'
    When user deletes added link
    Then display url in popup delete successfully
    When user selects message and delete
    Then message deleted successfully with message 'Record deleted'

8 - Validate error prompt when save more than 5 URL and only can save with limited 5 URL
    [Documentation]    Validate error message prompt when more than 5 URL added and only limited to add 5 URL
    [Tags]     hqadm    9.1.1    NRSZUANQ-39416    NRSZUANQ-39347
    set test variable    ${no_url}    6
    Given user navigates to menu Master Data Management | Message
    When user creates message using over limit url
    And user deletes added link
    Then display url in popup delete successfully
    When user selects message and delete
    Then message deleted successfully with message 'Record deleted'

9 - Unable to save link with invalid URL
    [Documentation]    Validate error message prompt when url is invalid
    [Tags]     hqadm    9.1.1    NRSZUANQ-39346
    ${message_details}=    create dictionary
    ...    messageTo=Route & Distributor
    ...    URL=456m.dh.ghjk
    Given user navigates to menu Master Data Management | Message
    When user creates message using invalid url
    Then validate pop up message shows 'Unable to save link with invalid URL'
    And confirm pop up message

10 - Unable to save link with empty data
    [Documentation]    Validate error message prompt when url or display text is empty
    [Tags]     hqadm    9.1.1    NRSZUANQ-39345
    ${message_details}=    create dictionary
    ...    URL=${EMPTY}
    Given user navigates to menu Master Data Management | Message
    When user creates message using empty url
    Then validate pop up message shows 'Unable to save link with empty data.'
    And confirm pop up message

11 - Validate column showing '-' when no link added
    [Documentation]    Validate message listing showing '-' when no url added
    [Tags]     hqadm    9.1.1    NRSZUANQ-39349
    ${message_details}=    create dictionary
    ...    messageTo=Route & Distributor
    ...    URL=${EMPTY}
    Given user navigates to menu Master Data Management | Message
    When user creates message with url
    Then message created successfully with message 'Record added'
    And navigate to message sent tab
    And user validates listing showing '-' for Links
    When user selects message and delete
    Then message deleted successfully with message 'Record deleted'
