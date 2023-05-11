from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from resources.restAPI.CompTrx.CompanyInvoice import CompanyInvoicePost
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json

END_POINT_URL = PROTOCOL + "inventory" + APP_URL


class CompanyInvoicePut(object):

    @keyword('user updates company invoice using ${data} data')
    def user_updates_company_invoice(self, data):
        inv_id = BuiltIn().get_variable_value("${inv_id}")
        url = "{0}company-invoice/{1}".format(END_POINT_URL, inv_id)
        payload = CompanyInvoicePost.CompanyInvoicePost().payload("updates", "SAVE")
        rand_string = COMMON_KEY.generate_random_id("0")
        payload['PRODUCT_DETAILS'][0]['ID'] = rand_string
        payload['PRODUCT_DETAILS'][0]['IS_DELETED'] = False
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, json.dumps(payload))
        print("Updated CI Payload:", payload)
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${inv_id}", body_result[0]['InvoiceId'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)
