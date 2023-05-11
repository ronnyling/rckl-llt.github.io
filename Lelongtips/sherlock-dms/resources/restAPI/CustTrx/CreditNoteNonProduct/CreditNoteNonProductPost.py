import json
import datetime
import secrets
from resources.restAPI.Config.ReferenceData.ReasonType import ReasonTypeGet, ReasonPost
from resources.restAPI.MasterDataMgmt.Customer import CustomerGet
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from resources.restAPI.CustTrx.SalesInvoice import SalesInvoiceGet
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route import RouteGet
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod, TokenAccess
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
import urllib3

CN_HEADER = "${cn_np_header_details}"
urllib3.disable_warnings()
END_POINT_URL = PROTOCOL + "credit-note" + APP_URL


class CreditNoteNonProductPost(object):

    def create_cn_np_tax_detail(self):
        cn_np_id = BuiltIn().get_variable_value(COMMON_KEY.RANDOM_ID)
        url = "{0}cn-header/{1}/cn-tax".format(END_POINT_URL, cn_np_id)
        common = APIMethod.APIMethod()
        payload = self.cn_np_tax_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("POST", url, payload)
        print("POST Status code for credit note non product tax is " + str(response.status_code))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        print('TAX BD', payload)

    #@keyword('user creates credit note non product with ${data_type} data')
    def create_cn_np_header(self, data):
        url = "{0}cn-header".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = self.credit_note_non_prd_header_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("POST", url, payload)
        print("POST Status code for credit note non product header is " + str(response.status_code))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body = response.json()
        print ('BODY BD', payload)
        if response.status_code == 200:
            BuiltIn().set_test_variable(COMMON_KEY.RANDOM_ID, body['ID'])
            self.create_cn_np_details()
            tax_ind = BuiltIn().get_variable_value("${tax_ind}")
            if tax_ind:
                self.create_cn_np_tax_detail()

    def create_cn_np_details(self):
        cn_np_id = BuiltIn().get_variable_value(COMMON_KEY.RANDOM_ID)
        url = "{0}cn-header/{1}/cn-detail".format(END_POINT_URL, cn_np_id)
        common = APIMethod.APIMethod()
        payload = self.cn_np_details_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("POST", url, payload)
        print("POST Status code for credit note non product details is " + str(response.status_code))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        print('DETAILS BD', payload)

    def cn_np_tax_payload(self):
        rand_value = str(secrets.randbelow(99)) + str(".") + str(secrets.randbelow(99))
        rand_perc = str(secrets.randbelow(50)) + str(".") + str(secrets.randbelow(90))
        payload = {
            "UNIT_TAX": rand_value,
            "TAX_AMT": rand_value,
            "PRD_ID": "D9293E7B:4AD07B46-DD6A-45B2-A6F2-B06C0F5A81C1",
            "TAX_PERC": rand_perc,
            "APPLY_SEQ": 1,
            "TAXABLE_AMT": rand_value,
            "TAX_ID": "30498E7F:7410B8D0-41FA-4347-9A98-00646F7AB23A"
        }
        return payload

    def cn_np_details_payload(self):
        rand_value = str(secrets.randbelow(99)) + str(".") + str(secrets.randbelow(99))
        inv_no = BuiltIn().get_variable_value("${inv_no}")
        inv_date = BuiltIn().get_variable_value("${inv_date}")
        payload = {
            "ITEM_NO": "1",
            "REFERENCE_NO": str(secrets.randbelow(999999)),
            "SAC_ID": "D9293E7B:4AD07B46-DD6A-45B2-A6F2-B06C0F5A81C1",
            "SVC_INV_NO": inv_no,
            "SVC_INV_DT": inv_date,
            "REMARK": rand_value,
            "GROSS_AMT": rand_value,
            "TAX_AMT": rand_value,
            "NET_AMT_TAX": rand_value,
            "NET_AMT": rand_value
        }
        return payload

    def credit_note_non_prd_header_payload(self):
        inv_no = None
        inv_id = None
        flag = False
        user_role = BuiltIn().get_variable_value("${user_role}")
        header_details = BuiltIn().get_variable_value(CN_HEADER)
        route_id = BuiltIn().get_variable_value("${route_id}")
        cust_id = BuiltIn().get_variable_value("${cust_id}")
        checking = BuiltIn().get_variable_value("${cn_np_header_details['INV_FLAG']}")
        if checking:
            flag = True
        if flag and user_role == "distadm":
            body_result = SalesInvoiceGet.SalesInvoiceGet().user_retrieves_cust_inv_based_on_flag(header_details['INV_CUST'], header_details['INV_FLAG'])
            print("INV RESULT", body_result)
            inv_no = body_result['INV_NO']
            inv_id = body_result['ID']
            inv_date =  body_result['INV_DT']
            BuiltIn().set_test_variable("${inv_no}", inv_no)
            BuiltIn().set_test_variable("${inv_date}", inv_date)
        reason_id = BuiltIn().get_variable_value("${res_bd_reason_id}")
        rp_id = BuiltIn().get_variable_value("${rp_id}")
        prime = header_details['PRIME_FLAG']
        rand_value = str(secrets.randbelow(99)) + str(".") + str(secrets.randbelow(99))
        tax_ind = False
        BuiltIn().set_test_variable("${tax_ind}", tax_ind)
        payload = {
            "TXN_DT": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            "ROUTE_ID": route_id,
            "RP_ID": rp_id,
            "CUST_ID": cust_id,
            "REASON_ID": reason_id,
            "INV_ID": inv_id,
            "INV_NO": inv_no,
            "CLAIMABLE_IND": secrets.choice([True, False]),
            "REMARK": "",
            "STATUS": 'P',
            "TAXABLE_IND": tax_ind,
            "GROSS_TTL": rand_value,
            "NET_TTL": rand_value,
            "NET_TTL_TAX": rand_value,
            "ADJ_AMT": rand_value,
            "TAX_TTL": rand_value,
            "PRIME_FLAG": prime
        }
        return payload

    def payload_combine(self, type):
        payload_header = self.credit_note_non_prd_header_payload()
        payload_details = self.cn_np_details_payload()
        prd_tax = []
        if type == 'taxable':
            prd_tax = [self.cn_np_tax_payload()]
        payload = {
            "TXN_HEADER": payload_header,
            "TXN_PRODUCT": [payload_details],
            "TXN_PRDTAX": prd_tax
        }
        print ("FULL ",payload)
        return payload

    #@keyword('user post credit note non product with ${type} data')
    @keyword('user creates credit note non product with ${data_type} data')
    def user_post_cn_np(self, type):
        url = "{0}credit-note-np".format(END_POINT_URL)
        payload = self.payload_combine(type)
        print ('FULL',payload)
        payload = json.dumps(payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print("POST Status code for credit note non product header is " + str(response.status_code))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body = response.json()
        if response.status_code == 201:
            print("Output Result", body)
            BuiltIn().set_test_variable('${cn_np_id}', body['TXN_HEADER']['ID'])

    @keyword("user get ${cn_type} credit note non product prerequisite")
    def user_get_credit_note_no_prd_prerequisite(self, cn_type):
        TokenAccess.TokenAccess().user_retrieves_token_access_as("hqadm")
        DistributorGet.DistributorGet().user_gets_distributor_by_using_code('DistEgg')
        RouteGet.RouteGet().user_gets_route_by_using_code('Rchoon')
        RouteGet.RouteGet().user_gets_route_plan_by_using_code('CY0000000417')
        CustomerGet.CustomerGet().user_gets_cust_by_using_code('CT0000001549')
        ReasonTypeGet.ReasonTypeGet().user_retrieves_reason_type('Credit Note Non Product')
        ReasonPost.ReasonPost().user_creates_reason_with("random")
        if cn_type == "Prime":
            cn_np_header_details = {"PRIME_FLAG": "PRIME"}
        else:
            cn_np_header_details = {"PRIME_FLAG": "NON_PRIME"}
        BuiltIn().set_test_variable(CN_HEADER, cn_np_header_details)
