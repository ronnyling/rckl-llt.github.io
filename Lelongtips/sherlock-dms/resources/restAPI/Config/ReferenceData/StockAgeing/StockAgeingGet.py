import json
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class StockAgeingGet(object):

    @keyword("user retrieves all aging period")
    def user_retrieves_all_aging_period(self):
        url = "{0}aging-period".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response.status_code

    @keyword("user retrieves the created aging period by ID")
    def user_retrieves_the_created_aging_period(self):
        aging_period_id = BuiltIn().get_variable_value("${AgingPeriodID}")
        aging_period_code = BuiltIn().get_variable_value("${AgingPeriodCode}")
        aging_period_desc = BuiltIn().get_variable_value("${AgingPeriodDesc}")
        url = "{0}aging-period/{1}".format(END_POINT_URL, aging_period_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if "PERIOD_DESC" in response.text:
            data = response.json()
            print(json.dumps(data, indent=4))
            age_code = data["PERIOD_CD"]
            age_desc = data["PERIOD_DESC"]
            if aging_period_code == age_code and aging_period_desc == age_desc:
                print("Get by ID verified")
