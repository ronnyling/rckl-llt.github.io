from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import secrets
import string
import json
import ast
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.CustTrx.SalesReturn import SalesReturnEntitlementPost

END_POINT_URL = PROTOCOL + "promotion-eng" + APP_URL


class SalesReturnApplyPost(object):

    @keyword('user post invoice with foc to return apply')
    def user_post_invoice_with_foc_to_return_apply(self):
        url = "{0}promotion-eng/return/apply/".format(END_POINT_URL)
        payload = self.payload_apply()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 200:
            response_dict = json.loads(response.text)
            print("Result: ", response_dict)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_apply(self):
        entitlement = SalesReturnEntitlementPost.SalesReturnEntitlementPost()
        TXN_HEADER = entitlement.txn_header()
        TXN_PRODUCT = entitlement.txn_product()

        payload = \
            {
                "TXN_HEADER": TXN_HEADER,
                "TXN_PRODUCT": TXN_PRODUCT
            }

        details = BuiltIn().get_variable_value("&{return_details}")
        for k, v in details.items():
            if "PROMO_FOC_ALLOCATE-" in k:
                PROMO_FOC_ALLOCATE = self.promo_foc_allocate()
                payload = \
                    {
                        "TXN_HEADER": TXN_HEADER,
                        "TXN_PRODUCT": TXN_PRODUCT,
                        "PROMO_FOC_ALLOCATE": PROMO_FOC_ALLOCATE
                    }
                break

        payload = json.dumps(payload)
        print("Payload: ", payload)
        return payload

    def promo_foc_allocate(self):
        block = \
            {
                "PROMO_ID": ''.join(secrets.choice(string.ascii_lowercase) for _ in range(40)),
                "PROMO_SLAB_ID": ''.join(secrets.choice(string.ascii_lowercase) for _ in range(40)),
                "PRD_ID": ''.join(secrets.choice(string.ascii_lowercase) for _ in range(40)),
                "PRDCAT_ID": None,
                "PRDCAT_VALUE_ID": ''.join(secrets.choice(string.ascii_lowercase) for _ in range(40)),
                "FOC_UOM_ID": ''.join(secrets.choice(string.ascii_lowercase) for _ in range(40)),
                "FOC_QTY": str(secrets.randbelow(9999999)),
                "INV_ID": ''.join(secrets.choice(string.ascii_lowercase) for _ in range(40)),
                "BALANCE_QTY": str(secrets.randbelow(9999999)),
                "RET_FOC_QTY": str(secrets.randbelow(9999999)),
                "CHARGE_QTY": str(secrets.randbelow(9999999)),
                "COST_PRC": str(secrets.randbelow(9999999))
            }

        details = BuiltIn().get_variable_value("&{return_details}")
        if details:
            for k, v in details.items():
                if v == "" or type(v) is int:  # skip empty or int cells
                    pass
                elif v.casefold() == 'null':
                    details[k] = ast.literal_eval("None")
            block.update((k.split('-')[1], v) for k, v in details.items() if "PROMO_FOC_ALLOCATE-" in k if v)

        return block
