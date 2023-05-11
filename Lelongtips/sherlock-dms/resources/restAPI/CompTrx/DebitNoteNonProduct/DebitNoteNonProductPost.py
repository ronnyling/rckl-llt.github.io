import datetime
import json
import secrets

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from resources.restAPI.Config.ReferenceData.ReasonType import ReasonTypeGet
from resources.restAPI.Config.TaxMgmt.ServiceMaster import ServiceMasterGet
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from resources.restAPI.MasterDataMgmt.Supplier import SupplierGet

END_POINT_URL = PROTOCOL + "debit-note-sup" + APP_URL
TAX_END_POINT_URL = PROTOCOL + "taxation" + APP_URL
current_date = str(datetime.datetime.now().strftime("%Y-%m-%d"))


class DebitNoteNonProductPost(object):

    @keyword('user creates debit note non product using ${data} data')
    def user_creates_debit_note_non_product(self, data):
        url = "{0}supplier-dn-np-header".format(END_POINT_URL)
        dn_payload = self.dn_payload("SAVE")
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, dn_payload)
        if response.status_code == 201:
            body_result = response.json()
            sdnnp_id = body_result['ID']
            BuiltIn().set_test_variable("${sdnnp_id}", sdnnp_id)
            tax_url = "{0}supplier-dn-np-header/{1}/dn-tax".format(END_POINT_URL, sdnnp_id)
            dn_tax_payload = self.dn_tax_payload()
            response = common.trigger_api_request("POST", tax_url, dn_tax_payload)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def get_supplier_and_service_details(self):
        dnnp_details = BuiltIn().get_variable_value("${dnnp_details}")
        supplier_id = SupplierGet.SupplierGet().user_retrieves_supplier_by_code(dnnp_details['SUPPLIER'])
        BuiltIn().set_test_variable("${supplier_id}", supplier_id)
        ReasonTypeGet.ReasonTypeGet().user_gets_reason_by_using_code(dnnp_details['REASON'], "SDNNP")
        dist_id = DistributorGet.DistributorGet().user_gets_distributor_by_using_code(dnnp_details['DIST'])
        amt = dnnp_details['AMOUNT']
        BuiltIn().set_test_variable("${amt}", amt)
        svc_details = ServiceMasterGet.ServiceMasterGet().user_get_service_master_by_code(dnnp_details['SVC_CD'])
        BuiltIn().set_test_variable("${sac_id}", svc_details['ID'])
        sup_svc_tax = self.get_supplier_svc_tax(dist_id, supplier_id, svc_details['SVC_CD'], amt)
        BuiltIn().set_test_variable("${svc_tax}", sup_svc_tax['SERVICE_TAX'][0])

    def dn_tax_payload(self):
        sdnnp_id = BuiltIn().get_variable_value("${sdnnp_id}")
        self.get_supplier_and_service_details()
        amt = BuiltIn().get_variable_value("${amt}")
        sac_id = BuiltIn().get_variable_value("${sac_id}")
        svc_tax = BuiltIn().get_variable_value("${svc_tax}")

        tax_info = svc_tax['TAX_INFO']
        dn_tax_payload = []
        for x in tax_info:
            tax_list = {
                "SAC_INDEX": "1",
                "TXN_ID": sdnnp_id,
                "SAC_ID": sac_id,
                "UNIT_TAX": str(x['AMT']),
                "TAX_AMT": str(x['AMT']),
                "TAX_ID": x['TAX_ID'],
                "APPLE_SEQ": int(x['APPLY_SEQ']),
                "TAXABLE_AMT": str(x['TAXABLE_AMT']),
                "NET_AMT": amt,
                "TAX_PERC": x['TAX_RATE']
            }
            dn_tax_payload.append(tax_list)
        dn_tax_payload = json.dumps(dn_tax_payload)
        return dn_tax_payload

    def dn_payload(self, post_type):
        self.get_supplier_and_service_details()
        supplier_id = BuiltIn().get_variable_value("${supplier_id}")
        reason_id = BuiltIn().get_variable_value("${res_bd_reason_id}")
        sac_id = BuiltIn().get_variable_value("${sac_id}")
        svc_tax = BuiltIn().get_variable_value("${svc_tax}")
        svc_dtl_id = BuiltIn().get_variable_value("${svc_dtl_id}")
        sdnnp_id = BuiltIn().get_variable_value("${sdnnp_id}")

        if post_type == "SAVE AND CONFIRM":
            status = "C"
        else:
            status = "O"

        dn_payload = {
            "POST_TYPE": post_type,
            "STATUS": status,
            "SUPPLIER_ID": supplier_id,
            "REASON_ID": reason_id,
            "REMARK": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "TXN_DT": current_date,
            "DUE_DT": current_date,
            "GROSS_TTL": svc_tax['GROSS_AMT'],
            "ADJ_AMT": "-0.1",
            "TAX_TTL": str(svc_tax['GROSS_TAX_AMT']),
            "NET_TTL": svc_tax['GROSS_AMT'],
            "ERP_IND": False,
            "TXN_NO": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "PRIME_FLAG": "PRIME",
            "NET_TTL_TAX": str(svc_tax['NET_AMT_TTL']),
            "TAXABLE_IND": True,
            "SERVICE_DETAILS": [
                {
                    "ID": svc_dtl_id,
                    "TXN_ID": sdnnp_id,
                    "ITEM_NO": "1",
                    "REFERENCE_NO": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
                    "GROSS_AMT": svc_tax['GROSS_AMT'],
                    "REMARK": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
                    "SAC_ID": sac_id,
                    "NET_AMT": svc_tax['GROSS_AMT'],
                    "NET_AMT_TAX": str(svc_tax['NET_AMT_TTL']),
                    "TAX_AMT": str(svc_tax['GROSS_TAX_AMT'])
                }
            ]
        }
        if dn_payload['SERVICE_DETAILS'][0]['ID'] is None:
            del dn_payload['SERVICE_DETAILS'][0]['ID']
        if dn_payload['SERVICE_DETAILS'][0]['TXN_ID'] is None:
            del dn_payload['SERVICE_DETAILS'][0]['TXN_ID']
        dn_payload = json.dumps(dn_payload)
        return dn_payload

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
