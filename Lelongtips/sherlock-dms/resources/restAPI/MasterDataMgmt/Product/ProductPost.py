import secrets
from resources.restAPI import PROTOCOL, APP_URL
import json
from resources.restAPI.Common import APIMethod, TokenAccess
from resources.restAPI.Config.TaxMgmt.TaxGroup import TaxGroupGet
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure.StructureGet import StructureGet
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
END_POINT_URL = PROTOCOL + "product" + APP_URL


class ProductPost:

    @keyword('user creates product with ${data_type} data using ${user}')
    def user_creates_product(self, data_type,  user):
        url = "{0}product/".format(END_POINT_URL)
        payload = self.payload_product_master_info(user)
        payload = json.dumps(payload)
        print(payload)
        response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
        print("POST Status code for product master info is " + str(response.status_code))
        if response.status_code != 201:
            print(response.text)
            return str(response.status_code), ""
        else:
            body_result = response.json()
            BuiltIn().set_test_variable("${prd_id}", body_result["ID"])
            BuiltIn().set_test_variable("${prd_cd}", body_result["PRD_CD"])
            print("PRODUCT ID IS", BuiltIn().get_variable_value("${prd_id}"))
            print("PRODUCT CODE IS", BuiltIn().get_variable_value("${prd_cd}"))
            BuiltIn().set_test_variable("${status_code}", response.status_code)
            return str(response.status_code)

    def payload_product_master_info(self, user):
        details = BuiltIn().get_variable_value("${product_details}")
        update_details = BuiltIn().get_variable_value("${update_product_details}")
        sell = 1
        if update_details is not None and update_details['PRD_CD'] is not None:
            prd_cd = update_details['PRD_CD']
        else:
            prd_cd = "".join(secrets.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(10))
        principal = secrets.choice(["PRIME", "NON_PRIME"])
        if principal == "PRIME":
            tax_group = BuiltIn().get_variable_value("${tax_group_id}")
            sell = "0"
        else:
            tax_group = BuiltIn().get_variable_value("${np_tax_group_id}")
            sell = secrets.choice(["0", "1"])
        if tax_group is not None:
            prd_tx = "1"
            tx_gp = {"ID": tax_group}
        else:
            prd_tx = "0"
            tx_gp = None
        if update_details is not None:
            sell = "1"

        StructureGet().user_get_hierid_from_hierarchy_structure_name("General Product Hierarchy")
        hier_structure_details = StructureGet().user_get_hierarchy_structure_info_by_hierarchy_id()
        hier_id = hier_structure_details['hierId']
        BuiltIn().set_test_variable("${hier_id}", hier_id)
        StructureGet().user_retrieves_hierarchy_structure("valid")
        body_res = BuiltIn().get_variable_value("${hier_rs_bd}")
        prd_hier = body_res["levels"]
        node_id_list = []
        parent_id = None
        for x in range((len(prd_hier) - 1), -1, -1):
            tree_id = prd_hier[x]["treeId"]
            BuiltIn().set_test_variable("${tree_id}", tree_id)
            tree_list = StructureGet().user_get_prd_or_or_cust_hierearchy_info()
            if parent_id is None:
                rand = secrets.choice(tree_list)
                while not rand["children"]:
                    rand = secrets.choice(tree_list)
                node_id = rand["children"][0]["nodeId"]
                node_id_list.append(node_id)
                parent_id = rand["nodeId"]
            else:
                for i in tree_list:
                    if i["children"] is not None:
                        for j in i["children"]:
                            if j["nodeId"] == parent_id:
                                node_id = j["nodeId"]
                                node_id_list.append(node_id)
                                parent_id = i["nodeId"]

        payload = {
            'PRD_CD': prd_cd,
            'PRD_DESC': "".join(secrets.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(10)),
            'PRD_DESC1': "".join(secrets.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(10)),
            "PRD_DESC2": "".join(secrets.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(10)),
            'STATUS': secrets.choice(['Active', 'Inactive', 'Block']),
            'PRD_TYPE': "O",
            'SELLING_IND': sell,
            'PRIORITY': secrets.choice(['Active', 'Inactive', 'Block']),
            'MOST_RECENT_ACTIVE': secrets.choice(['1', '0']),
            'PRD_TAX': prd_tx,
            "HSN": None,
            'PRD_TAX_GRP': tx_gp,
            'SHELF_LIFE': "".join(secrets.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(10)),
            'PROMO_IND': "1",
            'PARENT_PRD': None,
            'PARENT_PRD_DESC': "".join(secrets.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(10)),
            'RTN_TYPE': secrets.choice(['1', '2']),
            'CHECK_LICENSE': secrets.choice(['1', '0']),
            'PRIME_FLAG': principal,
            'HIERARCHY': None,
            'HIERARCHY_LEVEL_1':node_id_list[3],
            'HIERARCHY_LEVEL_2':node_id_list[2],
            'HIERARCHY_LEVEL_3':node_id_list[1],
            'HIERARCHY_LEVEL_4':node_id_list[0],
            'STOCK_CONTROL': '0'
        }
        if details:
            payload.update((k, v) for k, v in details.items())
        if update_details:
            payload.update((k, v) for k, v in update_details.items())
        if payload["PRD_TAX"] == "0":
            payload["PRD_TAX_GRP"] = None
        if user == "distadm" and payload["PRIME_FLAG"] == "PRIME":
            payload["SELLING_IND"] = "0"
        if update_details is not None and "SELLING_IND" in update_details.keys():
            print("payload is " + json.dumps(update_details))
            payload["SELLING_IND"] = update_details["SELLING_IND"]
        return payload

    @keyword('user creates ${data_type} product as prerequisite')
    def user_creates_product_as_prerequisite(self, data_type):
        user = BuiltIn().get_variable_value("${user_role}")
        if user == "distadm":
            TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
            TaxGroupGet.TaxGroupGet().user_get_random_tax_group_by_principal_flag("NON_PRIME")
        else:
            TokenAccess.TokenAccess().user_retrieves_token_access_as("hqadm")
            TaxGroupGet.TaxGroupGet().user_get_random_tax_group_by_principal_flag("PRIME")
        self.user_creates_product(data_type, user)
