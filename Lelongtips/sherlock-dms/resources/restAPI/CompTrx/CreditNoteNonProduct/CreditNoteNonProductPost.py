from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.MasterDataMgmt.Supplier import SupplierGet
from resources.restAPI.Config.ReferenceData.ReasonType import ReasonTypeGet
from resources.restAPI.Config.TaxMgmt.ServiceMaster import ServiceMasterGet
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet

import json
import secrets
import datetime

END_POINT_URL = PROTOCOL + "credit-note" + APP_URL
TAX_END_POINT_URL = PROTOCOL + "taxation" + APP_URL


class CreditNoteNonProductPost(object):

    @keyword('user creates credit note non product using ${data} data')
    def user_creates_credit_note_non_product(self, data):
        url = "{0}supplier-cn-np".format(END_POINT_URL)
        payload = self.payload("SAVE")
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, json.dumps(payload))
        print("CNNP Payload", payload)
        if response.status_code == 201:
            body_result = response.json()
            print("Body Result: ", body_result)
            BuiltIn().set_test_variable("${scnnp_id}", body_result['TXN_HEADER']['ID'])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def payload(self, post_type):
        scnnp_id = BuiltIn().get_variable_value("${scnnp_id}")
        cnnp_details = BuiltIn().get_variable_value("${cnnp_details}")
        current_date = str(datetime.datetime.now().strftime("%Y-%m-%d"))
        supplier_id = SupplierGet.SupplierGet().user_retrieves_supplier_by_code(cnnp_details['SUPPLIER'])
        ReasonTypeGet.ReasonTypeGet().user_gets_reason_by_using_code("", "SCNNP")
        reason_id = BuiltIn().get_variable_value("${res_bd_reason_id}")
        dist_id = DistributorGet.DistributorGet().user_gets_distributor_by_using_code(cnnp_details['DIST'])
        amt = cnnp_details['AMOUNT']
        svc_details = ServiceMasterGet.ServiceMasterGet().user_get_service_master_by_code(cnnp_details['SVC_CD'])
        sac_id = svc_details['ID']
        sup_svc_tax = self.get_supplier_svc_tax(dist_id, supplier_id, svc_details['SVC_CD'], amt)
        svc_tax = sup_svc_tax['SERVICE_TAX'][0]
        tax_info = svc_tax['TAX_INFO']
        tax_details = []
        for x in tax_info:
            tax_list = {
                "SAC_INDEX": "1",
                "TXN_ID": scnnp_id,
                "SAC_ID": sac_id,
                "UNIT_TAX": str(x['AMT']),
                "TAX_AMT": str(x['AMT']),
                "TAX_ID": x['TAX_ID'],
                "APPLE_SEQ": int(x['APPLY_SEQ']),
                "TAXABLE_AMT": str(x['TAXABLE_AMT']),
                "NET_AMT": amt,
                "TAX_PERC": x['TAX_RATE']
            }
            tax_details.append(tax_list)

        if post_type == "SAVE AND CONFIRM":
            status = "C"
        else:
            status = "O"

        payload = {
            "TXN_HEADER": {
                "POST_TYPE": post_type,
                "STATUS": status,
                "SUPPLIER_ID": supplier_id,
                "REASON_ID": reason_id,
                "REMARK": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
                "TXN_DT": current_date,
                "GROSS_TTL": svc_tax['GROSS_AMT'],
                "ADJ_AMT": "-0.1",
                "TAX_TTL": str(svc_tax['GROSS_TAX_AMT']),
                "NET_TTL": svc_tax['GROSS_AMT'],
                "ERP_IND": False,
                "TXN_NO": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
                "PRIME_FLAG": "PRIME",
                "NET_TTL_TAX": str(svc_tax['NET_AMT_TTL']),
                "TAXABLE_IND": True
            },
            "SERVICE_DETAILS": [
                {
                    "TXN_ID": scnnp_id,
                    "ITEM_NO": "1",
                    "REFERENCE_NO": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
                    "GROSS_AMT": svc_tax['GROSS_AMT'],
                    "REMARK": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
                    "SAC_ID": sac_id,
                    "NET_AMT": svc_tax['GROSS_AMT'],
                    "NET_AMT_TAX": str(svc_tax['NET_AMT_TTL']),
                    "TAX_AMT": str(svc_tax['GROSS_TAX_AMT'])
                }
            ],
            "TAX_DETAILS": tax_details
        }
        return payload

    def get_supplier_svc_tax(self, dist_id, sup_id, svc_cd, amt):
        url = "{0}supplier-service-tax".format(TAX_END_POINT_URL)
        payload = self.svc_payload(dist_id, sup_id, svc_cd, amt)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, json.dumps(payload))
        assert response.status_code == 200, "Unable to retrieve service"
        body_result = response.json()
        return body_result

    def svc_payload(self, dist_id, sup_id, svc_cd, amt):
        current_dt = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        payload = {
            "TXN_HEADER": {
                "TXN_DT": current_dt,
                "DIST_ID": dist_id,
                "SUPPLIER_ID": sup_id
            },
            "SERVICE_TAX": [
                {
                    "SVC_CD": svc_cd,
                    "GROSS_AMT": amt
                }
            ]
        }
        return payload
