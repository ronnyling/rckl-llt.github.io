import secrets, json
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI.Merchandising.MerchandisingSetup.StoreSpace import StoreSpaceGet
END_POINT_URL = PROTOCOL + "merchandising" + APP_URL

class StoreSpacePost(object):
    STORE_SPACE_DETAILS = "${store_space_details}"
    STORE_SPACE_LEVEL_DETAILS = "${store_space_level_details}"
    STORE_SPACE_PAYLOAD = "${res_bd_store_space_payload}"

    @keyword('user creates store space with ${data_type} data')
    def user_creates_store_space_with(self, data_type):
        url = "{0}merchandising/merc-store-space".format(END_POINT_URL)
        payload = self.payload_store(data_type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable(self.STORE_SPACE_PAYLOAD, body_result)
            BuiltIn().set_test_variable("${res_bd_store_space_id}", body_result["ID"])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @keyword('user creates store space level')
    def user_creates_store_space_level(self):
        res_bd_store_space_id = BuiltIn().get_variable_value("${res_bd_store_space_id}")
        url = "{0}merchandising/merc-store-space/{1}/merc-store-space-level".format(END_POINT_URL, res_bd_store_space_id)
        payload = self.payload_level()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable(self.STORE_SPACE_PAYLOAD, body_result)
            BuiltIn().set_test_variable("${res_bd_store_space_level_id}", body_result['INSERT'][0]['ID'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_store(self, data_type):
        if data_type == 'existing':
            body_result = BuiltIn().get_variable_value(self.STORE_SPACE_PAYLOAD)
            store_code = body_result['SPACE_CD']
        else:
            store_code = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(15))
        store_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(20))
        payload = {
                "SPACE_CD":store_code,
                "SPACE_DESC": store_desc
        }
        details = BuiltIn().get_variable_value(self.STORE_SPACE_DETAILS)
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Store Space Payload: ", payload)
        return payload

    def payload_level(self):
        StoreSpaceGet.StoreSpaceGet.user_retrieves_all_store_spaces_level(self)
        level_id = BuiltIn().get_variable_value("${rand_level_id}")
        cust_group_id = BuiltIn().get_variable_value("${rand_cust_group_id}")
        payload =[{
                "LEVEL_ID": level_id,
                "CUST_GROUP_ID": cust_group_id
            }]

        payload = json.dumps(payload)
        print("Store Space Level Payload: ", payload)
        return payload
