from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI.Config.ReferenceData.Uom.UomGet import UomGet
from resources.restAPI.Config.ReferenceData.DimensionUnit.DimensionUnitGet import DimensionUnitGet
from resources.restAPI.Config.ReferenceData.WeightUnit.WeightUnitGet import WeightUnitGet
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json
import secrets

END_POINT_URL = PROTOCOL + "product" + APP_URL


class ProductUomPost(object):
    """ Functions to create product uom """

    @keyword('user creates product uom with ${data_type} data')
    def user_creates_prd_uom(self, data_type):
        prd_id = BuiltIn().get_variable_value("${prd_id}")
        url = "{0}product/{1}/product-uom".format(END_POINT_URL, prd_id)
        payload = self.payload("creates")
        payload = json.dumps(payload)
        print("payload = ", payload)
        response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${prd_uom_id}", body_result["ID"])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload(self, action):
        uom = BuiltIn().get_variable_value("${uom}")
        weight_unit = BuiltIn().get_variable_value("${weight_unit}")
        dim_unit = BuiltIn().get_variable_value("${dim_unit}")

        if uom is None:
            UomGet().user_gets_all_uom_data()
            uom_list = BuiltIn().get_variable_value("${uom_br}")
            rand_uom_no = secrets.choice(uom_list)
            uom = rand_uom_no
        if dim_unit is None:
            DimensionUnitGet().get_all_dimension_unit()
            dim_unit_list = BuiltIn().get_variable_value("${dim_unt_br}")
            rand_dim_no = secrets.choice(dim_unit_list)
            dim_unit = rand_dim_no
        if weight_unit is None:
            WeightUnitGet().get_all_weight_unit()
            weight_unit_list = BuiltIn().get_variable_value("${weight_unt_br}")
            rand_weight_no = secrets.choice(weight_unit_list)
            weight_unit = rand_weight_no

        payload = {
            "SALE_UOM": True,
            "SML_UOM": True,
            "DEFAULT_UOM": False,
            "CONV_FACTOR": 1,
            "IS_PALLET": False,
            "IS_LAYER": False,
            "UOM_ID": {
                "ID": uom['ID'],
                "DIST_ID": uom['DIST_ID'],
                "UOM_CD": uom['UOM_CD'],
                "UOM_DESCRIPTION": uom['UOM_DESCRIPTION'],
                "PRIME_FLAG": uom['PRIME_FLAG']
            },
            "PACK_LENGTH": secrets.choice(range(1, 10)),
            "PACK_WIDTH": secrets.choice(range(1, 10)),
            "PACK_HEIGHT": secrets.choice(range(1, 10)),
            "WEIGHT_UNIT": {
                "ID": weight_unit['ID'],
                "WEIGHT_CD": weight_unit['WEIGHT_CD'],
                "WEIGHT_DESC": weight_unit['WEIGHT_DESC'],
                "CONV_FACTOR_KG": weight_unit['CONV_FACTOR_KG'],
                "_DESC": "{0} - {1}".format(weight_unit['WEIGHT_DESC'], weight_unit['WEIGHT_CD'])
            },
            "NET_WEIGHT": secrets.choice(range(1, 10)),
            "GROSS_WEIGHT": secrets.choice(range(1, 10)),
            "DIMENSION_UNIT": {
                "ID": dim_unit['ID'],
                "DIMENSION_CD": dim_unit['DIMENSION_CD'],
                "DIMENSION_DESC": dim_unit['DIMENSION_DESC'],
                "CONV_FACTOR_M": dim_unit['CONV_FACTOR_M'],
                "_DESC": "{0} - {1}".format(dim_unit['DIMENSION_DESC'], dim_unit['DIMENSION_CD'])
            }
        }
        if action == "updates":
            payload['UOM_CD'] = uom['UOM_CD']
            payload['UOM_DESCRIPTION'] = uom['UOM_DESCRIPTION']
            payload['UOM_LEVEL'] = 1
            payload['CONV_FACTOR_SML'] = 1

        BuiltIn().set_test_variable("${uom}", payload['UOM_ID'])
        BuiltIn().set_test_variable("${weight_unit}", payload['WEIGHT_UNIT'])
        BuiltIn().set_test_variable("${dim_unit}", payload['DIMENSION_UNIT'])
        return payload

