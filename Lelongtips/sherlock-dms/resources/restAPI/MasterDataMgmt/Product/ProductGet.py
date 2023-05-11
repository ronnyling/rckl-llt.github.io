import secrets
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

from resources.restAPI.MasterDataMgmt.Product.ProductUomGet import ProductUomGet
PRD_END_POINT_URL = PROTOCOL + "metadata" + APP_URL
PRODUCT_END_POINT_URL = PROTOCOL + "product" + APP_URL


class ProductGet(object):

    def user_retrieves_all_products(self):
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributors/{1}/product/".format(PRODUCT_END_POINT_URL, dist_id)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response.status_code

    def user_retrieves_product_by_id(self):
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        prod_id = BuiltIn().get_variable_value("${prd_id}")
        url = "{0}distributors/{1}/product/{2}".format(PRODUCT_END_POINT_URL, dist_id, prod_id)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        BuiltIn().set_test_variable("${prd_res}", response.json())
        return response.status_code

    def user_retrieves_prd_by(self, filter_type, data):
        filter_prd = ""
        if filter_type == "code":
            filter_prd = {"PRD_CD": {"$eq": data}}
        elif filter_type == "id":
            filter_prd = {"ID": {"$eq": data}}
        elif filter_type == "status":
            filter_prd = {"STATUS": {"$eq": data}}
        filter_prd = json.dumps(filter_prd)
        str(filter_prd).encode(encoding='UTF-8', errors='strict')
        url = "{0}module-data/product?filter={1}".format(PRD_END_POINT_URL, filter_prd)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve prd"
        body_result = response.json()
        prd_id = body_result[0]['ID']
        prd_cd = body_result[0]['PRD_CD']
        BuiltIn().set_test_variable("${prd_id}", prd_id)
        BuiltIn().set_test_variable("${prd_cd}", prd_cd)
        print("PRD ID IS {0}".format(prd_id))
        return body_result[0]

    @keyword("user retrieves prd by prd code '${prd}'")
    def user_retrieves_prd_by_prd_code(self, prd):
        return self.user_retrieves_prd_by("code", prd)

    def user_retrieves_prd_cd_by_prd_id(self, ids):
        return self.user_retrieves_prd_by("id", ids)

    @keyword("user retrieves prd by prd status '${status}'")
    def user_retrieves_prd_by_prd_status(self, status):
        return self.user_retrieves_prd_by("status", status)

    def user_retrieves_all_product_list(self):
        hdr_filter = "?filter={%22FIELDS%22:[%22ID%22,%22MODIFIED_DATE%22,%22PRD_TAX%22,%22SELLING_IND%22,%22DIST_ID%22,%22PRD_TYPE%22,%22PRD_CD%22,%22PRD_DESC%22,%22STATUS%22,%22PRIME_FLAG%22,%22PRD_TAX_GRP.TAX_GRP_CD%22,%22PRD_TAX_GRP_DISPLAY%22],%22FILTER%22:[]}"
        url = "{0}product{1}".format(PRODUCT_END_POINT_URL, hdr_filter)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        BuiltIn().set_test_variable("${all_prd}", response.json())
        return response.status_code

    def user_retrieves_random_product_details(self):
        self.user_retrieves_all_product_list()
        all_prd = BuiltIn().get_variable_value("${all_prd}")

        all_prd_non_prime = (
            prd for prd in all_prd
            if prd['PRIME_FLAG'] == "NON_PRIME"
        )
        prd_with_uom_id = None
        while prd_with_uom_id is None:
            rand_prd_non_prime = next(all_prd_non_prime, None)
            BuiltIn().set_test_variable("${prd_id}", rand_prd_non_prime['ID'])
            ProductUomGet().user_retrieves_previous_prd_uom()
            if BuiltIn().get_variable_value("${sts_code}") == 200:
                prd_with_uom_id = rand_prd_non_prime['ID']
        BuiltIn().set_test_variable("${prd_id}", prd_with_uom_id)

        url = "{0}product/{1}".format(PRODUCT_END_POINT_URL, prd_with_uom_id)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return response.status_code
