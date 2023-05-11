import datetime
import json

from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.MasterDataMgmt.Warehouse import WarehouseGet

END_POINT_URL = PROTOCOL + "picklist" + APP_URL


class PickListPut(object):
    """ Functions to retrieve picklist """

    @keyword('user updates picklist with ${type} data')
    def user_updates_picklist(self, type):
        res_bd_picklist_id = BuiltIn().get_variable_value("${res_bd_picklist_id}")
        url = "{0}picklist-details/{1}".format(END_POINT_URL, res_bd_picklist_id)
        payload = self.updated_payload(type)
        print('Updated Picklist Payload is : ', payload)
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, payload)
        print("PUT Status code for picklist is " + str(response.status_code))
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code != 200:
            return str(response.status_code), ""
        else:
            body_result = response.json()
            print("Body Result:", body_result)
            print("Picklist ID:", res_bd_picklist_id)
            BuiltIn().set_test_variable("${res_bd_picklist_id}", res_bd_picklist_id)
            BuiltIn().set_test_variable("${status_code}", response.status_code)

    def updated_payload(self, type):
        """Function to update existing picklist with new actual delivery date"""
        picklist_details = BuiltIn().get_variable_value("${pl_details}")
        warehouse = picklist_details['WH_CD']
        doc_type = picklist_details['DOCUMENT_TYPE']
        invoice_id = picklist_details['INV_ID']
        pick_doc_type = picklist_details['PICK_DOC_TYPE']
        wh_id = WarehouseGet.WarehouseGet().user_retrieves_warehouse_by_using_code(warehouse)

        if doc_type == "Sampling":
            doc_type = "P"
        else:
            doc_type = "S"

        if type == "valid":
            updated_del_dt = datetime.datetime.today() + datetime.timedelta(days=1)
        else:
            updated_del_dt = datetime.datetime.today() + datetime.timedelta(days=-1)

        updated_payload = {
                "WHS_ID": wh_id,
                "STATUS": "Open",
                "ACTUAL_DELIVERY_DT": updated_del_dt.strftime('%Y-%m-%d'),
                "PICK_DOC_TYPE": pick_doc_type,
                "INVOICE_LIST": [
                    {
                        "INV_ID": invoice_id
                    }
                ],
                "PICKLIST_DOCTYPE": doc_type,
        }
        payload = json.dumps(updated_payload)
        print("Updated Picklist Payload :", payload)
        return payload
