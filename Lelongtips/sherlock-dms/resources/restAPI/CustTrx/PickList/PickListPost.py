import datetime
import json

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.MasterDataMgmt.Warehouse import WarehouseGet
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route import RouteGet
from resources.restAPI.MasterDataMgmt.Van import VanGet


END_POINT_URL = PROTOCOL + "picklist" + APP_URL


class PickListPost(object):

    @keyword("user creates picklist with fixed data")
    def user_creates_picklist(self):
        """ Function to create picklist with given data"""
        picklist_details = BuiltIn().get_variable_value("${pl_details}")
        status = picklist_details['STATUS']
        url = "{0}picklist-details".format(END_POINT_URL)
        payload = self.payload_picklist("creates")
        print('Returned Picklist Payload is : ', payload)
        response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
        print("POST Status code for picklist is " + str(response.status_code))
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if status == "Open":
            if response.status_code != 201:
                return str(response.status_code), ""
            else:
                body_result = response.json()
                print("Body Result:", body_result)
                res_bd_picklist_id = body_result['ID']
                BuiltIn().set_test_variable("${res_bd_picklist_id}", res_bd_picklist_id)
                BuiltIn().set_test_variable("${status_code}", response.status_code)
        else:
            if response.status_code != 201:
                return str(response.status_code), ""
            else:
                res_bd_picklist_id = BuiltIn().get_variable_value("${res_bd_picklist_id}")
                body_result = response.json()
                print("Body Result:", body_result)
                print("Picklist ID:", res_bd_picklist_id)
                BuiltIn().set_test_variable("${res_bd_picklist_id}", res_bd_picklist_id)
                BuiltIn().set_test_variable("${status_code}", response.status_code)


    def payload_picklist(self, action):
        """Function to create/confirm picklist payload based on the action"""
        current_date = datetime.datetime.today().strftime('%Y-%m-%d')
        picklist_details = BuiltIn().get_variable_value("${pl_details}")
        pl_id = BuiltIn().get_variable_value("${res_bd_picklist_id}")

        warehouse = picklist_details['WH_CD']
        route = picklist_details['DELIVERY_ROUTE_CD']
        van = picklist_details['VAN_CD']
        pick_doc_type = picklist_details['PICK_DOC_TYPE']
        principal = picklist_details['PRIME_FLAG']
        status = picklist_details['STATUS']
        invoice_id = picklist_details['INV_ID']

        if pick_doc_type == "Invoice":
            pick_doc_type = "I"
        else:
            pick_doc_type = "O"

        if "DOCUMENT_TYPE" in picklist_details:
            doc_type = picklist_details['DOCUMENT_TYPE']
            if doc_type == "Sampling":
                doc_type = "P"
            else:
                doc_type = "S"
        else:
            doc_type = "S"

        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        route_id = RouteGet.RouteGet().user_gets_route_by_using_code(route)
        wh_id = WarehouseGet.WarehouseGet().user_retrieves_warehouse_by_using_code(warehouse)
        van_id = VanGet.VanGet().user_gets_van_id_by_using_code(dist_id, van)

        payload = {
                "WHS_ID": wh_id,
                "DELIVERY_DT_FROM": current_date,
                "DELIVERY_DT_TO": current_date,
                "ACTUAL_DELIVERY_DT": current_date,
                "DELIVERY_PERSON_ID": route_id,
                "VEHICLE_ID": van_id,
                "PICKLIST_TYPE": pick_doc_type,
                "STATUS": status,
                "INVOICE_LIST": [
                    {
                        "INV_ID": invoice_id
                    }
                ],
                "PICKLIST_DOCTYPE": doc_type,
                "PRIME_FLAG": principal,
                "TXN_DT": current_date
        }
        if action == 'confirm':
            payload.update({"STATUS": "Confirmed"})
            payload.update({"PICKLIST_ID": pl_id})

        payload = json.dumps(payload)
        print("Picklist Payload :", payload)
        return payload