from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from resources.restAPI.CompTrx.CompanyInvoice import CompanyInvoicePost
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

import json

from resources.restAPI.CompTrx.CompanyInvoice.CompanyInvoiceGet import CompanyInvoiceGet

END_POINT_URL = PROTOCOL + "inventory" + APP_URL


class CompanyInvoiceConfirm(object):

    @keyword('user confirms company invoice')
    def user_confirms_company_invoice(self):
        payload = CompanyInvoicePost.CompanyInvoicePost().payload("confirms", "SAVE AND CONFIRM")
        # CompanyInvoicePost.CompanyInvoicePost().user_creates_company_invoice("")
        inv_id = BuiltIn().get_variable_value("${inv_id}")
        # CompanyInvoiceGet().user_retrieves_company_invoice_by_id()
        # payload = BuiltIn().get_variable_value("${inv_dtls}")
        # payload['POST_TYPE'] = "SAVE AND CONFIRM"
        # if payload['STOCK_MOVEMENT'] == "false":
        #     payload['STOCK_MOVEMENT'] = False
        # else:
        #     payload['STOCK_MOVEMENT'] = True
        # payload['SUPPLIER'] = payload['SUPPLIER']['ID']
        # payload['WAREHOUSE'] = payload['WAREHOUSE']['ID']
        # payload['STATUS'] = payload['STATUS_OBJECT']['ID']
        # uom_ids = []
        # def_uom = None
        # for i in payload['PRODUCT_DETAILS'][0]['UOM']:
        #     uom_ids.append(i['ID'])
        #     if i['SML_UOM']:
        #         def_uom = i['ID']
        # payload['PRODUCT_DETAILS'][0]['UOM'] = payload['PRODUCT_DETAILS'][0]['UOM_ID']
        # payload['PRODUCT_DETAILS'][0]['DEF_UOM_ID'] = def_uom
        # payload['PRODUCT_DETAILS'][0]['VARIANCE'] = str(0)
        # payload['PRODUCT_DETAILS'][0]['PRD_INDEX'] = str(payload['PRODUCT_DETAILS'][0]['PRD_INDEX'])
        # payload['PRODUCT_DETAILS'][0]['PRD_QTY'] = str(payload['PRODUCT_DETAILS'][0]['PRD_QTY'])
        # payload['PRODUCT_DETAILS'][0]['INV_QTY'] = str(float(payload['PRODUCT_DETAILS'][0]['INV_QTY']))
        # payload['PRODUCT_DETAILS'][0]['DISCOUNT'] = None
        url = "{0}company-invoice/{1}".format(END_POINT_URL, inv_id)
        rand_string = COMMON_KEY.generate_random_id("0")
        payload['PRODUCT_DETAILS'][0]['ID'] = rand_string
        payload['PRODUCT_DETAILS'][0]['IS_DELETED'] = False
        print("url in cf = ", url)
        print("Confirmed CI Payload = ", json.dumps(payload))
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, json.dumps(payload))
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${inv_id}", body_result[0]['InvoiceId'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)
