*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookGeneralInfo/DigitalPlaybookGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookGeneralInfo/DigitalPlaybookPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookGeneralInfo/DigitalPlaybookDelete.py
Library          ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupGet.py
Library          ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py

#Test Setup    User sets the feature setup for playbook to on passing with 'playbk' value


*** Test Cases ***
1 - Able to POST Playbook with random data
    [Documentation]    Able to create valid Playbook with random generated data via API
    [Tags]  hqadm   9.2     NRSZUANQ-44760
    Given user retrieves token access as ${user_role}
    When user creates playbook with random data
    Then expected return status code 201
    When user deletes playbook with created data
    Then expected return status code 200

2 - Able to POST Playbook with fixed data
    [Documentation]  Able to create valid playbook with fixed data via API
    [Tags]  hqadm   9.2     NRSZUANQ-44760
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
    When user creates playbook with fixed data
    Then expected return status code 201
    When user deletes playbook with created data
    Then expected return status code 200

3 - Unable to POST Playbook with existing Playbook Description
    [Documentation]  Unable to create playbook with existing playbook description
    [Tags]  hqadm   9.2     NRSZUANQ-44760
    Given user retrieves token access as ${user_role}
    When user retrieves playbook by valid id
    Then expected return status code 200
    When user creates playbook with existing data
    Then expected return status code 409

4 - Unable to POST Playbook with invalid data
    [Documentation]  Unable to create playbook with invalid priority, playbook assign to, product hierarchy id, product catergory id,
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
    When user creates playbook with fixed data
    Then expected return status code 400

5 - Unable to POST Playbook with past date in start date field
    [Documentation]  Unable to create playbook with past date in the start date field
    [Tags]  hqadm   9.2     NRSZUANQ-44760
    ${playbook_general_details}=    create dictionary
    ...     START_DATE=2010-01-01
    set test variable   &{playbook_general_details}
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 400

6 - Unable to POST Playbook with earlier end date than start date
    [Documentation]  Unable to create playbook with earlier end date than start date
    [Tags]  hqadm   9.2     NRSZUANQ-44760
    ${playbook_general_details}=    create dictionary
    ...     START_DATE=2050-01-02
    ...     END_DATE=2050-01-01
    set test variable   &{playbook_general_details}
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 400

7 - Unable to POST Playbook using distributor access and get 403
    [Documentation]  To validate distributor admin unable to create Playbook
    [Tags]  distadm   9.2     NRSZUANQ-44760
    Given user retrieves token access as ${user_role}
    When user creates playbook with random data
    Then expected return status code 403

8 - Able to POST playbook and save video type content with file length
    [Documentation]  To validate user able to save video type content with video duration
    [Tags]  hqadm    9.2    NRSZUANQ-46114
    ${playbook_content_details}=    create dictionary
    ...     ATTACHMENT_FILE_NAME=videoplayback-1610956795973.mp4
    ...     ATTACHMENT_FILE_SIZE=1711
    ...     ATTACHMENT_FILE_TYPE=V
    ...     ATTACHMENT_FILE_LENGTH=0:55
    ...     ATTACHMENT_URL=/objectstore-svc/api/v1.0/storage/playbook_content/ATTACHMENT/videoplayback-1610956795973.mp4
    set test variable   &{playbook_content_details}
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    And validates content file length saved
    When user deletes playbook with created data
    Then expected return status code 200

9 - Able to POST playbook and save pdf type content with file length
    [Documentation]  To validate user able to save pdf type content with no of page
    [Tags]  hqadm    9.2    NRSZUANQ-46114
    ${playbook_content_details}=    create dictionary
    ...     ATTACHMENT_FILE_NAME=PDF_B002-1613704303747.pdf
    ...     ATTACHMENT_FILE_SIZE=511
    ...     ATTACHMENT_FILE_TYPE=A
    ...     ATTACHMENT_FILE_LENGTH=1
    ...     ATTACHMENT_URL=/objectstore-svc/api/v1.0/storage/playbook_content/ATTACHMENT/PDF_B002-1613704303747.pdf
    set test variable   &{playbook_content_details}
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    And validates content file length saved
    When user deletes playbook with created data
    Then expected return status code 200

10 - Unable to POST valid file with invalid size to objectstore
    [Documentation]  To validate user unable to POST valid file with invalid size to objectstore playbook folder
    [Tags]  hqadm    9.2    NRSZUANQ-49642
    Given user retrieves token access as ${user_role}
    When user uploads valid file with invalid size to object store
    Then expected return status code 400

11 - Unable to POST invalid file with valid size to objectstore
    [Documentation]  To validate user unable to POST invalid file with valid size to objectstore playbook folder
    [Tags]  hqadm    9.2    NRSZUANQ-49642
    Given user retrieves token access as ${user_role}
    When user uploads invalid file with valid size to object store
    Then expected return status code 400

12 - Able to POST valid file with valid size to objectstore
    [Documentation]  To validate user able to POST valid file with valid size to objectstore playbook folder
    [Tags]  hqadm    9.2    NRSZUANQ-49642
    Given user retrieves token access as ${user_role}
    When user uploads valid file with valid size to object store
    Then expected return status code 201
