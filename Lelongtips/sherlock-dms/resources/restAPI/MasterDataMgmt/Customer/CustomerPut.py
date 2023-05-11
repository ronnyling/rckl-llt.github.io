import json
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from resources.restAPI.MasterDataMgmt.Customer.CustomerPost import CustomerPost

CUST_END_POINT_URL = PROTOCOL + "profile-cust" + APP_URL
METADATA_END_POINT_URL = PROTOCOL + "metadata" + APP_URL

class CustomerPut(object):
    DISTRIBUTOR_ID = "${distributor_id}"
    CUSTOMER_ID = "${cust_id}"

    def user_puts_customer_data(self):
        dist_id = BuiltIn().get_variable_value("${dist_id}")
        cust_id = BuiltIn().get_variable_value("${cust_id}")
        cust_details = BuiltIn().get_variable_value("${cust_details}")
        url = "{0}distributors/{1}/customer/{2}".format(CUST_END_POINT_URL, dist_id, cust_id)
        self.gen_payload(cust_details)
        payload = self.gen_payload(cust_details)
        payload = json.dumps(payload)
        common = APIMethod.APIMethod()
        print("payload = " + str(payload))
        response = common.trigger_api_request("PUT", url, payload)
        body_result = response.json()
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return body_result

    def gen_payload(self, payload):
        payload["OUT_BLNCE"] = float(payload["OUT_BLNCE"])
        cr_limit = payload["CRDT_LIMIT"]
        cust_disc = payload["CUST_DISC"]
        payload["CRDT_LIMIT"] = float(cr_limit) if cr_limit is not None else 0
        payload["CUST_DISC"] = float(cust_disc) if cust_disc is not None else 0
        return payload