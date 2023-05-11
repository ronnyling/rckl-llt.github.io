from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json
import secrets
import datetime

from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure.StructureGet import StructureGet

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL
current_date = datetime.datetime.now()


class AuditPost(object):
    AUDIT_ID = "${audit_id}"

    @keyword('user creates audit setup using ${data} data')
    def user_creates_audit_setup(self, data):
        payload = self.payload()
        url = "{0}merchandising/merc-general-info".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            body_result = response.json()
            print("Body Result: ", body_result)
            BuiltIn().set_test_variable(self.AUDIT_ID, body_result["HEADER"]["ID"])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload(self):
        start_dt = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        end_dt = (datetime.datetime.today() + datetime.timedelta(days=30)).strftime("%Y-%m-%d")
        store_id = BuiltIn().get_variable_value("${rand_store_id}")
        StructureGet().user_get_hierid_from_hierarchy_structure_name("General Product Hierarchy")
        StructureGet().user_get_hierarchy_structure_info_by_hierarchy_id()
        response_dict = BuiltIn().get_variable_value("${response_dict}")
        tree_id = next((level['treeId'] for level in response_dict['levels'] if level['name'] == "Brand"), None)
        BuiltIn().set_test_variable("${tree_id}", tree_id)
        StructureGet().user_get_prd_or_or_cust_hierearchy_info()
        tree_view_bd = BuiltIn().get_variable_value("${tree_view_bd}")
        prd_brands_id = []
        for tree in tree_view_bd:
            if len(tree['children']) > 0:
                for child in tree['children']:
                    prd_brands_id.append(child['nodeId'])
        rand_prd_brand = secrets.choice(prd_brands_id)
        rand_prd_id = rand_prd_brand
        payload = {
          "AUDIT_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
          "START_DATE": start_dt,
          "END_DATE": end_dt,
          "STORE_SPACE": [
            {
              "ID": store_id
            }
          ],
          "CATEGORY": [
            {
              "ATTRIBUTE_ID": rand_prd_id
            }
          ]
        }
        details = BuiltIn().get_variable_value("${audit_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload["START_DATE"] = start_dt
        payload = json.dumps(payload)
        print("Audit Setup Payload :", payload)
        return payload

    @keyword('user assigns audit setup with facing audit')
    def user_assigns_facing_audit(self, data):
        payload = self.facing_payload()
        url = "{0}merchandising/merc-general-info".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            body_result = response.json()
            print("Body Result: ", body_result)
            BuiltIn().set_test_variable(self.AUDIT_ID, body_result["HEADER"]["ID"])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def facing_payload(self):
        brand_id = BuiltIn().get_variable_value("${brand_id}")
        audit_id = BuiltIn().get_variable_value(self.AUDIT_ID)
        payload = [
          {
            "AUDIT_ID": audit_id,
            "TRANSACTION_ID": "A68BC6B9:94254624-C722-409F-84A9-13A192D40A7B",
            "FACING_ID": brand_id,
            "STATUS": True
          }
        ]

        payload = json.dumps(payload)
        print("Audit Payload :", payload)
        return payload
