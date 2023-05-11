from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json
import ast
import secrets
import string
import datetime

END_POINT_URL = PROTOCOL + "promotion-eng" + APP_URL
NOW = datetime.datetime.now()


class SalesReturnEntitlementPost(object):

    @keyword('user sends invoice with non foc promo to return entitlement')
    def user_sends_invoice_with_non_foc_promo_to_return_entitlement(self):
        url = "{0}promotion-eng/return/entitlement/".format(END_POINT_URL)
        payload = self.payload_entitlement()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 200:
            response_dict = json.loads(response.text)
            print("Result: ", response_dict)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_entitlement(self):
        TXN_HEADER = self.txn_header()
        TXN_PRODUCT = self.txn_product()

        payload = {"TXN_HEADER": TXN_HEADER,
                   "TXN_PRODUCT": TXN_PRODUCT}

        payload = json.dumps(payload)
        print("Payload: ", payload)
        return payload

    def txn_header(self):
        block = \
            {
                "TXN_ID": None,
                "TXN_DT": NOW.today().strftime('%Y-%m-%d'),
                "DIST_ID": ''.join(secrets.choice(string.ascii_lowercase) for _ in range(40)),
                "CUST_ID": ''.join(secrets.choice(string.ascii_lowercase) for _ in range(40)),
                "ROUTE_ID": ''.join(secrets.choice(string.ascii_lowercase) for _ in range(40)),
                "NET_AMT": str(secrets.randbelow(9999999)),
                "WHS_ID": ''.join(secrets.choice(string.ascii_lowercase) for _ in range(40)),
                "FULL_IND": False
            }

        details = BuiltIn().get_variable_value("&{return_details}")
        if details:
            for k, v in details.items():
                if v == "" or type(v) is int:  # skip empty or int cells
                    pass
                elif v.casefold() == 'true':  # handling data input with true false attributes
                    details[k] = ast.literal_eval("True")
                elif v.casefold() == 'false':
                    details[k] = ast.literal_eval("False")
                elif v.casefold() == 'null':
                    details[k] = ast.literal_eval("None")
            block.update((k.split('-')[1], v) for k, v in details.items() if "TXN_HEADER-" in k if v)

        return block

    def txn_product(self):
        block = \
            {
                "INV_ID": ''.join(secrets.choice(string.ascii_lowercase) for _ in range(40)),
                "PRD_SLSTYPE": "S",
                "MRP": str(secrets.randbelow(9999999)),
                "PRD_ID": ''.join(secrets.choice(string.ascii_lowercase) for _ in range(40)),
                "UOM_ID": ''.join(secrets.choice(string.ascii_lowercase) for _ in range(40)),
                "PRD_INDEX": secrets.randbelow(9999999),
                "PRD_QTY": secrets.randbelow(9999999),
                "PRD_LISTPRC": str(secrets.randbelow(9999999)),
                "PRD_LISTPRC_UOM": str(secrets.randbelow(9999999)),
                "GROSS_AMT": str(secrets.randbelow(9999999)),
                "NET_AMT": str(secrets.randbelow(9999999)),
                "INVPRD_INDEX": secrets.randbelow(9999999)
            }

        details = BuiltIn().get_variable_value("&{return_details}")
        if details:
            if details.get('TXN_HEADER-FULL_IND').casefold() == "true":
                block.clear()
                block = []
                return block
            else:
                block.update((k.split('-')[1], v) for k, v in details.items() if "TXN_PRODUCT-" in k if v)
                return [block]
