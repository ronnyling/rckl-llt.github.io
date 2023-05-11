*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/WhatsApp/MyContactsListPage.py
Library         Collections

#TODO - Fix navigation to WhatsApp module (Now it is located at button at page header)

*** Test Cases ***
1 - Distributor admin goes to WhatsApp contact list page and verify the validations are in place
    [Documentation]    Distributor admin user only sees Sales Person and Customer in Entity List
    [Tags]    distadm       NRSZUANQ-29212       9.1
    Given user retrieve test data from "WhatsAppData.csv" located at "WhatsApp" folder
    ${whatsapp_data}=   get from dictionary   ${file_data}     dist_admin
    When user navigates to menu Master Data Management | WhatsApp
    Then user verifies Entity default for distributor
    Then user verifies contact able to use whatsapp feature
    Then user searches customer entity
    And user verifies contact without whatsapp number unable to use whatsapp feature

2 - HQ admin goes to WhatsApp contact list page
    [Documentation]    HQ admin can sees Sales HQ Customer in Entity List, able to filter by Distributor column
    [Tags]    hqadm       NRSZUANQ-29212       9.1
    Given user retrieve test data from "WhatsAppData.csv" located at "WhatsApp" folder
    ${whatsapp_data}=   get from dictionary   ${file_data}     hq_admin
    When user navigates to menu Master Data Management | WhatsApp
    Then user verifies Entity default for HQ user
    And user verifies Sales Person field able to filtered by Distributor column

3 - Verify distributor admin able to navigate to WhatsApp listing page using top header icon
    [Documentation]
    [Tags]    distadm       NRSZUANQ-29203       9.1
    Given user retrieve test data from "WhatsAppData.csv" located at "WhatsApp" folder
    ${whatsapp_data}=   get from dictionary   ${file_data}     dist_admin
    When user clicks on header contact icon after landing at main page
    Then user verifies Entity default for distributor
