*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/AppSetup/DeliveryOptimizationEditPage.py
Library         ${EXECDIR}${/}resources/components/Tab.py

*** Test Cases ***
1 - Able to update Delivery Optimization using random data
    [Documentation]    Able to update Replenishment using random data
    [Tags]    hqadm    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Delivery Optimization tab
    Then user updates Delivery Optimization using random data
    And general updated successfully with message 'Record updated successfully'

2 - Able to update Delivery Optimization using fixed data
    [Documentation]    Able to update Delivery Optimization using given data
    [Tags]    hqadm    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Delivery Optimization tab
    ${DeliveryOptimizationDetails}=    create dictionary
    ...    Enable Delivery Optimisation=${False}
    ...    Delivery Optimisation by=Weight
    ...    Address Fields for Delivery Optimisation=all
    set test variable    &{DeliveryOptimizationDetails}
    Then user updates Delivery Optimization using fixed data
    And general updated successfully with message 'Record updated successfully'

#Only sysimp can access
3 - Able to update Delivery Optimization using fixed data
    [Documentation]    Able to update Delivery Optimization using given data
    [Tags]    hqadm    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Delivery Optimization tab
    ${DeliveryOptimizationDetails}=    create dictionary
    ...    Open Route Service Key=Check123
    set test variable    &{DeliveryOptimizationDetails}
    Then user updates Delivery Optimization using fixed data
    And general updated successfully with message 'Record updated successfully'
