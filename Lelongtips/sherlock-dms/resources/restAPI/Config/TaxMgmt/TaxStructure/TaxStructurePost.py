import secrets
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from resources.restAPI.Config.TaxMgmt.TaxGroup.TaxGroupPost import TaxGroupPost
from resources.restAPI.Config.TaxMgmt.TaxGroup.TaxGroupDelete import TaxGroupDelete
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json
import datetime
NOW = datetime.datetime.now()
Tax_Group_Post = TaxGroupPost()
Tax_Group_Delete = TaxGroupDelete()
END_POINT_URL = PROTOCOL + "taxation" + APP_URL


class TaxStructurePost(object):

    @keyword('user creates tax structure with ${data} data')
    def user_creates_tax_structure(self, data):
        url = "{0}tax-structure/".format(END_POINT_URL)
        payload = self.payload_tax_structure(data)
        print('Payload:', payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body = response.json()
        try:
            print("Result: ", response.json())
            BuiltIn().set_test_variable("${res_body}", response.json())
            BuiltIn().set_test_variable("${tax_struct_id}", body['ID'])
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user creates ${type} tax group prerequisite')
    def create_tax_structure_prerequisive(self, type):
        if type == "supplier":
            tg_dict = {"TYPE": "S"}
        elif type == 'product':
            tg_dict = {"TYPE": "P"}
        else:
            tg_dict = {"TYPE": "R"}
        BuiltIn().set_test_variable("${tax_group_details}", tg_dict)
        Tax_Group_Post.user_creates_tax_group("given")
        status_code = BuiltIn().get_variable_value(COMMON_KEY.STATUS_CODE)
        assert status_code == 201, "Failed to create tax group"
        tax_group = BuiltIn().get_variable_value("${res_body}")
        tax_group_id = BuiltIn().get_variable_value("${tax_group_id}")
        if type == 'product':
            BuiltIn().set_test_variable("${Product_TG}", tax_group)
            BuiltIn().set_test_variable("${Product_TG_ID}", tax_group_id)
        else:
            BuiltIn().set_test_variable("${Others_TG}", tax_group)
            BuiltIn().set_test_variable("${Others_TG_ID}", tax_group_id)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE,status_code)


    def payload_tax_structure(self, data):
        details = ""
        s_or_c_tax_group = BuiltIn().get_variable_value("${Others_TG}")
        res_product_tax_group = BuiltIn().get_variable_value("${Product_TG}")
        if data == 'edit':
            payload = BuiltIn().get_variable_value("${payload}")
        else:
            payload = {
                "TAX_STRUCTURE_CD": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
                "TAX_STRUCTURE_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(15)),
                "REG_IND": ''.join(secrets.choice('AC') for _ in range(1)),
                "TAX_GRP_CD": s_or_c_tax_group,
                "TAX_TYPE": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20)),
                "PRD_TAX_GRP": res_product_tax_group,
                "START_DT": str((NOW + datetime.timedelta(days=100)).strftime("%Y-%m-%d")),
                "END_DT": str((NOW + datetime.timedelta(days=110)).strftime("%Y-%m-%d"))
            }
        if data == 'given':
            details = BuiltIn().get_variable_value("&{TS_details}")
            payload.update((k, v) for k, v in details.items())
        BuiltIn().set_test_variable("${payload}", payload)
        dump_payload = json.dumps(payload)
        return dump_payload