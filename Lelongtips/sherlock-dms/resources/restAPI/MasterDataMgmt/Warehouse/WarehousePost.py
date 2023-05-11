from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from setup.hanaDB import HanaDB
import secrets
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from faker import Faker
fake = Faker()

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class WarehousePost(object):
    """ Functions to create warehouse """

    @keyword('user creates warehouse with ${data_type} data')
    def user_creates_warehouse_with(self, data_type):
        """ Function to create warehouse using fixed/random data """
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributors/{1}/warehouse".format(END_POINT_URL, distributor_id)
        payload = self.payload_warehouse(data_type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            res_bd_warehouse_id = body_result['ID']
            # HanaDB.HanaDB().connect_database_to_environment()
            # HanaDB.HanaDB().user_validates_database_data("warehouse", body_result)
            # HanaDB.HanaDB().disconnect_from_database()
            BuiltIn().set_test_variable("${body_result}", body_result)
            res_bd_warehouse_flag = body_result['PRIME_FLAG']
            res_bd_warehouse_desc = body_result['WHS_DESC']
            if res_bd_warehouse_flag == 'NON_PRIME':
                BuiltIn().set_test_variable("${res_bd_warehouse_id}", res_bd_warehouse_id)
                BuiltIn().set_test_variable("${res_bd_non_prime_warehouse}", body_result)
            else:
                BuiltIn().set_test_variable("${res_bd_warehouse_desc}", res_bd_warehouse_desc)
                BuiltIn().set_test_variable("${res_bd_prime_warehouse}", body_result)
            BuiltIn().set_test_variable("${res_bd_warehouse_id}", res_bd_warehouse_id)
            BuiltIn().set_test_variable("${res_bd_warehouse}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)


    def payload_warehouse(self, data_type):
        """ Function for warehouse payload content """
        van_id = BuiltIn().get_variable_value("${res_bd_van_id}")
        if data_type == 'existing' or data_type == 'update':
            res_bd_warehouse_cd = BuiltIn().get_variable_value("${res_bd_warehouse['WHS_CD']}")
            res_bd_warehouse_prime = BuiltIn().get_variable_value("${res_bd_warehouse['PRIME_FLAG']}")
        else:
            res_bd_warehouse_cd = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(4))
            res_bd_warehouse_prime = secrets.choice(["PRIME", "NON_PRIME"])

        payload = {
            "WHS_CD": res_bd_warehouse_cd,
            "WHS_DESC": fake.word(),
            "WHS_BATCH_TRACE": False,
            "WHS_EXP_MAND": False,
            "WHS_IS_DAMAGE": False,
            "WHS_IS_VAN": False,
            "VAN_ID": None,
            "PRIME_FLAG": res_bd_warehouse_prime,
            "SHIP_TO": {"ID": "11B7F2A2:1F75A5C1-A51F-4149-B1CE-171F08B74A65"}
            #Infinity2 please add in pre-requisite for this ship to
        }
        details = BuiltIn().get_variable_value("${warehouse_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        if van_id is not None and payload['PRIME_FLAG'] == "PRIME":
            payload['WHS_IS_VAN'] = True
            payload['VAN_ID'] = {"ID": van_id}
        payload = json.dumps(payload)
        print("Warehouse Payload: ", payload)
        return payload
