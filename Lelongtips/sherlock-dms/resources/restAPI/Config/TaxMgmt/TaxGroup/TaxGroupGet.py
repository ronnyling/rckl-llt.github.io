from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json, secrets
END_POINT_URL = PROTOCOL + "taxation" + APP_URL
METADATA_END_POINT_URL = PROTOCOL + "metadata" + APP_URL

class TaxGroupGet(object):
    TG_ID = "${tax_group_id}"
    NP_TG_ID = "${np_tax_group_id}"
    @keyword('user retrieves ${cond} tax group')
    def user_get_tax_group(self, cond):
        tax_group_id = BuiltIn().get_variable_value(self.TG_ID)
        if cond == 'all':
            url = "{0}tax-group".format(END_POINT_URL)
        else:
            url = "{0}tax-group/{1}".format(END_POINT_URL, tax_group_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        return response.json()

    @keyword ("user get tax group by code ${svc_cd}")
    def user_get_tax_group_by_code(self, svc_cd):
        filter_ts = {"TAX_GRP_CD": {"$eq": svc_cd}}
        filter_ts = json.dumps(filter_ts)
        url = "{0}tax-group?filter={1}".format(END_POINT_URL, filter_ts)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        assert response.status_code == 200, "Unable to retrieve tax group"
        body_result = response.json()[0]
        print("Tax body result: ",body_result)
        if body_result["PRIME_FLAG"] == "NON_PRIME":
            BuiltIn().set_test_variable(self.NP_TG_ID, body_result["ID"])
        else:
            BuiltIn().set_test_variable(self.TG_ID, body_result["ID"])
        return body_result

    @keyword("user get random tax group by ${prime} principal flag")
    def user_get_random_tax_group_by_principal_flag(self, flag):
        filter_ts = {"PRIME_FLAG": {"$eq": flag}, "TYPE": {"$eq": "P"}}
        filter_ts = json.dumps(filter_ts)
        url = "{0}module-data/tax-group?filter={1}".format(METADATA_END_POINT_URL, filter_ts)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        assert response.status_code == 200, "Unable to retrieve tax group"
        body_result = response.json()
        body_result = secrets.choice(body_result)
        if body_result["PRIME_FLAG"] == "NON_PRIME":
            BuiltIn().set_test_variable(self.NP_TG_ID, body_result["ID"])
        else:
            BuiltIn().set_test_variable(self.TG_ID, body_result["ID"])
        return body_result

    def retrieve_get_tax_group_by_type(self, tax_type):
        filter_ts = {"TYPE": {"$eq": tax_type}}
        filter_ts = json.dumps(filter_ts)
        url = "{0}tax-group?filter={1}".format(END_POINT_URL, filter_ts)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        assert response.status_code == 200, "Unable to retrieve tax group"
        body_result = response.json()[0]
        print("Tax body result: ",body_result)
        if body_result["PRIME_FLAG"] == "NON_PRIME":
            BuiltIn().set_test_variable(self.NP_TG_ID, body_result["ID"])
        else:
            BuiltIn().set_test_variable(self.TG_ID, body_result["ID"])
        return body_result