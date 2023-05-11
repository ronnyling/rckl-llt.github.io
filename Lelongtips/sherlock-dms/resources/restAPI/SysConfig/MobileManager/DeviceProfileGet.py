from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "mobile-manager-ui" + APP_URL + "mm-device-profile"


class DeviceProfileGet:
    """ Functions related to module setup GET request """

    @keyword("user retrieves ${data_type} device profile")
    def user_retrieves_device_profile(self, data_type):
        """ Functions to retrieve all/created/fixed module setup """
        url = END_POINT_URL

        if data_type == "created":
            device_profile_id = BuiltIn().get_variable_value("${device_profile_id}")
            url = "{0}/{1}".format(END_POINT_URL, device_profile_id)
        elif data_type == "fixed":
            url = "{0}/".format(END_POINT_URL)

        print("GET URL", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)

        try:
            body_result = response.json()
            print("Result: ", body_result)

        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)
