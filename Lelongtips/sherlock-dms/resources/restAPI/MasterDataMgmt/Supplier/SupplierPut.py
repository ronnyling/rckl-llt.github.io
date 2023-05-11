from resources.restAPI import PROTOCOL, APP_URL
import json
from resources.restAPI.Common import APIMethod
from resources.restAPI.MasterDataMgmt.Supplier import SupplierPost
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class SupplierPut:

    @keyword('user updates supplier with ${data_type} data')
    def user_updates_supplier(self, data_type):
        sup_id = BuiltIn().get_variable_value("${supplier_id}")
        url = "{0}supplier/{1}".format(END_POINT_URL, sup_id)
        payload = SupplierPost.SupplierPost().payload_supplier()
        details = BuiltIn().get_variable_value("${update_supplier_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, payload)
        print("PUT Status code for supplier is " + str(response.status_code))
        print(response.text)
        if response.status_code != 200:
            return str(response.status_code), ""
        else:
            body_result = response.json()
            BuiltIn().set_test_variable("${status_code}", response.status_code)
            return body_result['PRIME_FLAG']

    def user_updates_supplier_details(self):
        sup_id = BuiltIn().get_variable_value("${supplier_id}")
        payload = {}
        url = "{0}supplier/{1}".format(END_POINT_URL, sup_id)
        details = BuiltIn().get_variable_value("${update_supplier_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, payload)
        print("PUT Status code for supplier is " + str(response.status_code))
        print(response.text)
        if response.status_code != 200:
            return str(response.status_code), ""
        else:
            body_result = response.json()
            BuiltIn().set_test_variable("${status_code}", response.status_code)
            return body_result['PRIME_FLAG']
