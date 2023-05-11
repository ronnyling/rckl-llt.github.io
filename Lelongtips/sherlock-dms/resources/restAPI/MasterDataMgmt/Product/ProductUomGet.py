import secrets

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
import json

PRD_END_POINT_URL = PROTOCOL + "product" + APP_URL
PRD_END_POINT_URL_META = PROTOCOL + "metadata" + APP_URL


class ProductUomGet(object):
    """ Functions to retrieve product uom record """

    def user_retrieves_prd_uom_by_code(self, prd_id, prd_uom):
        filter_prd_uom = {"UOM_CD": {"$eq": prd_uom}}
        filter_prd_uom = json.dumps(filter_prd_uom)
        str(filter_prd_uom).encode(encoding='UTF-8', errors='strict')
        url = "{0}module-data/product/{1}/product-uom?filter={2}".format(PRD_END_POINT_URL_META, prd_id, filter_prd_uom)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve prd uom"
        body_result = response.json()
        return body_result[0]

    def user_retrieves_previous_prd_uom(self):
        body_result = None
        prd_id = BuiltIn().get_variable_value("${prd_id}")

        extension = "filter={%22FIELDS%22:[%22ID%22,%22MODIFIED_DATE%22,%22UOM_CD%22,%22CONV_FACTOR_SML%22,%22BASEUOM_ID.UOM_CD%22,%22UOM_ID.UOM_CD%22,%22UOM_DESCRIPTION%22,%22BASEUOM_DESCRIPTION%22,%22SALE_UOM%22,%22SML_UOM%22,%22DEFAULT_UOM%22,%22CONV_FACTOR%22,%22DIMENSION_UNIT.DIMENSION_DESC%22,%22DIMENSION_UNIT.DIMENSION_CD%22,%22PACK_LENGTH%22,%22PACK_WIDTH%22,%22PACK_HEIGHT%22,%22WEIGHT_UNIT.WEIGHT_DESC%22,%22WEIGHT_UNIT.WEIGHT_CD%22,%22NET_WEIGHT%22,%22GROSS_WEIGHT%22,%22EAN_NO%22,%22PROD_ID.PRD_CD%22,%22UOM_LEVEL%22,%22IS_PALLET%22,%22IS_LAYER%22],%22FILTER%22:[]}&silent=null"
        url = "{0}product/{1}/product-uom?{2}".format(PRD_END_POINT_URL, prd_id, extension)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200 or response.status_code == 204, "Unable to retrieve prd-uom"
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${prd_uom_ls}", body_result)
        BuiltIn().set_test_variable("${sts_code}", response.status_code)
        return body_result

    @keyword('user retrieves all product uom')
    def user_retrieves_all_prd_uom(self):
        prd_id = BuiltIn().get_variable_value("${prd_id}")
        url = "{0}product/{1}/product-uom".format(PRD_END_POINT_URL, prd_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "No product uom retrieved"
        body_result = response.json()
        return body_result

    def user_retrieves_prd_uom_by_id(self, prd, uom_id):
        url = "{0}product/{1}/product-uom/{2}".format(PRD_END_POINT_URL, prd, uom_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve prd-uom"
        body_result = response.json()
        return body_result

    def user_retrieves_uom_details_of_product(self):
        prd_id = BuiltIn().get_variable_value("${prd_id}")
        prd_uom_ls = BuiltIn().get_variable_value("${prd_uom_ls}")
        uom = secrets.choice(prd_uom_ls)

        url = "{0}product/{1}/product-uom/{2}".format(PRD_END_POINT_URL, prd_id, uom['ID'])
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve prd-uom"
        body_result = response.json()
        return body_result

    def user_retrieves_prd_uom(self, prd):
        url = "{0}product/{1}/product-uom".format(PRD_END_POINT_URL, prd)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve prd-uom"
        body_result = response.json()
        return body_result
