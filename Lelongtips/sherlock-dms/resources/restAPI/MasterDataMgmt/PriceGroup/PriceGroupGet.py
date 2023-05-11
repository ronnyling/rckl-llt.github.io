import json
import secrets

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
END_POINT_URL = PROTOCOL + "price" + APP_URL


class PriceGroupGet(object):

    def user_retrieves_all_price_group(self):
        url = "{0}price".format(END_POINT_URL)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${price_group_ls}", response.json())
        return response.status_code

    def get_price_group_by_id(self):
        pg_id = BuiltIn().get_variable_value("${price_group_id}")
        url = "{0}price/{1}".format(END_POINT_URL, pg_id)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response.status_code

    @keyword("get price group by code ${code}")
    def get_price_group_by_code(self, code):
        if code != "random":
            filter_pg = {"PRICE_GRP_CD": {"$eq": code}}
        else:
            filter_pg = {}
            filter_pg = json.dumps(filter_pg)
        url = "{0}price?filter={1}".format(END_POINT_URL, filter_pg)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve price group"
        body_result = response.json()
        if code == "random":
            x = secrets.choice(range(0, len(body_result)))
            BuiltIn().set_test_variable("${price_group}", body_result[x])
            return body_result[x]
        else:
            BuiltIn().set_test_variable("${price_group", body_result[0])
            return body_result[0]
