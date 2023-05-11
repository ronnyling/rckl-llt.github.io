import json
import datetime
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Config.ReferenceData.ClaimType import ClaimTypeGet
from resources.web import COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
NOW = datetime.datetime.now()
END_POINT_URL = PROTOCOL + "claim" + APP_URL


class PromotionClaimPost(object):
    TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.000Z"
    PAY_VARIABLE = "${payload}"
    CLAIM_ID_VARIABLE = "${claim_id}"

    @keyword('user creates ${type} claims')
    def user_creates_promotion_claims(self, type):
        url = "{0}add-claim".format(END_POINT_URL)
        if type == "non-customer related":
            payload = self.non_cust_related_claim_payload()
        else:
            payload = self.promotion_claim_payload(type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body = response.json()
        if response.status_code == 201:
            claim_id = body['CLAIM_HEADER']['ID']
            BuiltIn().set_test_variable(self.CLAIM_ID_VARIABLE, claim_id)

    def promotion_claim_payload(self, type):
        if type == "promotion":
            claim_type = "P"
        elif type == "spacebuy":
            claim_type = "S"
        status = BuiltIn().get_variable_value("${ClaimDetails}")
        status = status["ClaimStatus"]
        promo_id = BuiltIn().get_variable_value("${promo_id}")
        claim_amt = BuiltIn().get_variable_value("${claim_amt}")
        promo_amt = BuiltIn().get_variable_value("${promo_amt}")
        cust_id = BuiltIn().get_variable_value("${cust_id}")
        doc_id = BuiltIn().get_variable_value("${doc_id}")
        doc_type = BuiltIn().get_variable_value("${doc_type}")
        claim_perc = BuiltIn().get_variable_value("${claim_perc}")
        payload = {
            "CLAIM_HEADER": {
                "CLAIM_TYPE": claim_type,
                "PROMO_ID": promo_id,
                "MULTIPROMO_IND": False,
                "CLAIM_AMOUNT": claim_amt,
                "PROMO_AMOUNT": promo_amt,
                "REMARK": "",
                "STATUS": status,
                "FROM_DT": "2019-02-01",
                "TO_DT": str((NOW + datetime.timedelta(days=2)).strftime(self.TIME_FORMAT)),

            },
            "DOC_DTLS": [
                {
                    "CUST_ID": cust_id,
                    "DOC_ID": doc_id,
                    "PROMO_ID": promo_id,
                    "CLAIM_AMOUNT": claim_amt,
                    "PROMO_AMOUNT": promo_amt,
                    "APPROVE_AMOUNT": "0",
                    "DOC_TYPE": doc_type,
                    "CLAIMABLE_PERC": claim_perc,
                }
            ]
        }

        BuiltIn().set_test_variable(self.PAY_VARIABLE, payload)
        payload = json.dumps(payload)
        print("Promotion Claim: ", payload)
        return payload

    def non_cust_related_claim_payload(self):
        claim_details = BuiltIn().get_variable_value("${ClaimDetails}")
        status = claim_details["ClaimStatus"]
        claim_amt = claim_details["Amount"]
        claim_type_non_cust = claim_details['Claim_Type_Non_Cust']
        claim_type_non_cust_id = ClaimTypeGet.ClaimTypeGet().get_claim_type_id_by_code(claim_type_non_cust)

        payload = {
            "CLAIM_HEADER": {
                "CLAIM_TYPE": "N",
                "STATUS": status,
                "FROM_DT": "2023-02-15",
                "TO_DT": str((NOW + datetime.timedelta(days=2)).strftime(self.TIME_FORMAT)),
                "PROMO_ID": None,
                "MULTIPROMO_IND": None,
                "CLAIM_AMOUNT": claim_amt,
                "FILEUPLOAD_ID": None,
                "REMARK": "",
                "CUST_ID": None
            },
            "DOC_DTLS": [
                {
                    "CLAIM_TYPE": claim_type_non_cust_id,
                    "FILEUPLOAD_ID": None,
                    "REASON_ID": None,
                    "REMARK": "",
                    "CLAIM_AMOUNT": claim_amt,
                    "APPROVE_AMOUNT": "0"
                }
            ]
        }

        BuiltIn().set_test_variable(self.PAY_VARIABLE, payload)
        payload = json.dumps(payload)
        print("Non-Customer Related Claim: ", payload)
        return payload

    @keyword('user cancelled created claims')
    def user_cancelled_claims(self):
        url = "{0}update-claim-status".format(END_POINT_URL)
        payload = self.cancel_claim_payload()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body = response.json()
        print(body)
        print("payload", payload)

    def cancel_claim_payload(self):
        claim_id = BuiltIn().get_variable_value(self.CLAIM_ID_VARIABLE)
        payload = [{
            "ID": claim_id,
            "STATUS": "C"
        }]
        BuiltIn().set_test_variable(self.PAY_VARIABLE, payload)
        payload = json.dumps(payload)
        print("Cancelled Claim: ", payload)
        return payload

    @keyword('user reject created claims')
    def user_reject_claim(self):
        claim_id = BuiltIn().get_variable_value(self.CLAIM_ID_VARIABLE)
        url = "{0}claim/{1}/reject".format(END_POINT_URL, claim_id)
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        print(response.status_code)
        print(response)
        return response.status_code

    @keyword('user gets the ${claim_type} details')
    def get_promo_doc_filter(self, claim_type):
        url = "{0}promo-documents-filter".format(END_POINT_URL)
        payload = self.promo_doc_filter(claim_type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body = response.json()
        print("payload", payload)
        if str(response.status_code) != "200" in response.text:
            return response.status_code, "", "", "", "", "", ""
        else:
            data = response.json()
            print(json.dumps(data, indent=4))
            BuiltIn().set_test_variable("${promo_id}", body["fieldValueRecords"][0]["PROMO_ID"])
            BuiltIn().set_test_variable("${claim_amt}", body["fieldValueRecords"][0]["CLAIM_AMOUNT"])
            BuiltIn().set_test_variable("${promo_amt}", body["fieldValueRecords"][0]["PROMO_AMOUNT"])
            BuiltIn().set_test_variable("${cust_id}", body["fieldValueRecords"][0]["CUST_ID"])
            BuiltIn().set_test_variable("${doc_id}", body["fieldValueRecords"][0]["DOC_ID"])
            BuiltIn().set_test_variable("${doc_type}", body["fieldValueRecords"][0]["DOC_TYPE"])
            BuiltIn().set_test_variable("${claim_perc}", body["fieldValueRecords"][0]["CLAIMABLE_PERC"])

    def promo_doc_filter(self, claim_type):
        if claim_type == "promotion":
            c_type = "P"
        else:
            c_type = "S"
        payload = {
            "CLAIM_TYPE": c_type,
            "START_DATE": "2019-10-01",
            "END_DATE": datetime.datetime.today().strftime("%Y-%m-%d")
        }
        BuiltIn().set_test_variable(self.PAY_VARIABLE, payload)
        payload = json.dumps(payload)
        print("promotion doc records: ", payload)
        return payload

    @keyword('user approve created claims')
    def user_approve_claim(self):
        claim_id = BuiltIn().get_variable_value(self.CLAIM_ID_VARIABLE)
        url = "{0}claim/{1}/activate".format(END_POINT_URL, claim_id)
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        print(response.status_code)
        print(response)
        return response.status_code

    @keyword('user dispute created claim')
    def user_dispute_claim(self):
        url = "{0}update-claim-status".format(END_POINT_URL)
        payload = self.dispute_claim_payload()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body = response.json()
        print(body)
        print("payload", payload)

    def dispute_claim_payload(self):
        claim_id = BuiltIn().get_variable_value(self.CLAIM_ID_VARIABLE)
        payload = [{
            "ID": claim_id,
            "STATUS": "X"
        }]
        BuiltIn().set_test_variable(self.PAY_VARIABLE, payload)
        payload = json.dumps(payload)
        print("Disputed Claim: ", payload)
        return payload

    @keyword('user acknowledge approved claim')
    def user_acknowledge_claims(self):
        url = "{0}update-claim-status/ack".format(END_POINT_URL)
        payload = self.ack_claim_payload()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body = response.json()
        print(body)
        print("payload", payload)

    def ack_claim_payload(self):
        claim_id = BuiltIn().get_variable_value(self.CLAIM_ID_VARIABLE)
        payload = [{
            "ID": claim_id,
            "STATUS": "K"
        }]
        BuiltIn().set_test_variable(self.PAY_VARIABLE, payload)
        payload = json.dumps(payload)
        print("Acknowledge Claim: ", payload)
        return payload

