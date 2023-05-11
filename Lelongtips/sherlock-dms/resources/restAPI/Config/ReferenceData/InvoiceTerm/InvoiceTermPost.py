import secrets

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod, TokenAccess
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class InvoiceTermPost(object):
    """ Function to create invoice term with random/fixed data """

    @keyword('user creates invoice term with ${data_type}')
    def user_creates_invoice_term_with(self, data_type):
        """ Function to create invoice term with random/fixed data """
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributors/{1}/setting-invoice-term".format(END_POINT_URL, dist_id)
        payload = self.payload_invoice_term()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${res_bd_inv_term_id}", body_result['ID'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_invoice_term(self):
        """ Function for invoice term payload content """
        header = BuiltIn().get_variable_value("${invoice_term_header}")
        details = BuiltIn().get_variable_value("${invoice_term_details}")
        term_days = secrets.choice(range(1, 100))
        payload = {
            "TERMS": ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            #"TERMS_DAYS": ''.join(secrets.choice('0123456789') for _ in range(2)),
            "TERMS_DAYS": str(term_days),
            "TERMS_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20)),
            "SETTING-INVOICE-TERM-DETAIL": [
                {
                    "DISC_PERC": secrets.choice(range(1, 100)),
                    #"INV_DUE_DAYS": ''.join(secrets.choice('0123456789') for _ in range(2))
                    "INV_DUE_DAYS": str(secrets.choice(range(1, term_days))),
                }
            ]
            }
        print("payload is ", payload)
        if header:
            payload.update((k, v) for k, v in header.items())
        if details:
            payload['SETTING-INVOICE-TERM-DETAIL'][0].update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        return payload

    def user_creates_invoice_term_as_prerequisite(self):
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        self.user_creates_invoice_term_with("random")
