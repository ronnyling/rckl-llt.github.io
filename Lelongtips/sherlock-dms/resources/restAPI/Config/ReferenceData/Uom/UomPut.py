from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Config.ReferenceData.Uom import UomPost

END_POINT_URL = PROTOCOL + "product" + APP_URL


class UomPut(object):
    """ Functions to create uom """

    @keyword('user edits uom with ${data_type}')
    def user_edits_uom_with(self, data_type):
        """ Function to create uom with random/given data """
        res_bd_uom_id = BuiltIn().get_variable_value("${res_bd_uom_id}")
        url = "{0}uom-setting/{1}".format(END_POINT_URL, res_bd_uom_id)
        payload = UomPost.UomPost().payload_uom("update")
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            print("Result:", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
