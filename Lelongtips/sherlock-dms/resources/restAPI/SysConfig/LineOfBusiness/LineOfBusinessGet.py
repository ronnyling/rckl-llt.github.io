from resources.restAPI import PROTOCOL, APP_URL, BuiltIn
import json, secrets
from resources.restAPI.Common import APIMethod
from robot.api.deco import keyword
END_POINT_URL = PROTOCOL + "setting" + APP_URL

class LineOfBusinessGet:


    @keyword('user retrieve ${cond} lob ')
    def user_retrieve_lob(self, cond):
        url = "{0}lob-ref/".format(END_POINT_URL)
        payload = self.product_sector_payload()
        payload = json.dumps(payload)
        print(payload)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        print("Get Status code for line of business info is " + str(response.status_code))
        if response.status_code != 200:
            print(response.text)
            return str(response.status_code), ""

    @keyword("get lob by Field:${field} Value:${Value}")
    def get_lob_by_field_and_value(self, field, value):
        filter_lob = {field: {"$eq": value}}
        filter_lob = json.dumps(filter_lob)
        url = "{0}lob-ref/?filter={1}".format(END_POINT_URL, filter_lob)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve lob"
        body_result = response.json()
        choice = secrets.choice(body_result)
        BuiltIn().set_test_variable("${rs_bd_lob}", choice)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return choice