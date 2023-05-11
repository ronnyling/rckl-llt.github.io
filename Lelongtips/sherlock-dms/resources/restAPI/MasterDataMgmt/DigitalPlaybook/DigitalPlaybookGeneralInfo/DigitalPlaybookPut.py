import secrets
import datetime

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Config.ReferenceData.PlaybookType.PlaybookTypeGet import PlaybookTypeGet
from resources.restAPI.MasterDataMgmt.DigitalPlaybook.DigitalPlaybookGeneralInfo.DigitalPlaybookPost import DigitalPlaybookPost
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure.StructureGet import StructureGet
from resources.restAPI.Config.DynamicHierarchy.ProductCustomerHierarchy.ValueGet import ValueGet
from resources.restAPI.Config.AppSetup.AppSetupGet import AppSetupGet
from setup.hanaDB import HanaDB

current_date = datetime.datetime.now()
END_POINT_URL = PROTOCOL + "message" + APP_URL
start_date = str((current_date + datetime.timedelta(days=2)).strftime("%Y-%m-%d"))
end_date = str((current_date + datetime.timedelta(days=45)).strftime("%Y-%m-%d"))
image_file_type = [
    "jpeg",
    "jpg",
    "png",
]
max_thumbnail_size = 500

class DigitalPlaybookPut(object):
    """ Functions to update playbook """

    @keyword('user updates playbook with ${type} data')
    def user_updates_playbook_with(self, type):
        """ Function to updates playbook with random/fixed data"""
        playbook_id = BuiltIn().get_variable_value("${playbook_id}")
        url = "{0}playbk-setup/{1}".format(END_POINT_URL, playbook_id)
        general_payload = self.get_general_payload(type, playbook_id)
        content_assignment = []
        content_payload = DigitalPlaybookPost().get_content_payload()
        content_assignment.append(content_payload)
        payload = DigitalPlaybookPost().payload_playbook(type, general_payload, content_assignment)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            # HanaDB.HanaDB().connect_database_to_environment()
            # HanaDB.HanaDB().user_validates_database_data("playbk-setup", body_result['GENERAL_INFO'])
            # HanaDB.HanaDB().disconnect_from_database()
            BuiltIn().set_test_variable("${res_bd_playbook_payload}", body_result)
            res_bd_playbook_desc = body_result['GENERAL_INFO']['PLAYBK_DESC']
            BuiltIn().set_test_variable("${res_bd_playbook_desc}", res_bd_playbook_desc)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def get_general_payload(self, type, playbook_id):
        StructureGet().user_get_hierid_from_hierarchy_structure_name("General Product Hierarchy")
        hier_structure_details = StructureGet().user_get_hierarchy_structure_info_by_hierarchy_id()
        hier_id = hier_structure_details['hierId']
        AppSetupGet().user_retrieves_details_of_application_setup()
        body_res = BuiltIn().get_variable_value("${body_result}")
        tree_id = body_res['PLAYBK_PROD_HIERARCHY_LEVEL']
        BuiltIn().set_test_variable("${tree_id}", tree_id)
        ValueGet().get_all_values_from_hierarchy_tree()
        node_id = ValueGet().get_value_by_random_data()

        general_payload = DigitalPlaybookPost().set_general_payload(hier_id, tree_id, node_id)
        general_payload['ID'] = playbook_id
        if type == 'existing':
            general_payload['PLAYBK_DESC'] = BuiltIn().get_variable_value("${playbook_desc}")
        general_details = BuiltIn().get_variable_value("${playbook_general_details}")
        if general_details:
            if 'PLAYBOOK_TYPE_CODE' in general_details.keys():
                general_payload['PLAYBK_TYPE_ID'] = PlaybookTypeGet().user_gets_playbook_type_by_using_field("PLAYBOOK_TYPE_CD", general_details['PLAYBOOK_TYPE_CODE'])
            if 'PRODUCT_HIERARCHY_DESCRIPTION' in general_details.keys():
                StructureGet().user_get_hierid_from_hierarchy_structure_name(general_details['PRODUCT_HIERARCHY_DESCRIPTION'])
                hier_structure_details = StructureGet().user_get_hierarchy_structure_info_by_hierarchy_id()
                hier_id = hier_structure_details['hierId']
                AppSetupGet().user_retrieves_details_of_application_setup()
                body_res = BuiltIn().get_variable_value("${body_result}")
                tree_id = body_res['PLAYBK_PROD_HIERARCHY_LEVEL']
                BuiltIn().set_test_variable("${tree_id}", tree_id)
                ValueGet().get_all_values_from_hierarchy_tree()
                node_id = ValueGet().get_value_by_random_data()
                general_payload['PRD_HIER_ID'] = hier_id
                general_payload['PRDCAT_ID'] = tree_id
                general_payload['PRDCAT_VALUE_ID'] = node_id
            general_payload.update((k, v) for k, v in general_details.items())
        return general_payload

