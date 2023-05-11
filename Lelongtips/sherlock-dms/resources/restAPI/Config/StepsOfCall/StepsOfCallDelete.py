from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common.APIMethod import APIMethod
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "setting" + APP_URL

class StepsOfCallDelete(object):

    @keyword('user deletes the created soc')
    def user_deletes_the_created_soc(self):
        soc_id = BuiltIn().get_variable_value("${soc_id}")
        url = "{0}steps-of-call/{1}".format(END_POINT_URL, soc_id)
        print("URL_SOC_GET: ", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            body_result = response.json()
            print("Result: ", body_result)
