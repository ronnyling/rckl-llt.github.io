import json
import secrets

from robot.api.deco import keyword

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "dynamic-attribute" + APP_URL


class AttributeValueSetupGet(object):

    def user_gets_attribute_value_by(self, attribute):
        filter_data = {"ATTRIBUTE": {"$eq": attribute}}
        return self.get_attribute_id_by(filter_data)

    def user_gets_attribute_id_by_value(self, attribute_value):
        filter_data = {"ATTRIBUTE_VALUE": {"$eq": attribute_value}}
        return self.get_attribute_id_by(filter_data)

    def get_attribute_id_by(self, filter_data):
        filter_data = json.dumps(filter_data)
        url = "{0}attribute-value-creation?filter={1}".format(END_POINT_URL, filter_data)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unabletoretrieveattributevalue"
        body_result = response.json()
        att_value_id = body_result[0]['ID']
        BuiltIn().set_test_variable("${att_value_res_bd}", body_result)
        BuiltIn().set_test_variable("${att_value_id}", att_value_id)
        return att_value_id

    def user_retrieves_all_attribute_value_setup(self):
        """ Function to retrieve all attribute value setup """
        url = "{0}attribute-value-creation".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            if len(body_result) > 1:
                rand_so = secrets.randbelow(len(body_result))
            else:
                rand_so = 0

            BuiltIn().set_test_variable("${attribute_value_setup_id}", body_result[rand_so]["ID"])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves attribute value setup by ${type} id')
    def user_retrieves_attribute_value_setup_by_id(self, type):
        """ Function to retrieve attribute value setup by using id """
        self.user_retrieves_all_attribute_value_setup()
        if type == 'valid' or type == 'delete':
            res_attribute_value_setup_id = BuiltIn().get_variable_value("${attribute_value_setup_id}")
            print("Valid Id: ", res_attribute_value_setup_id)
        else:
            res_attribute_value_setup_id = COMMON_KEY.generate_random_id("0")

        url = "{0}attribute-value-creation/{1}".format(END_POINT_URL, res_attribute_value_setup_id)
        print("URL : ", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        BuiltIn().set_test_variable("${res_body}", response.json())
        print("Res body", response.json())
