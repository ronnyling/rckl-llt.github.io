from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from faker import Faker
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()


END_POINT_URL = PROTOCOL + "mobile-manager-ui" + APP_URL + "mm-device-profile"

class DeviceProfileDelete:

    @keyword("user delete created device profile")
    def user_delete_created_device_profile(self):
        device_profile_id = BuiltIn().get_variable_value("${device_profile_id}")
        url = "{0}/{1}".format(END_POINT_URL, device_profile_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records deleted are ", (body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)
