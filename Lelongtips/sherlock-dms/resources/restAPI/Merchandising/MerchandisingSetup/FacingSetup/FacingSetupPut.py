import secrets, json
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI.Config.AppSetup.AppSetupGet import AppSetupGet
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure.StructureGet import StructureGet
from resources.restAPI.Config.DynamicHierarchy.ProductCustomerHierarchy.ValueGet import ValueGet

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL

class FacingSetupPut(object):
    SETUP_DETAILS="${setup_details}"
    SETUP_ID="${res_bd_prod_group_id}"
    @keyword('user updates product group with ${data_type} data')
    def user_updates_product_group_with(self, data_type):
        res_bd_prod_group_id = BuiltIn().get_variable_value("${res_bd_prod_group_id}")
        res_bd_prod_group_brand_cd = BuiltIn().get_variable_value("${res_bd_prod_group_brand_cd}")
        url = "{0}merchandising/merc-prod-group/{1}".format(END_POINT_URL, res_bd_prod_group_id)
        payload = self.payload_setup(res_bd_prod_group_brand_cd)
        details = BuiltIn().get_variable_value(self.SETUP_DETAILS)
        if details:
            payload.update((k, v) for k, v in details.items())
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            print("Result:", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_setup(self,brand_code):
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
        brand_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(15))
        setup_id = BuiltIn().get_variable_value(self.SETUP_ID)

        payload = {
            "ID": setup_id,
             "PRD_HIER_ID": hier_id,
             "PRDCAT_ID": tree_id,
             "BRAND_CD": brand_code,
             "PRDCAT_VALUE_ID": node_id,
             "BRAND_DESC": brand_desc,
             "BRAND_TYPE": brand_type
        }
        details = BuiltIn().get_variable_value(self.SETUP_DETAILS)
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Facing Setup Payload: ", payload)
        return payload
