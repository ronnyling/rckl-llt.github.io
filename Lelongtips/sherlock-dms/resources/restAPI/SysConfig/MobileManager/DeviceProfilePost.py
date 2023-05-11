import json
import secrets
import string
from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.SysConfig.MobileManager import DeviceProfileGet

END_POINT_URL = PROTOCOL + "mobile-manager-ui" + APP_URL + "mm-device-profile"


class DeviceProfilePost(PageObject):
    STATUS_CODE = "${status_code}"

    @keyword("user creates device profile using ${data_type} data")
    def user_creates_device_profile_using_data(self, data_type):
        url = END_POINT_URL

        payload = self.create_payload_device_profile(fixed_data=None)

        if data_type == "fixed":
            fixed_data = BuiltIn().get_variable_value("${DeviceProfileDetails}")
            profile_code = fixed_data["PROFILE_CODE"]
            BuiltIn().set_test_variable("${profile_code}", profile_code)
            common = DeviceProfileGet.DeviceProfileGet()
            common.user_retrieves_device_profile("fixed")
            status_code = BuiltIn().get_variable_value(self.locator.STATUS_CODE)
            print()

            if status_code == 200:
                BuiltIn().set_test_variable(self.locator.STATUS_CODE, 201)
                return
            payload = self.create_payload_device_profile(fixed_data)

        print("POST URL", url)
        print("POST Payload", payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable(self.locator.STATUS_CODE, response.status_code)

        try:
            body_result = response.json()
            print("Result: ", body_result)
            device_profile_id = body_result['ID']
            BuiltIn().set_test_variable("${device_profile_id}", body_result['ID'])
            BuiltIn().set_test_variable("${profile_code}", body_result['PROFILE_CODE'])
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)
            return str(response.status_code), device_profile_id

    def create_payload_device_profile(self, fixed_data):
        """ Functions to create payload for module setup """
        random_char = "".join(secrets.choice(string.digits + string.ascii_letters) for _ in range(5))
        payload = {
            "PROFILE_CD": "CODETEST{0}".format(random_char),
            "ENG_TYPE": "AND",
            "WORK_DIR": "DIR{0}".format(random_char)
        }

        if fixed_data:
            payload.update((k, v) for k, v in fixed_data.items())

        payload = json.dumps(payload)

        return payload
