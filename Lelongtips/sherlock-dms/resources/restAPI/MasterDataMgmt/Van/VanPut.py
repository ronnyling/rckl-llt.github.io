import secrets

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from faker import Faker
import json
import datetime
from resources.restAPI.MasterDataMgmt.Van import VanGet
fake = Faker()
NOW = datetime.datetime.now()

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class VanPut(object):

    @keyword('user updates van with ${data_type} data')
    def user_updates_van_with(self, data_type):
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        van_id = BuiltIn().get_variable_value("${res_bd_van_id}")
        VanGet.VanGet.user_gets_van_by_using_id(self)
        van_details = BuiltIn().get_variable_value("${van_get_body_results}")
        url = "{0}distributors/{1}/setting-van/{2}".format(END_POINT_URL, distributor_id, van_id)
        payload = self.payload_van(van_details)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            res_bd_van_id = body_result['ID']
            BuiltIn().set_test_variable("${res_bd_van_id}", res_bd_van_id)
            BuiltIn().set_test_variable("${res_bd_van}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_van(self, van_details):
        payload = {
            "VAN_CD": van_details["VAN_CD"],
            "CORE_FLAGS": van_details["CORE_FLAGS"],
            "CREATED_BY": van_details["CREATED_BY"],
            "CREATED_DATE": van_details["CREATED_DATE"],
            "DIST_ID": van_details["DIST_ID"],
            "ID": van_details["ID"],
            "IS_DELETED": van_details["IS_DELETED"],
            "MODEL_NO": van_details["MODEL_NO"],
            "PLATE_NO": van_details["PLATE_NO"],
            "SI_DATE": van_details["SI_DATE"],
            "VAN_CD": van_details["VAN_CD"],
            "VAN_DESC": van_details["VAN_DESC"],
            "VERSION": 2,
            "VOLUME_CAPACITY": secrets.choice(range(1, 99)),
            "WEIGHT_CAPACITY": secrets.choice(range(1, 99))
        }
        details = BuiltIn().get_variable_value("${van_update}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Van Payload: ", payload)
        return payload