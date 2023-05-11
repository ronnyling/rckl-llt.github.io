*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesReturn/SalesReturnGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesReturn/SalesReturnPost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonTypeGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehousePost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehouseGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/CustomerGroupDiscount/CustomerGroupDiscountPost.py

#Test Setup        run keywords
#...    user retrieves token access as ${user_role}
#...    AND    user gets distributor by using code 'DistEgg'

*** Test Cases ***
1 - Able to perform autoapproval for good return
    [Documentation]    Able to perform autoapproval for good sales return when approval flag = ON
    [Tags]     distadm    9.5
    ${AppSetupDetails}=    create dictionary
    ...    ENABLE_GOOD_RET_APPROVAL=${True}
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as sysimp
    And user retrieves details of application setup
    Then user updates app setup details using fixed data
    Given user retrieves token access as ${user_role}
    When user retrieves all return
    Then expected return status code 200
#ENABLE_DAMAGE_RET_APPROVAL
#1. auto approval success for good return
#- turn on flag for good
#- turn on setting for good
#- create return
#- save and confirm return
#- verify status approved
#- confirm return

#prerequisite
#-turn on return approval, if unable, prompt error requesting to fix data/resolve pending txn
#    post good txn with status = pending approval
#    post good txn with status = approved, auto approval on
#    post bad txn with status = pending approval
#    post bad txn with status = approved, auto approval on
#    post bad with status = open, failed with gsv exceed
#
#    api - check all api in the enhancement 1. positive 2. validation 3. negative
#    good return
#        - autoapprove, pending
#        - config
#        - task list
#        -

#    bad return - rejct, autoapprove, pending
#
#
#
#
#    xxweb - ui component
#    xxhht - flow
#
#    setup - good return  < 2000 auto approval, >= 2000 manual approve, 2 levels
#    setup - damaged return gsv < 0.02, 0.02 <= gsv <= 0.05, 2 levels

#2. auto approval success for damaged return
#- turn on flag for damaged
#- turn on setting for damaged
#- create return
#- save and confirm return
#- verify status approved
#- confirm return
#3. auto approval fail for good return
#4. auto approval fail for damaged return
#5. manual approval approve success for good return
#- turn on flag for good
#- turn on setting for good
#- create return
#- save and confirm return
#- verify status pending
#- login as approver1 approve
#- login as approver2 approve
#- verify status approved
#- confirm return
#6. manual approval approve success for damaged return
#- turn on flag for damaged
#- turn on setting for damaged
#- create return
#- save and confirm return
#- verify status pending
#- login as approver1 approve
#- login as approver2 approve
#- verify status approved
#- confirm return
#7. manual approval approve fail for good return
#8. manual approval approve fail for damaged return
#9. manual approval reject success for good return
#- turn on flag for good
#- turn on setting for good
#- create return
#- save and confirm return
#- verify status pending
#- login as approver1 approve
#- login as approver2 reject
#- verify status rejected
#10. manual approval reject success for damaged return
#- turn on flag for good
#- turn on setting for good
#- create return
#- save and confirm return
#- verify status pending
#- login as approver1 approve
#- login as approver2 rejected
#- verify status rejected
#11. manual approval reject fail for good return
#- turn on flag for good
#- turn on setting for good
#- create return from immediate
#- save and confirm return
#- verify status pending
#- login as approver1 approve
#- login as approver2 rejected
#- login as approver2 approve
#- verify status approved
#12. manual approval reject fail for damaged return
#- turn on flag for damaged
#- turn on setting for damaged
#- create return from immediate
#- save and confirm return
#- verify status pending
#- login as approver1 approve
#- login as approver2 rejected
#- login as approver2 approve
#- verify status approved
#13. verify step by step approval log status change
#13. verify approver2 not able to confirm when approver1 reject
#- turn on flag for good
#- turn on setting for good
#- create return from immediate
#- save and confirm return
#- verify status pending
#- login as approver1 rejected
#- login as approver2 approve
#- login as approver2 approve
#- verify status rejected
