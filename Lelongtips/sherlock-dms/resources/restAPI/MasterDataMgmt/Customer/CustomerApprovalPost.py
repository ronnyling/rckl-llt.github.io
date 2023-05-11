import json

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL

CUST_END_POINT_URL = PROTOCOL + "profile-cust" + APP_URL


class CustomerApprovalPost(object):

    @keyword('user approves created customer')
    def update_cust_status(self):
        cust_id = BuiltIn().get_variable_value("${cust_id}")
        payload = self.gen_payload(cust_id)
        url = "{0}customer/approve".format(CUST_END_POINT_URL, payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print("payload = " + str(payload))
        assert response.status_code == 200
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def gen_payload(self, cust_id):
        tmp = {}
        payload = []
        tmp["CUST_ID"] = cust_id
        payload.append(tmp)
        payload = json.dumps(payload)
        return payload

