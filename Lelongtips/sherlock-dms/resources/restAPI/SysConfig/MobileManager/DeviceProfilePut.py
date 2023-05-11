import json

from robot.libraries.BuiltIn import BuiltIn

import resources.restAPI
from resources.restAPI.Common import APIMethod
from robot.api.deco import keyword
from faker import Faker
from resources.restAPI.SysConfig.MobileManager import DeviceProfilePost

fake = Faker()

END_POINT_URL = resources.restAPI.PROTOCOL + "mobile-manager-ui" + resources.restAPI.APP_URL + "mm-device-profile"


class DeviceProfilePut:

    def read_device_profile(self, specific_id):

        if specific_id:
            url = "{0}/{1}".format(END_POINT_URL, specific_id)
            common = APIMethod.APIMethod()
            response = common.trigger_api_request("GET", url, "")

        try:
            data = response.json()
            return str(response.status_code), data
        except Exception as e:
            print(e.__class__, "occured")
            return str(response.status_code), ""

    @keyword('user updates created attribute assign to record')
    def update_device_profile(self):
        data = DeviceProfilePost.DeviceProfilePost().user_creates_device_profile_using_data("random")
        specific_id = data[1]
        url = "{0}/{1}".format(END_POINT_URL, specific_id)
        if specific_id is not None:
            new_payload = self.read_device_profile(specific_id)
            new_payload = dict(new_payload[1])
            #new_payload.update((k, v) for k, v in update_info.items())
            new_payload = json.dumps(new_payload)
            common = APIMethod.APIMethod()
            response = common.trigger_api_request("PUT", url, new_payload)
            BuiltIn().set_test_variable("${status_code}", response.status_code)
            return str(response.status_code)

        return "403", ""
