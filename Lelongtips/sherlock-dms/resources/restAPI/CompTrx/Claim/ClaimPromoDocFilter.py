from resources.restAPI.CustTrx.SalesInvoice import InvoicePost
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
import json
import datetime

NOW = datetime.datetime.now()
CLAIM_POINT_URL = PROTOCOL + "claim" + APP_URL


class ClaimPromoDocFilter(object):

    @keyword("user filter ${type} document")
    def user_filter_promo_document(self, type):
        if type == "sampling":
            url = "{0}sampling-documents".format(CLAIM_POINT_URL)
        elif type == "damaged":
            url = "{0}damage-documents".format(CLAIM_POINT_URL)
        elif type == "others - customer related":
            url = "{0}other-documents".format(CLAIM_POINT_URL)
        elif type == "incentive":
            url = "{0}incentive-documents".format(CLAIM_POINT_URL)
        else:
            url = "{0}promo-documents-filter".format(CLAIM_POINT_URL)
        body_result = ""
        payload = self.promo_filter_payload(type)
        print("Payload:", payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${claim_filter_res}", body_result)
            print("Body Result: ", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        return body_result

    def promo_filter_payload(self, type):
        if type == "promo":
            claim_type = "P"
        elif type == "spacebuy":
            claim_type = "S"
        elif type == "sampling":
            claim_type = "F"
        elif type == "damaged":
            claim_type = "D"
        elif type == "others - customer related":
            claim_type = "C"
        elif type == "incentive":
            claim_type = "I"

        st_date = str((NOW + datetime.timedelta(days=0)).strftime("%Y-%m-%d"))
        end_date = str((NOW + datetime.timedelta(days=100)).strftime("%Y-%m-%d"))

        payload = {
         "CLAIM_TYPE": claim_type,
         "START_DATE": st_date,
         "END_DATE": end_date
        }

        if type == "incentive":
            payload['FROM_DT'] = payload.pop('START_DATE')
            payload['TO_DT'] = payload.pop('END_DATE')

        details = BuiltIn().get_variable_value("${filter_payload}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        return payload
