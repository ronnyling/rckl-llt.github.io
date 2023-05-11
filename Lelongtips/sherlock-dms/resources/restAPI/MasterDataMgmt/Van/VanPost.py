from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from faker import Faker
import secrets
import json
import datetime
fake = Faker()
NOW = datetime.datetime.now()

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class VanPost(object):
    """ Functions to create van """

    @keyword('user creates van with ${data_type} data')
    def user_creates_van_with(self, data_type):
        """ Function to create van using fixed/random data """
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributors/{1}/setting-van".format(END_POINT_URL, distributor_id)
        payload = self.payload_van()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            res_bd_van_id = body_result['ID']
            BuiltIn().set_test_variable("${res_bd_van_id}", res_bd_van_id)
            BuiltIn().set_test_variable("${res_bd_van}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_van(self):
        """ Function for van payload content """
        payload = {
            "VAN_CD": 'VAN' + str(secrets.choice(range(1, 99999))),
            "VAN_DESC": fake.word(),
            "PLATE_NO": 'PlateNo' + str(secrets.choice(range(1, 1000))),
            "SI_DATE": NOW.strftime("%Y-%m-%d"),
            "WEIGHT_CAPACITY": secrets.choice(range(1, 99)),
            "VOLUME_CAPACITY": secrets.choice(range(1, 99)),
        }
        details = BuiltIn().get_variable_value("${van_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Van Payload: ", payload)
        return payload
