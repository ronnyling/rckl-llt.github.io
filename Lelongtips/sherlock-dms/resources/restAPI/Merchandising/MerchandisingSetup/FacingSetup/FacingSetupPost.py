import secrets, json
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI.Config.AppSetup.AppSetupGet import AppSetupGet
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure.StructureGet import StructureGet
from resources.restAPI.Config.DynamicHierarchy.ProductCustomerHierarchy.ValueGet import ValueGet

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL

class FacingSetupPost(object):
    SETUP_DETAILS="${setup_details}"

    @keyword('user creates product group with ${data_type} data')
    def user_creates_product_group_with(self, data_type):
        url = "{0}merchandising/merc-prod-group".format(END_POINT_URL)
        payload = self.payload_setup()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${res_bd_setup_payload}", body_result)
            BuiltIn().set_test_variable("${res_bd_prod_group_id}", body_result["ID"])
            BuiltIn().set_test_variable("${res_bd_prod_group_brand_cd}", body_result["BRAND_CD"])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_setup(self):
        StructureGet().user_get_hierid_from_hierarchy_structure_name("General Product Hierarchy")
        hier_structure_details = StructureGet().user_get_hierarchy_structure_info_by_hierarchy_id()
        hier_id = hier_structure_details['hierId']
        AppSetupGet().user_retrieves_details_of_application_setup()
        body_res = BuiltIn().get_variable_value("${body_result}")
        tree_id = body_res['MDSE_PROD_HIERARCHY_LEVEL']
        BuiltIn().set_test_variable("${tree_id}", tree_id)
        ValueGet().get_all_values_from_hierarchy_tree()
        node_id = ValueGet().get_value_by_random_data()

        brand_type = secrets.choice(["O", "C"])
        brand_code = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(8))
        brand_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(15))

        payload = {

                "BRAND_TYPE": brand_type,
                "PRDCAT_VALUE_ID": node_id,
                "BRAND_CD": brand_code,
                "BRAND_DESC": brand_desc,
                "PRDCAT_ID": tree_id,
                "PRD_HIER_ID": hier_id

        }
        details = BuiltIn().get_variable_value(self.SETUP_DETAILS)
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Facing Setup Payload: ", payload)
        return payload
