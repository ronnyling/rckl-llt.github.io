import secrets
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

END_POINT_URL = PROTOCOL + "dynamic-attribute" + APP_URL


class AttributeCreationGet(object):
    ATTRIBUTE_CREATION = '${attribute_creation_id}'
    ACTIVE_ATTRIBUTE = '${active_attribute_id}'
    BODY_RESULT = "${body_result}"

    @staticmethod
    def user_gets_attribute_creation_by(module, lob):
        filter_data = {"MODULE": {"$eq": module}, "LOB": {"$eq": lob}}
        filter_data = json.dumps(filter_data)
        url = "{0}dynamic-attribute?filter={1}".format(END_POINT_URL, filter_data)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve attribute creation data"
        body_result = response.json()
        BuiltIn().set_test_variable("${att_creation_respond}", body_result)

        return body_result

    def user_retrieves_all_attribute_creation(self, first_row=False):
        """ Function to retrieve all attribute creation """
        url = "{0}dynamic-attribute".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            respond_len = len(response.json())
            for i in range(respond_len):
                BuiltIn().set_test_variable(self.ATTRIBUTE_CREATION, response.json()[i]['ID'])
                self.user_retrieves_active_attribute()
                active_attr_res = BuiltIn().get_variable_value(self.BODY_RESULT)
                try:
                    active_attr_res[0]['ID']
                    print("OK attr")
                except IndexError:
                    print("invalid attr")
                else:
                    BuiltIn().set_test_variable("${active_attribute_id}", active_attr_res[0]['ID'])
                    break
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves attribute creation by ${type} id')
    def user_retrieves_attribute_creation_by_id(self, type):
        """ Function to retrieve attribute creation by using id """
        self.user_retrieves_all_attribute_creation()
        if type == 'valid' or type == 'delete':
            res_attribute_creation_id = BuiltIn().get_variable_value(self.ATTRIBUTE_CREATION)
            print("Valid Id: ", res_attribute_creation_id)
        else:
            res_attribute_creation_id = COMMON_KEY.generate_random_id("0")

        url = "{0}dynamic-attribute/{1}".format(END_POINT_URL, res_attribute_creation_id)
        print("URL : ", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        BuiltIn().set_test_variable("${res_body}", response.json())
        print("Res body", response.json())

    @keyword('user retrieves active attribute')
    def user_retrieves_active_attribute(self):
        res_attribute_creation_id = BuiltIn().get_variable_value(self.ATTRIBUTE_CREATION)
        url = "{0}getAttributeValueByAttribute/attribute/{1}".format(END_POINT_URL, res_attribute_creation_id)
        print("URL : ", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        BuiltIn().set_test_variable("${body_result}", response.json())

    def user_retrieves_customer_attributes(self):
        url = '{0}attribute-assignment/CUST/FILT_ASSIGN/CUST_ASSIGN'.format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

