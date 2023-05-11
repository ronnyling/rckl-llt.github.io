import secrets
from resources.restAPI import PROTOCOL, APP_URL
import json
from resources.restAPI.SysConfig.LineOfBusiness.LineOfBusinessGet import LineOfBusinessGet
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure import StructureGet
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
END_POINT_URL = PROTOCOL + "product-sector" + APP_URL


class ProductSectorPost:

    @keyword('user creates product sector with ${data_type} data')
    def user_creates_product_sector(self, cond):
        url = "{0}product-sector/".format(END_POINT_URL)
        payload = self.product_sector_general_payload()
        print("payload", payload)
        response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${product_sector_id}", body_result['createdSector']['ID'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def product_sector_hierarchy_payload(self):
        StructureGet.StructureGet().user_get_hierid_from_hierarchy_structure_name("General Product Hierarchy")
        StructureGet.StructureGet().user_get_hierarchy_structure_info_by_hierarchy_id()
        ps_hier_details = BuiltIn().get_variable_value("${product_sector_hierarchy_details}")
        if ps_hier_details:
            level_id = StructureGet.StructureGet().get_levels_from_structure(ps_hier_details.get("LevelName"), "name")
        else:
            level_id = StructureGet.StructureGet().get_levels_from_structure("random", "name")
        payload = {
            "PRODUCT_HIER_ID": level_id,
            "LEVEL_VALUE_ID": "ALL"
        }
        return payload

    def product_sector_general_payload(self):
        lob = LineOfBusinessGet().get_lob_by_field_and_value("DEFAULT_IND", "true")
        user = BuiltIn().get_variable_value("${user_role}")

        if user == "hqadm":
            principal = "PRIME"
        else:
            principal = "NON_PRIME"
        status = secrets.choice([True, False])
        hierarchy = []
        if status is True:
            hierarchy.append(self.product_sector_hierarchy_payload())
        payload = {
            "PROD_SECTOR_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(15)),
            "LOB_REF": lob['ID'],
            "IS_SUPER_SET": True,
            "SUPER_SET_SECTOR": "None",
            "STATUS": status,
            "PRIME_FLAG": principal,
            "IS_POSM": False,
            "tableValues":  hierarchy

        }
        product_sector_details = BuiltIn().get_variable_value("${product_sector_details}")
        if product_sector_details:
            payload.update((k, v) for k, v in product_sector_details.items())
        BuiltIn().set_test_variable("${product_sector_payload}", payload)
        payload = json.dumps(payload)
        return payload
