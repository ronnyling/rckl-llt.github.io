import secrets
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from setup.hanaDB import HanaDB
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.MasterDataMgmt.Product import ProductGet
import json

END_POINT_URL = PROTOCOL + "invoice" + APP_URL


class SalesInvoiceGet(object):
    """ Functions to retrieve SalesInvoice transaction """
    RS_BD_INV ="${res_bd_invoice_id}"
    ERR_MSG = "ID retrieved not matched"

    @keyword("user retrieves ${cond} invoice")
    def user_retrieves_all_invoice(self, cond):
        """ Function to retrieve all invoice """
        distributor_id = BuiltIn().get_variable_value(COMMON_KEY.DISTRIBUTOR_ID)
        if cond == "all":
            url = "{0}distributors/{1}/invoice-header".format(END_POINT_URL, distributor_id)
        else:
            invoice_header_id = BuiltIn().get_variable_value(self.RS_BD_INV)
            url = "{0}distributors/{1}/invoice-header/{2}".format(END_POINT_URL, distributor_id, invoice_header_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${invoice_list}", body_result)
            print("Total number of records retrieved are ", len(body_result))
            if cond == "all":
                if len(body_result) > 1:
                    rand_so = secrets.randbelow(len(body_result))
                else:
                    rand_so = 0
                BuiltIn().set_test_variable("${rand_inv_selection}", body_result[rand_so]["ID"])
            else:
                BuiltIn().set_test_variable("${invoice_header_rs_bd}", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def validated_delivery_status_is_returned(self):
        inv_header = BuiltIn().get_variable_value("${invoice_header_rs_bd}")
        assert inv_header['DELIVERY_STATUS'] is not None, "Delivery Status column is not exist"

    def user_retrieves_invoice_by_id(self):
        """ Function to retrieve invoice by using id.
            Currently get all SalesInvoice and randomize pick 1 id to use.
            Will update again when SalesInvoice POST is ready """
        #self.user_retrieves_all_invoice("all")
        res_bd_invoice_id = BuiltIn().get_variable_value("${rand_inv_selection}")
        body_result = self.send_get_invoice_request(res_bd_invoice_id)
        return body_result

    def user_retrieves_particular_invoice_by_id(self):
        res_bd_invoice_id = BuiltIn().get_variable_value(self.RS_BD_INV)
        body_result = self.send_get_invoice_request(res_bd_invoice_id)
        return body_result

    def get_invoice_by_id(self):
        res_bd_invoice_id = BuiltIn().get_variable_value(self.RS_BD_INV)
        url = "{0}invoice/{1}".format(END_POINT_URL, res_bd_invoice_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            assert res_bd_id == res_bd_invoice_id, self.ERR_MSG
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        return body_result

    def send_get_invoice_request(self, res_bd_invoice_id):
        distributor_id = BuiltIn().get_variable_value(COMMON_KEY.DISTRIBUTOR_ID)
        url = "{0}distributors/{1}/invoice-header/{2}".format(END_POINT_URL, distributor_id, res_bd_invoice_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            assert res_bd_id == res_bd_invoice_id, self.ERR_MSG
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        return body_result

    def user_retrieves_invoice_product_by_id(self):
        """ Function to retrieve invoice product details by using id"""
        distributor_id = BuiltIn().get_variable_value(COMMON_KEY.DISTRIBUTOR_ID)
        res_bd_invoice_id = BuiltIn().get_variable_value("${res_bd_invoice_id}")
        res_bd_invoice_prd_id = BuiltIn().get_variable_value("${res_bd_invoice_prd_id}")
        url = "{0}distributors/{1}/invoice-header/{2}/invoice-detail"\
                    .format(END_POINT_URL, distributor_id, res_bd_invoice_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result[0]['TXN_ID']
            res_bd_prd_id = body_result[0]['PRD_ID']
            assert res_bd_id == res_bd_invoice_id, self.ERR_MSG
            assert res_bd_prd_id == res_bd_invoice_prd_id
            BuiltIn().set_test_variable("${res_inv_prd}",body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword("user retrieves '${cust}' cust inv based on flag '${flag}'")
    def user_retrieves_cust_inv_based_on_flag(self, cust, flag):
        filter_inv = [{"CUST_CD": {"$eq": cust}, "PRIME_FLAG": {"$eq": flag}}]
        filter_inv = json.dumps(filter_inv)
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributors/{2}/invoice-header?filter={1}".format(END_POINT_URL, filter_inv, dist_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve inv"
        body_result = response.json()
        body_result = secrets.choice(body_result)
        inv_id = body_result['ID']
        BuiltIn().set_test_variable("${INV}", inv_id)
        BuiltIn().set_test_variable("${inv_info}", body_result)
        return body_result

    def user_retrieves_inv_based_on_status(self, deliver_status, inv_status):
        """Changed to retrieve by API"""
        self.user_retrieves_all_invoice("all")
        inv_listing = BuiltIn().get_variable_value("${invoice_list}")
        inv_listing = json.dumps(inv_listing)
        inv_listing_converted = json.loads(inv_listing)

        inv_list_by_inv_status = [x for x in inv_listing_converted if x['INV_STATUS'] == inv_status]
        body_result = [x for x in inv_list_by_inv_status if x['DELIVERY_STATUS'] == deliver_status]

        inv_id = body_result[0]["ID"]
        BuiltIn().set_test_variable("${INV}", inv_id)
        BuiltIn().set_test_variable("${inv_info}", body_result)
        return body_result[0]

        """Comment out hana db script, change it to retrieve/update by API"""
        # query = "select cast(ID as varchar), cast(DIST_ID as varchar), cast(ROUTE_ID as varchar), cast(CUST_ID as varchar), cast(WHS_ID as varchar) FROM txn_invoice where INV_STATUS='{0}' AND DELIVERY_STATUS = '{1}' ORDER BY CREATED_DATE DESC".format(inv_status, deliver_status)
        # HanaDB.HanaDB().connect_database_to_environment()
        # result = HanaDB.HanaDB().fetch_all_record(query)
        # HanaDB.HanaDB().disconnect_from_database()
        # body_result = result[0]
        # inv_id = body_result[0]
        # BuiltIn().set_test_variable("${INV}", inv_id)
        # BuiltIn().set_test_variable("${inv_info}", body_result)
        # return body_result

    def user_retrieves_invoice_by_customer_and_inv_no(self):
        self.user_retrieves_all_invoice("all")
        invoice = BuiltIn().get_variable_value("${invoice_list}")
        inv_dtl = BuiltIn().get_variable_value("${fixedData}")
        inv_no = inv_dtl['INV_NO']
        for i in range(len(invoice)):
            if invoice[i]["INV_NO"] == inv_no:
                BuiltIn().set_test_variable("${res_bd_invoice_id}", invoice[i]["ID"])
                print(invoice[i]["ID"])
                break

    @keyword("validate amount retrieved ${cond} discount")
    def validate_amount_retrieved_is_correct(self, cond):
        inv_dtl = self.get_invoice_by_id()
        if cond == 'without':
            assert inv_dtl['GRPDISC_AMT'] == 0, "Amount with no discount is incorrect"
        else :
            assert inv_dtl['GRPDISC_AMT'] != 0, "Amount with discount is incorrect"

    @keyword("validate discount details for product ${cond} discount")
    def validate_disc_details_for_prod(self, cond):
        inv_dtl = BuiltIn().get_variable_value("${fixedData}")
        prod_cd = inv_dtl['PROD_CD']
        prod = ProductGet.ProductGet().user_retrieves_prd_by_prd_code(prod_cd)
        BuiltIn().set_test_variable("${res_bd_invoice_prd_id}",prod["ID"])
        self.user_retrieves_invoice_product_by_id()
        prod_dtl = BuiltIn().get_variable_value("${res_inv_prd}")
        print(prod_dtl)
        if cond == 'without':
            assert prod_dtl[0]['GRPDISC_AMT'] is None, "Disc details with no discount is incorrect"
            assert prod_dtl[0]['GRPDISC_ID'] is None, "Disc details with no discount is incorrect"
            assert prod_dtl[0]['DISC_TYPE'] is None, "Disc details with no discount is incorrect"
            assert prod_dtl[0]['APPLY_ON'] is None, "Disc details with no discount is incorrect"
            assert prod_dtl[0]['DISCOUNT'] is None, "Disc details with no discount is incorrect"
        else:
            assert prod_dtl[0]['GRPDISC_AMT'] is not None, "Disc details with discount is incorrect"
            assert prod_dtl[0]['GRPDISC_ID'] is not None, "Disc details with discount is incorrect"
            assert prod_dtl[0]['DISC_TYPE'] is not None, "Disc details with discount is incorrect"
            assert prod_dtl[0]['APPLY_ON'] is not None, "Disc details with discount is incorrect"
            assert prod_dtl[0]['DISCOUNT'] is not None, "Disc details with discount is incorrect"