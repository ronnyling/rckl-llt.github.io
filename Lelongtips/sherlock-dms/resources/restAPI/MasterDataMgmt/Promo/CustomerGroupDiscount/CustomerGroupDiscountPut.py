import json
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.MasterDataMgmt.Promo.CustomerGroupDiscount import CustomerGroupDiscountGet

END_POINT_URL = PROTOCOL + "promotion" + APP_URL

class CustomerGroupDiscountPut(object):

    def user_update_customer_group_discount(self):
        group_disc_id = BuiltIn().get_variable_value("${res_bd_grpdisc_id}")
        get_response = CustomerGroupDiscountGet.CustomerGroupDiscountGet.user_gets_customer_group_disc_by_id(self)
        url = "{0}cust-group-discount/{1}".format(END_POINT_URL, group_disc_id)
        payload = self.payload_new(get_response)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        if response.status_code == 201:
            body_result = response.json()
            print("PUT Body Result: ", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_new(self, get_response):
        payload = {
               "ID":get_response["ID"],
               "GRPDISC_CD": get_response["GRPDISC_CD"],
               "GRPDISC_DESC": get_response["GRPDISC_DESC"],
               "REF_NO": get_response["REF_NO"],
               "PRDASSIGN_IND": get_response["PRDASSIGN_IND"],
               "CUSTGRP_LVL": get_response["CUSTGRP_LVL"],
               "CUSTGRP_VAL_ID": get_response["CUSTGRP_VAL_ID"],
               "DISC_TYPE": get_response["DISC_TYPE"],
               "DISCOUNT": get_response["DISCOUNT"],
               "APPLY_ON": get_response["APPLY_ON"],
               "CLAIMABLE_IND": get_response["CLAIMABLE_IND"],
               "START_DT": get_response["START_DT"],
               "END_DT": get_response["END_DT"],
               "STATUS": get_response["STATUS"],
               "CUSTGRP_LVL_ID": get_response["CUSTGRP_LVL_ID"]
            }
        details = BuiltIn().get_variable_value("${GroupDiscountDetails}")
        if details:
           payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        return payload