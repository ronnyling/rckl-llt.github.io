from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()


END_POINT_URL = PROTOCOL + "vs-scorecard" + APP_URL


class VSKpiTypeGet(object):

    @keyword("user retrieves ${data_type} kpi type")
    def user_retrieves_user_setup(self, data_type):
        url = "{0}vs-kpi-type".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return str(response.status_code), response.json()




