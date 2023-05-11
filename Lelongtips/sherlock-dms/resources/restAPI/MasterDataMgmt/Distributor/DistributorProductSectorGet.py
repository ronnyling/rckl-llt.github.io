""" Python file related to distributor product sector API """
from faker import Faker
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.components import COMMON_KEY

FAKE = Faker()

END_POINT_URL = PROTOCOL + "product-sector" + APP_URL
END_POINT_URL_ALL = PROTOCOL + "metadata" + APP_URL


class DistributorProductSectorGet:
    """ Functions related to distributor product sector GET request """

    def user_retrieves_all_product_sector(self):
        """ Functions to retrieve all product sector """
        url = "{0}module-data/product-sectors".format(END_POINT_URL_ALL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable(COMMON_KEY.BODY_RESULT, body_result)
            body_result = BuiltIn().get_variable_value(COMMON_KEY.BODY_RESULT)
            print("body_result", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @keyword('user retrieves assigned product sector')
    def user_retrieves_assigned_product_sector(self):
        """ Functions to retrieve assigned product sector based on distributor """
        """ Distributor_id is set using user_gets_distributor_by_using_code, please run in prerequisites"""
        dist_id = BuiltIn().get_variable_value("${dist_id}")
        url = "{0}product-sector-assign/distributor/{1}".format(END_POINT_URL, dist_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable(COMMON_KEY.BODY_RESULT, body_result)
            BuiltIn().set_test_variable("${assigned_dist_sector}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @keyword("user retrieves ${selection} product sector id for ${product_sector}")
    def user_retrieves_product_sector_id_for(self, selection, product_sector):
        """ Functions to retrieve product sector id """
        if selection == "assigned":
            self.user_retrieves_assigned_product_sector()
        else:
            self.user_retrieves_all_product_sector()
        body_result = BuiltIn().get_variable_value(COMMON_KEY.BODY_RESULT)
        product_sector_id = None
        for dic in body_result:
            if dic["PROD_SECTOR_DESC"] == str(product_sector):
                product_sector_id = dic["ID"]
                break
        return product_sector_id
