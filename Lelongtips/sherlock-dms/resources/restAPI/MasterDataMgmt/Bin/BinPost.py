import secrets, json
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI.MasterDataMgmt.Warehouse import WarehouseGet
END_POINT_URL = PROTOCOL + "setting" + APP_URL

class BinPost(object):



    @keyword('user creates bin with ${data_type} data')
    def user_creates_bin_with(self,data_type):

        url = "{0}warehouse-bin".format(END_POINT_URL)
        payload = self.payload_bin()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${res_bd_bin_payload}", body_result)
            BuiltIn().set_test_variable("${res_bd_bin_id}", body_result["ID"])
            BuiltIn().set_test_variable("${res_bd_bin_cd}", body_result["BIN_CODE"])
            BuiltIn().set_test_variable("${res_bd_bin}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_bin(self):
        payload = {

            "SINGLE_MULTIPLE": secrets.choice([True, False]),
            "PICKING_AREA": secrets.choice([True, False]),
            "REMARKS": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(15)),
            "BIN_CODE": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(10)),
            "RACK": ''.join(secrets.choice('0123456789') for _ in range(2)),
            "COLUMN": ''.join(secrets.choice('0123456789') for _ in range(2)),
            "LEVEL": ''.join(secrets.choice('0123456789') for _ in range(2)),
            "BIN_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(15)),
            "WAREHOUSE_CODE": self.warehouse_payload()

        }

        details = BuiltIn().get_variable_value("${bin_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Bin Payload: ", payload)
        return payload

    def warehouse_payload(self):
        body_result = WarehouseGet.WarehouseGet.user_gets_warehouse_by_using_type(self, "PRIME")
        BuiltIn().set_test_variable("${body_result}", body_result)
        warehouse = {
            "ID": body_result[1][0]['ID'],
            "WHS_CD": body_result[1][0]['WHS_CD'],
            "WHS_DESC": body_result[1][0]['WHS_DESC'],
            "DIST_ID": body_result[1][0]['DIST_ID'],
            "PRIME_FLAG": body_result[1][0]['PRIME_FLAG'],
            "WHS_BATCH_TRACE": body_result[1][0]['WHS_BATCH_TRACE'],
            "WHS_EXP_MAND": body_result[1][0]['WHS_EXP_MAND'],
            "WHS_IS_DAMAGE": body_result[1][0]['WHS_IS_DAMAGE'],
            "WHS_IS_VAN": body_result[1][0]['WHS_IS_VAN'],
            "VAN_ID": body_result[1][0]['VAN_ID'],
            "WHS_IS_BLOCKED": body_result[1][0]['WHS_IS_BLOCKED'],
            "IS_VARIANCE": body_result[1][0]['IS_VARIANCE'],
            "SHIP_TO": body_result[1][0]['SHIP_TO'],
            "IS_DUMMY": body_result[1][0]['IS_DUMMY'],
            "IS_DELETED": body_result[1][0]['IS_DELETED'],
            "MODIFIED_DATE": body_result[1][0]['MODIFIED_DATE'],
            "MODIFIED_BY": body_result[1][0]['MODIFIED_BY'],
            "CREATED_DATE": body_result[1][0]['CREATED_DATE'],
            "CREATED_BY": body_result[1][0]['CREATED_BY'],
            "VERSION": body_result[1][0]['VERSION'],
            "CORE_FLAGS": body_result[1][0]['CORE_FLAGS']
        }
        return warehouse