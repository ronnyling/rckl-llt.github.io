from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from setup.hanaDB import HanaDB
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from resources.restAPI.MasterDataMgmt.Promo import PromoBuyTypeGet
from resources.restAPI.MasterDataMgmt.Customer import CustomerGet
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure.StructureGet import StructureGet
from resources.restAPI.Config.AppSetup.GamificationGet import GamificationGet
from resources.restAPI.Config.Attribute.AttributeCreation import AttributeCreationGet
from resources.restAPI.Config.Attribute.AttributeValueSetup import AttributeValueSetupGet
from resources.restAPI.SysConfig.Maintenance.LOB import LobGet
from resources.restAPI.SysConfig.Attribute.AttributeAssignTo import AttributeAssignToGet
from resources.restAPI.SysConfig.Attribute.AttributeUsage import AttributeUsageGet
from resources.restAPI.SysConfig.Attribute.AttributeModule import AttributeModuleGet
from resources.restAPI.SysConfig.Attribute.AttributeMapping import AttributeMappingGet

import json
import secrets

PROMO_END_POINT_URL = PROTOCOL + "promotion" + APP_URL


class PromoAssignPost(object):

    @keyword("user assign distributor:${dist} and customer:${cust} to promotion ${cond} posm assignment")
    def assign_promotion(self, dist, cust, posm_assign):
        promo_id = BuiltIn().get_variable_value("${promo_id}")
        GamificationGet().user_retrieves_option_values_geo_level_leaderboard("Sales Office")
        geo_res = StructureGet().user_get_hierarchy_structure_node_details()[0]
        cust_assign_type_id = PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_cust_assign_type("Hierarchy")
        cust_assign_payload = self.cust_assignment_payload(cust_assign_type_id, promo_id, cust)
        dist_assign_payload = self.dist_assignment_payload(promo_id, dist, geo_res)
        if posm_assign == "with":
            other_assign_payload = self.other_assignment_payload(promo_id)
        else:
            other_assign_payload = []
        assign_payload = self.assignment_payload(cust_assign_payload, dist_assign_payload, other_assign_payload,
                                                 promo_id)
        print("Promo assignment==", assign_payload)
        url = "{0}promotion/{1}/assignment".format(PROMO_END_POINT_URL, promo_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, assign_payload)
        print("Response", response)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        HanaDB.HanaDB().connect_database_to_environment()
        promo_id = COMMON_KEY.convert_id_to_string(promo_id)
        HanaDB.HanaDB().check_if_exists_in_database_by_query("SELECT * FROM PROMO_OTHER_ASSIGNMENT WHERE "
                                                             "PROMO_ID = '{0}'".format(promo_id))
        HanaDB.HanaDB().disconnect_from_database()

    def dist_assignment_payload(self, promo_id, dist, geo_res):
        dist_list = []
        dist = dist.split(",")
        for item in dist:
            DistributorGet.DistributorGet().user_gets_distributor_by_using_code(item)
            self.get_geo_details_by_level_desc(BuiltIn().get_variable_value("${dist_name}"), geo_res)
            DISTCAT_ID = BuiltIn().get_variable_value("${DISTCAT_ID}")
            DISTCAT_VALUE_ID = BuiltIn().get_variable_value("${DISTCAT_VALUE_ID}")
            payload = {
                "action": "create",
                "DISTCAT_ID": DISTCAT_ID,
                "DISTCAT_VALUE_ID": DISTCAT_VALUE_ID,
                "ID": None,
                "PROMO_ID": promo_id,
                "VERSION": 0
            }
            details = BuiltIn().get_variable_value("${dist_asgn_details}")
            if details:
                payload.update((k, v) for k, v in details.items())
            dist_list.append(payload)
        return dist_list

    def get_geo_details_by_level_desc(self, level_desc, geo):
        if geo.get("children") is not None:
            self.loop_children(level_desc, geo['children'])

    def loop_children(self, level_desc, geo):
        for item in geo:
            if item.get("children") is not None:
                self.loop_children(level_desc, item['children'])
                result = self.level_node_found(item, level_desc)
                if result:
                    break
            else:
                result = self.level_node_found(item, level_desc)
                if result:
                    break

    def level_node_found(self, a, b):
        if a.get("levelDesc") == b:
            print("found node asd=",a)
            BuiltIn().set_test_variable("${node_res_bd}", a)
            BuiltIn().set_test_variable("${LEVEL_DESC}", a['levelDesc'])
            BuiltIn().set_test_variable("${LEVEL_VAL}", a['title'])
            BuiltIn().set_test_variable("${DISTCAT_ID}", a['treeId'])
            BuiltIn().set_test_variable("${DISTCAT_VALUE_ID}", a['nodeId'])
            BuiltIn().set_test_variable("${PARENT_ID}", a['parentId'])
            return True
        else:
            return False

    def cust_assignment_payload(self, assign_type, promo_id, cust):
        cx_list = []
        cust = cust.split(",")
        for item in cust:
            cust_respond = CustomerGet.CustomerGet().user_retrieves_cust_name(item)
            if cust_respond is not None:
                cust_id = cust_respond['ID']
            else:
                cust_id = ''
            payload = {
                "ID": None,
                "CUST_ASS_TYPE": assign_type,
                "PROMO_ID": promo_id,
                "CUSTCAT_ID": None,
                "CUSTCAT_VALUE_ID": cust_id,
                "VERSION": 1,
                "action": "create"
            }
            cx_list.append(payload)
        return cx_list

    def assignment_payload(self, cust_assign, dist_assign, other_assign, promo_id):
        geo_hier_id = BuiltIn().get_variable_value("${geo_hier_id}")
        payload = {
            "ID": promo_id,
            "CASH_CUST": True,
            "CREDIT_CUST": True,
            "CUST_ASS_ALL": False,
            "DIST_ASS_ALL": False,
            "GEO_HIER_ID": geo_hier_id,
            "CUST_HIER_ID": "5E306ADB:FD4E645E-8C4A-4071-AD96-AF031651EA9C",
            "action": "update",
            "PROMO_DIST_ASSIGNMENT": dist_assign,
            "PROMO_CUST_ASSIGNMENT": cust_assign,
            "PROMO_OTHER_ASSIGNMENT": other_assign,
            "PROMO_DIST_EX": [],
            "PROMO_CUST_EX": [],
            "VERSION": 1
        }
        details = BuiltIn().get_variable_value("${asgn_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        role = BuiltIn().get_variable_value("${role}")
        if role is None:
            role = BuiltIn().get_variable_value("${user_role}")
        if role == 'distadm':
            payload['DIST_ASS_ALL'] = True
            payload['PROMO_DIST_ASSIGNMENT'] = []
        payload = json.dumps(payload)
        return payload

    def other_assignment_payload(self, promo_id):
        oth_list = []
        def_lob_id = LobGet.LobGet().user_retrieves_lob(True)
        usage_id = AttributeUsageGet.AttributeUsageGet().user_retrieves_attribute_usage_using(
            "Filtering and Assignment")
        module_id = AttributeModuleGet.AttributeModuleGet().user_retrieves_attribute_module_by_name("POSM Products")
        posm_assign_to_id = AttributeAssignToGet.AttributeAssignToGet().user_retrieves_attribute_assign_to(
            "POSM Assignment")
        promo_assign_to_id = AttributeAssignToGet.AttributeAssignToGet().user_retrieves_attribute_assign_to(
            "Promotion Assignment")
        AttributeCreationGet.AttributeCreationGet().user_gets_attribute_creation_by(module_id, def_lob_id)
        mapping_status = BuiltIn().get_variable_value("${mapping_status}")
        if mapping_status is None:
            mapping_status = True
        att_creation_respond = BuiltIn().get_variable_value("${att_creation_respond}")
        AttributeMappingGet.AttributeMappingGet().user_retrieves_attribute_mapping_by_module_assigned \
            (mapping_status, module_id, usage_id, posm_assign_to_id)
        mapping_posm = BuiltIn().get_variable_value("${mapping_respond}")
        AttributeMappingGet.AttributeMappingGet().user_retrieves_attribute_mapping_by_module_assigned \
            (mapping_status, module_id, usage_id, promo_assign_to_id)
        mapping_promo = BuiltIn().get_variable_value("${mapping_respond}")
        mapping_list = []
        othcat_list = []
        for i in range(0, len(mapping_posm)):
            for j in range(0, len(mapping_promo)):
                if mapping_posm[i]["ATTRIBUTE"] == mapping_promo[j]["ATTRIBUTE"]:
                    mapping_list.append(mapping_posm[i])
        for i in range(0, len(att_creation_respond)):
            for j in range(0, len(mapping_list)):
                if att_creation_respond[i]["ID"] == mapping_list[j]["ATTRIBUTE"]:
                    othcat_list.append(att_creation_respond[i]["ID"])
        print("othcat_list: ", othcat_list)

        multiple_diff_oth = BuiltIn().get_variable_value("${multiple_diff_oth}")
        othcat_id = othcat_list[0]
        othcat_val_id = AttributeValueSetupGet.AttributeValueSetupGet().user_gets_attribute_value_by(othcat_id)
        payload = self.other_payload(promo_id, othcat_id, othcat_val_id)
        oth_list.append(payload)
        if multiple_diff_oth is not None:
            othcat_id = othcat_list[1]
            othcat_val_id = AttributeValueSetupGet.AttributeValueSetupGet().user_gets_attribute_value_by(othcat_id)
            payload = self.other_payload(promo_id, othcat_id, othcat_val_id)
            oth_list.append(payload)
        return oth_list

    def other_payload(self, promo_id, othcat_id, othcat_val_id):
        payload = {
            "action": "create",
            "OTHCAT_ID": othcat_id,
            "OTHCAT_VALUE_ID": othcat_val_id,
            "MIN_QTY": int(secrets.choice(range(1, 999))),
            "TYPE": "P",
            "ID": None,
            "PROMO_ID": promo_id,
            "VERSION": 0
        }
        details = BuiltIn().get_variable_value("${oth_asgn_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        return payload
