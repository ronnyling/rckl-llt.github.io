*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/PromoE2E/PromoSetup.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoAssignPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoApprove.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoApply.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoBuyTypeGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoEntitlementPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoCalculation/PromoDealCalculation.py
Library         ${EXECDIR}${/}resources/TransactionFormula.py
*** Test Case ***
1 - Able to create Promo and Deal Discount by Value - By Amount
    [Tags]   distadm   mrp    nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Value - By Amount
    And user approve promotion
    And user create sales order
    And user entitle promotion
    And user apply promotion
    And user calculate promo disc amount
    And assert api result with calculated result
    Then asserted result is matched

2 - Able to create Promo and Deal Discount by Value - By Quantity
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Value - By Quantity
    And user approve promotion
    And user create sales order
    And user entitle promotion
    And user apply promotion
    And user calculate promo disc amount
    And assert api result with calculated result
    Then asserted result is matched

3 - Able to create Promo and Deal Discount by Percentage - By Amount
    [Tags]   distadm   mrp    nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Percentage - By Amount
    And user approve promotion
    And user create sales order
    And user entitle promotion
    And user apply promotion
    And user calculate promo disc amount
    And assert api result with calculated result
    Then asserted result is matched

4 - Able to create Promo and Deal Discount by Percentage - By Quantity
    [Tags]   distadm   mrp    nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Percentage - By Quantity
    And user approve promotion
    And user create sales order
    And user entitle promotion
    And user apply promotion
    And user calculate promo disc amount
    And assert api result with calculated result
    Then asserted result is matched

5 - Able to create Promo and Deal Discount by Free Product - By Amount (OR condition)
    [Tags]   distadm   mrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Free Product (OR condition) - By Amount


6 - Able to create Promo and Deal Discount by Free Product - By Quantity (OR condition)
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Free Product (OR condition) - By Quantity

7 - Able to create Promo and Deal Discount by Free Product - By Amount (AND condition)
    [Tags]   distadm   mrp    nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Free Product (AND condition) - By Amount
    And user approve promotion
    And user create sales order
    And user entitle promotion
    And user apply promotion
    And user calculate promo disc amount
    And assert api result with calculated result
    Then asserted result is matched

8 - Able to create Promo and Deal Discount by Free Product - By Quantity (AND condition)
    [Tags]   distadm   mrp   nonmrp554466ff
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Free Product (AND condition) - By Quantity
    And user approve promotion
    And user create sales order
    And user entitle promotion
    And user apply promotion
    And user calculate promo disc amount
    And assert api result with calculated result
    Then asserted result is matched

#Promotion with max count
9 - Able to create Promo and Deal Discount By Value with Max Count - By Amount
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Value with Max Count - By Amount

10 - Able to create Promo and Deal Discount by Value with Max Count - By Quantity
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Value with Max Count - By Quantity

11 - Able to create Promo and Deal Discount by Percentage with Max Count - By Amount
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Percentage with Max Count - By Amount

12 - Able to create Promo and Deal Discount by Percentage with Max Count - By Quantity
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Percentage with Max Count - By Quantity

13 - Able to create Promo and Deal Discount by Free Product with Max Count - By Amount (OR condition)
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Free Product (OR condition) with Max Count - By Amount

14 - Able to create Promo and Deal Discount by Free Product with Max Count - By Quantity (OR condition)
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Free Product (OR condition) with Max Count - By Quantity

15 - Able to create Promo and Deal Discount by Free Product with Max Count - By Amount (AND condition)
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Free Product (AND condition) with Max Count - By Amount

16 - Able to create Promo and Deal Discount by Free Product with Max Count - By Quantity (AND condition)
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Free Product (AND condition) with Max Count - By Quantity

#Promotion with QPS scheme
17 - Able to create Promo and Deal Discount By Value with QPS - By Amount
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Value with QPS - By Amount

18 - Able to create Promo and Deal Discount by Value with QPS - By Quantity
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Value with QPS - By Quantity

19 - Able to create Promo and Deal Discount by Percentage with QPS - By Amount
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Percentage with QPS - By Amount

20 - Able to create Promo and Deal Discount by Percentage with QPS - By Quantity
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Percentage with QPS - By Quantity

21 - Able to create Promo and Deal Discount by Free Product with QPS - By Amount (OR condition)
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Free Product (OR condition) with QPS - By Amount

22 - Able to create Promo and Deal Discount by Free Product with QPS - By Quantity (OR condition)
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Free Product (OR condition) with QPS - By Quantity

23 - Able to create Promo and Deal Discount by Free Product with QPS - By Amount (AND condition)
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Free Product (AND condition) with QPS - By Amount

24 - Able to create Promo and Deal Discount by Free Product with QPS - By Quantity (AND condition)
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Free Product (AND condition) with QPS - By Quantity

#Promotion with Combi scheme
25 - Able to create Promo and Deal Discount By Value with Combi - By Amount
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Value with Combi - By Amount

26 - Able to create Promo and Deal Discount by Value with Combi - By Quantity
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Value with Combi - By Quantity

27 - Able to create Promo and Deal Discount by Percentage with Combi - By Amount
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Percentage with Combi - By Amount

28 - Able to create Promo and Deal Discount by Percentage with Combi - By Quantity
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Percentage with Combi - By Quantity

29 - Able to create Promo and Deal Discount by Free Product with Combi - By Amount (OR condition)
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Free Product (OR condition) with Combi - By Amount

30 - Able to create Promo and Deal Discount by Free Product with Combi - By Quantity (OR condition)
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Free Product (OR condition) with Combi - By Quantity

31 - Able to create Promo and Deal Discount by Free Product with Combi - By Amount (AND condition)
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Free Product (AND condition) with Combi - By Amount

32 - Able to create Promo and Deal Discount by Free Product with Combi - By Quantity (AND condition)
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Free Product (AND condition) with Combi - By Quantity

#Promotion with FOC Recurring scheme
33 - Able to create Promo and Deal Discount by Free Product with FOC Recurring - By Amount (OR condition)
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Free Product (OR condition) with FOC Recurring - By Amount

34 - Able to create Promo and Deal Discount by Free Product with FOC Recurring - By Quantity (OR condition)
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Free Product (OR condition) with FOC Recurring - By Quantity

35 - Able to create Promo and Deal Discount by Free Product with FOC Recurring - By Amount (AND condition)
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Free Product (AND condition) with FOC Recurring - By Amount

36 - Able to create Promo and Deal Discount by Free Product with FOC Recurring - By Quantity (AND condition)
    [Tags]   distadm   mrp   nonmrp
    Given user retrieves token access as ${user_role}
    When user creates promotion using Discount By Free Product (AND condition) with FOC Recurring - By Quantity
