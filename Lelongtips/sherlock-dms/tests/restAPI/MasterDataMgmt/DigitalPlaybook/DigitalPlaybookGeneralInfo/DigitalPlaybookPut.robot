*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookGeneralInfo/DigitalPlaybookGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookGeneralInfo/DigitalPlaybookPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookGeneralInfo/DigitalPlaybookPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookGeneralInfo/DigitalPlaybookDelete.py
Library          ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py

Test Setup    User sets the feature setup for playbook to on passing with 'playbk' value

*** Test Cases ***
1 - Able to PUT Playbook with random data
    [Documentation]    Able to edit Playbook with random generated data via API
    [Tags]  hqadm    9.2     NRSZUANQ-44760
    Given user retrieves token access as ${user_role}
    When user creates playbook with random data
    Then expected return status code 201
    When user updates playbook with random data
    Then expected return status code 200
    When user deletes playbook with created data
    Then expected return status code 200

2 - Able to PUT Playbook with fixed data
    [Documentation]  Able to edit playbook with fixed data via API
    [Tags]  hqadm    9.2     NRSZUANQ-44760
    ${playbook_general_details}=    create dictionary
    ...     PRIORITY=H
    ...     PLAYBOOK_TYPE_CODE=Play202
    ...     PLAYBK_ASSIGN_TO=C
    ...     PRODUCT_HIERARCHY_DESCRIPTION=General Product Hierarchy
    ...     START_DATE=2050-01-01
    ...     END_DATE=2060-01-01
    ...     THUMBNAIL_FILE_NAME=test-1610195023076.jpg
    ...     THUMBNAIL_FILE_TYPE=jpg
    ...     THUMBNAIL_FILE_SIZE=${115710}
    ...     THUMBNAIL_FILE_URL=playbk-setup/THUMBNAIL_IMAGE/test-1610195023076.jpg
    ...     STATUS=${TRUE}
    set test variable   &{playbook_general_details}
    ${playbook_content_details}=    create dictionary
    ...     CONTENT_DESC=Test Playbook Content
    ...     THUMBNAIL_FILE_NAME=test-1610195023076.jpg
    ...     THUMBNAIL_FILE_TYPE=jpg
    ...     THUMBNAIL_FILE_SIZE=${115710}
    ...     THUMBNAIL_FILE_URL=playbk-setup/THUMBNAIL_IMAGE/test-1610195023076.jpg
    ...     ATTACHMENT_FILE_NAME=PPT_B003-1612233509201.ppt
    ...     ATTACHMENT_FILE_SIZE=221
    ...     ATTACHMENT_FILE_TYPE=application/vnd.ms-powerpoint
    ...     ATTACHMENT_FILE_LENGTH=4
    ...     ATTACHMENT_URL=/objectstore-svc/api/v1.0/storage/playbook_content/ATTACHMENT/PPT_B003-1612233509201.ppt
    set test variable   &{playbook_content_details}
    Given user retrieves token access as ${user_role}
    When user creates playbook with random data
    Then expected return status code 201
    When user updates playbook with fixed data
    Then expected return status code 200
    When user deletes playbook with created data
    Then expected return status code 200

3 - Unable to PUT Playbook with existing Playbook Description
    [Documentation]  Unable to edit playbook with existing playbook description
    [Tags]  hqadm   9.2     NRSZUANQ-44760
    Given user retrieves token access as ${user_role}
    When user retrieves playbook by valid id
    Then expected return status code 200
    When user creates playbook with random data
    Then expected return status code 201
    When user updates playbook with existing data
    Then expected return status code 409
    When user deletes playbook with created data
    Then expected return status code 200

4 - Unable to PUT Playbook with invalid data
    [Documentation]  Unable to edit playbook with invalid priority, playbook assign to, product hierarchy id, product catergory id,
    ...     product category value id, start date, end date, thumbnail file name, thumbnail file type, thumbnail file size and status.
    [Tags]  hqadm   9.2     NRSZUANQ-44760
    ${playbook_general_details}=    create dictionary
    ...     PRIORITY=A
    ...     PLAYBK_ASSIGN_TO=A
    ...     PRD_HIER_ID=invalidID
    ...     PRDCAT_ID=invalidID
    ...     PRDCAT_VALUE_ID=invalidID
    ...     START_DATE=invalidDate
    ...     END_DATE=invalidDate
    ...     THUMBNAIL_FILE_NAME=${200}
    ...     THUMBNAIL_FILE_TYPE=${200}
    ...     THUMBNAIL_FILE_SIZE=string
    ...     STATUS=${0}
    set test variable   &{playbook_general_details}
    Given user retrieves token access as ${user_role}
    When user creates playbook with random data
    Then expected return status code 201
    When user updates playbook with fixed data
    Then expected return status code 400
    When user deletes playbook with created data
    Then expected return status code 200

5 - Unable to PUT Playbook with past date in start date field
    [Documentation]  Unable to edit playbook with past date in the start date field
    [Tags]  hqadm   9.2     NRSZUANQ-44760
    ${playbook_general_details}=    create dictionary
    ...     START_DATE=2010-01-01
    set test variable   &{playbook_general_details}
    Given user retrieves token access as ${user_role}
    When user creates playbook with random data
    Then expected return status code 201
    When user updates playbook with fixed data
    Then expected return status code 400
    When user deletes playbook with created data
    Then expected return status code 200

6 - Unable to PUT Playbook with earlier end date than start date
    [Documentation]  Unable to edit playbook with earlier end date than start date
    [Tags]  hqadm   9.2     NRSZUANQ-44760
    ${playbook_general_details}=    create dictionary
    ...     START_DATE=2050-01-02
    ...     END_DATE=2050-01-01
    set test variable   &{playbook_general_details}
    Given user retrieves token access as ${user_role}
    When user creates playbook with random data
    Then expected return status code 201
    When user updates playbook with fixed data
    Then expected return status code 400
    When user deletes playbook with created data
    Then expected return status code 200

7 - Unable to PUT Playbook using distributor access and get 403
    [Documentation]  To validate distributor admin unable to edit Playbook
    [Tags]  distadm   9.2     NRSZUANQ-44760
    Given user retrieves token access as ${user_role}
    When user retrieves all playbook
    Then expected return status code 200
    When user retrieves playbook by valid id
    Then expected return status code 200
    When user updates playbook with random data
    Then expected return status code 403