
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
import json

from resources.restAPI.VanInventory.VanReplenishment.VanReplenishmentGet import VanReplenishmentGet

INVT_END_POINT_URL = PROTOCOL + "inventory" + APP_URL


class VanReplenishmentPut(object):
    @keyword("user puts to ${operation} van replenishment")
    def user_puts_van_replenishment(self, operation):
        VanReplenishmentGet().user_retrieves_van_replenishment_details()
        van_rep_payload = BuiltIn().get_variable_value("${van_rep_details}")
        tmp_WHS_ID_FROM_ID = {}
        tmp_WHS_ID_TO_ID = {}
        van_rep_id = BuiltIn().get_variable_value("${van_rep_id}")
        url = "{0}van-replenishment/{1}".format(INVT_END_POINT_URL, van_rep_id)
        if operation == "confirm":
            van_rep_payload['STATUS'] = 'S'
        elif operation == "save":
            van_rep_payload['STATUS'] = 'P'
        van_rep_payload['DOWNLOAD_DT'] = ""
        van_rep_payload['REF_TYPE'] = ""
        van_rep_payload['REF_KEY'] = ""
        van_rep_payload['STKREQ_ID'] = ""
        van_rep_payload['STKREQ_NO'] = ""
        tmp_WHS_ID_FROM_ID['ID'] = van_rep_payload['WHS_ID_FROM']['ID']
        van_rep_payload.pop('WHS_ID_FROM')
        van_rep_payload['WHS_ID_FROM'] = tmp_WHS_ID_FROM_ID
        tmp_WHS_ID_TO_ID['ID'] = van_rep_payload['WHS_ID_TO']['ID']
        van_rep_payload.pop('WHS_ID_TO')
        van_rep_payload['WHS_ID_TO'] = tmp_WHS_ID_TO_ID
        van_rep_payload.pop('TXN_CREATED_DT')
        van_rep_payload['ROUTE_INFO'].pop('VAN')
        van_rep_payload.pop('STATUS')
        van_rep_payload.pop('HHT_CREATED_BY')
        van_rep_payload.pop('HHT_SUBMIT_DT')
        van_rep_payload.pop('PRN_NO')
        for i in van_rep_payload['PRODUCTS']:
            i.pop('AVAILABLE_QTY_DISP')
            for j in i['UOMS']:
                j['SALE_UOM'] = True
                j['GROSS_WEIGHT'] = "" if j['GROSS_WEIGHT'] is None else j['GROSS_WEIGHT']
                j['WEIGHT_UNIT'] = "" if j['WEIGHT_UNIT'] is None else j['WEIGHT_UNIT']
                j.pop('UOM_DESCRIPTION')
                j.pop('UOM_CD')
        payload = json.dumps(van_rep_payload)
        print("payload = " + str(payload))
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        return response.status_code
