from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json
END_POINT_URL = PROTOCOL + "product" + APP_URL
METADATA_END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class UomGet(object):
    """ Functions for retrieving Uom """

    def user_gets_all_uom_data(self):
        """ Function to retrieve all uom record """
        url = "{0}uom-setting".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of uom retrieved are ", len(body_result))
            BuiltIn().set_test_variable("${uom_br}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_gets_uom_by_using_id(self):
        """ Function to retrieve uom by using id """
        res_bd_uom_id = BuiltIn().get_variable_value("${res_bd_uom_id}")
        url = "{0}uom-setting/{1}".format(END_POINT_URL, res_bd_uom_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            assert res_bd_id == res_bd_uom_id, "ID retrieved not matched"
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieves_uom_by_code(self, filter_uom):
        filter_prd_uom = {"UOM_CD": {"$eq": filter_uom}}
        filter_prd_uom = json.dumps(filter_prd_uom)
        str(filter_prd_uom).encode(encoding='UTF-8', errors='strict')
        url = "{0}uom-setting?filter={1}".format(END_POINT_URL, filter_prd_uom)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve prd uom"
        body_result = response.json()
        return body_result[0]

    def user_retrieves_uom_by_code_in_uom_listing(self, filter_uom):
        url = "{0}uom-setting".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        body_result = response.json()

        uom_listing = json.dumps(body_result)
        uom_listing_converted = json.loads(uom_listing)

        filter_prd_uom = [x for x in uom_listing_converted if x['UOM_CD'] == filter_uom]

        print("UOM details", filter_prd_uom)
        return filter_prd_uom[0]
