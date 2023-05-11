*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/ExecutionResult/ExecutionImages/ExecutionImagesPost.py

*** Test Cases ***
1 - Able to retrieve all execution images with different user roles
    [Documentation]    Able to retrieve all execution images with different user roles
    [Tags]    sysimp    hqadm    distadm    9.1
    Given user retrieves token access as hqadm
    When user retrieves all execution images
    Then expected return either status code 200 or status code 204

2 - Validate end date greater than or equal to start date
    [Documentation]    Validate end date greater than or equal to start date
    [Tags]    sysimp    hqadm    distadm    9.1
    [Template]    Validate end date greater than or equal to start date
    #start_date      #end_date    #expected_status    #expected_status1
    2020-03-26       2020-03-26          200                204
    2020-01-14       2020-04-03          200                204
    2020-04-03       2020-01-14          400              ${empty}

3 - Validate fields shown with each activity selected
    [Documentation]    Validate respective fields shown with each activity selected
    [Tags]    sysimp    hqadm    distadm    9.1    NRSZUANQ-28766    NRSZUANQ-28781    NRSZUANQ-28782    NRSZUANQ-32095
    [Template]    Validate fields shown with each activity selected
    #Activity                       #On Promo    #Stock Availability   #Compliance    #expected_status    #expected_status1
    PRICE_AUDIT                      ${true}         ${false}            ${false}           200                 204
    DIST_CHECK                       ${true}         ${true}             ${false}           200                 204
    FACING_AUDIT                     ${false}        ${false}            ${false}           200                 204
    PLANO_CHECK                      ${false}        ${false}            ${true}            200                 204
    PROMO_CHECK                      ${false}        ${false}            ${true}            200                 204
    POSM_NW_INS                      ${false}        ${false}            ${false}           200                 204
    POSM_RECORD                      ${false}        ${false}            ${false}           200                 204