from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "promotion" + APP_URL


class SamplingDelete(object):
    """Function to delete sampling"""

    def user_deletes_sampling(self):
        sampling_id = BuiltIn().get_variable_value("${sampling_id}")
        url = "{0}sample/{1}".format(END_POINT_URL, sampling_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
