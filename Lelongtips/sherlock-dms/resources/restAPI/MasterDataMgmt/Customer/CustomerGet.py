import secrets
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL, BuiltIn, COMMON_KEY
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
import json

from resources.restAPI.MasterDataMgmt.Customer.CustomerOptionGet import CustomerOptionGet

CUST_END_POINT_URL = PROTOCOL + "profile-cust" + APP_URL
MERCHANDISING_END_POINT_URL = PROTOCOL + "merchandising" + APP_URL
METADATA_END_POINT_URL = PROTOCOL + "metadata" + APP_URL

class CustomerGet(object):
    DISTRIBUTOR_ID = "${distributor_id}"
    CUSTOMER_ID = "${cust_id}"
    CUSTOMER_CONTACT_ID = "${contact_id}"
    SHIPTO_ID = "${shipto_id}"
    INVOICE_TERM_ID = "${invoice_term_id}"
    LICNESE_ID = "${license_id}"

    def user_retrieves_all_cust(self):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        url = "{0}distributors/{1}/customer".format(CUST_END_POINT_URL, dist_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        body_result = response.json()
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        return body_result

    @keyword("user retrieves cust by using name '${cust}'")
    def user_retrieves_cust_name(self, cust):
        filter_cust = {"FILTER": {"CUST_NAME": {"$eq": cust}}}
        filter_cust = json.dumps(filter_cust)
        str(filter_cust).encode(encoding='UTF-8', errors='strict')
        url = "{0}distributors/1/customer?filter={1}".format(CUST_END_POINT_URL, filter_cust)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve cx"
        body_result = response.json()
        cust_id = body_result[0]['ID']
        pg_id = body_result[0]['PRICE_GRP']
        BuiltIn().set_test_variable(self.CUSTOMER_ID, cust_id)
        BuiltIn().set_test_variable("${pg_id}", pg_id)
        return body_result[0]

    def user_retrieves_cust_by_id(self):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        cust_id = BuiltIn().get_variable_value("${res_bd_cust_id}")
        url = "{0}distributors/{1}/customer/{2}".format(CUST_END_POINT_URL, dist_id, cust_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            BuiltIn().set_test_variable("${cust_details}", response.json())
        assert response.status_code == 200, "Unable to retrieve cx"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body_result = response.json()
        return body_result

    @keyword("user gets cust by using code '${cust_cd}'")
    def user_gets_cust_by_using_code(self, cust_cd):
        """ Functions to retrieve cust id by using cust code """
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        filter_cust = {"FILTER": {"CUST_CD":{"$eq":cust_cd}}}
        filter_cust = json.dumps(filter_cust)
        str(filter_cust).encode(encoding='UTF-8', errors='strict')
        url = "{0}distributors/{1}/customer?filter={2}".format(CUST_END_POINT_URL, dist_id, filter_cust)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve Cust"
        body_result = response.json()
        cust_id = body_result[0]['ID']
        cust_name = body_result[0]['CUST_NAME']
        pg_id = body_result[0]['PRICE_GRP']
        BuiltIn().set_test_variable("${cust_id}", cust_id)
        cust_opt = CustomerOptionGet().user_retrieves_cust_option()
        np_pg_id = cust_opt['NON_PRIME_PRICE_GRP']
        BuiltIn().set_test_variable(self.CUSTOMER_ID, cust_id)
        BuiltIn().set_test_variable("${cust_name}", cust_name)
        BuiltIn().set_test_variable("${cust_cd}", cust_cd)
        BuiltIn().set_test_variable("${pg_id}", pg_id)
        BuiltIn().set_test_variable("${np_pg_id}", np_pg_id)
        BuiltIn().set_test_variable("${cust_body_result}", body_result)

    @keyword("user gets customer shipto by desc '${shipto_desc}'")
    def user_gets_customer_shipto_by_desc(self, shipto_desc):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        cust_id = BuiltIn().get_variable_value(self.CUSTOMER_ID)
        filter_shipto = {"SHIPTO_DESC": {"$eq": shipto_desc}}
        filter_shipto = json.dumps(filter_shipto)
        url = "{0}distributors/{1}/customer/{2}/cust-shipto?filter={3}".format(CUST_END_POINT_URL,
                                                                               dist_id, cust_id, filter_shipto)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve ShipTo"
        body_result = response.json()
        shipto_id = body_result[0]['ID']
        BuiltIn().set_test_variable("${shipto_id}", shipto_id)

    @keyword("user gets customer POSM products with ID")
    def user_gets_customer_posm_products(self):
        customer_id = BuiltIn().get_variable_value("${res_bd_cust_id}")
        filterstring = '{"FIELDS":["ID","MODIFIED_DATE","PROD_CD","PROD_DESC","QTY","UOM_CD"],"FILTER":[]}'
        url = '{0}customer/{1}/customer-posm?filter={2}'.format(CUST_END_POINT_URL, customer_id, filterstring)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword("user gets customer type with code ${code}")
    def user_gets_customer_type_with_code(self, code):
        if code != "random":
            filter_custype = {"CUST_TYPE_CD": {"$eq": code}}
        else:
            filter_custype = {}
        filter_custype= json.dumps(filter_custype)
        url = "{0}module-data/customer-type?filter={1}".format(METADATA_END_POINT_URL, filter_custype)
        print ("Cust_type url {0}".format(url))
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve cusType"
        body_result = response.json()
        if code == "random":
            x = secrets.choice([0,1])
            BuiltIn().set_test_variable("${cust_type}", body_result[x])
            return body_result[x]
        else:
            BuiltIn().set_test_variable("${cust_type}", body_result[0])
            return body_result[0]

    @keyword("user gets customer contacts")
    def user_gets_customer_contacts(self):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        cust_id = BuiltIn().get_variable_value(self.CUSTOMER_ID)
        url = "{0}distributors/{1}/customer/{2}/customer-contact".format(CUST_END_POINT_URL, dist_id, cust_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            if len(body_result) > 1:
                rand_so = secrets.randbelow(len(body_result))
            else:
                rand_so = 0
            BuiltIn().set_test_variable("${contact_id}", body_result[rand_so]["ID"])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword("user retrieve customer code")
    def user_get_cust_cd(self):
        response = self.user_retrieves_cust_by_id()
        customer_cd = response["CUST_CD"]
        print("CUSTOMER CD IS: ", customer_cd)
        BuiltIn().set_test_variable("${CUSTOMER_CD}", customer_cd)

    @keyword("user gets customer contacts details")
    def user_gets_customer_contacts_details(self):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        cust_id = BuiltIn().get_variable_value(self.CUSTOMER_ID)
        cust_contact_id = BuiltIn().get_variable_value(self.CUSTOMER_CONTACT_ID)
        url = "{0}distributors/{1}/customer/{2}/customer-contact/{3}".format(CUST_END_POINT_URL, dist_id, cust_id, cust_contact_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
        # if response.status_code == 204:
        #     user_create_customer_contacts
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword("user gets customer shipto all")
    def user_gets_customer_shipto_all(self):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        cust_id = BuiltIn().get_variable_value(self.CUSTOMER_ID)
        extension = '?filter={%22FIELDS%22:[%22ID%22,%22MODIFIED_DATE%22,%22SHIPTO_CD%22,%22SHIPTO_DESC%22,%22CONT_PERSON%22,%22CONT_NO%22,%22DEFAULT_SHIPTO%22],%22FILTER%22:[]}&silent=null'
        url = "{0}distributors/{1}/customer/{2}/cust-shipto{3}".format(CUST_END_POINT_URL,
                                                                               dist_id, cust_id, extension)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200 or response.status_code == 204, "Unable to retrieve ShipTo"
        body_result = response.json()
        shipto_id = body_result[0]['ID']
        BuiltIn().set_test_variable("${shipto_id}", shipto_id)

    @keyword("user gets customer shipto details")
    def user_gets_customer_shipto_details(self):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        cust_id = BuiltIn().get_variable_value(self.CUSTOMER_ID)
        shipto_id = BuiltIn().get_variable_value(self.SHIPTO_ID)
        url = "{0}distributors/{1}/customer/{2}/cust-shipto/{3}".format(CUST_END_POINT_URL,
                                                                               dist_id, cust_id, shipto_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve ShipTo details"
        body_result = response.json()
        return body_result

    @keyword("user gets customer invoice term list")
    def user_gets_customer_invoice_term_list(self):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        cust_id = BuiltIn().get_variable_value(self.CUSTOMER_ID)
        extension = '?filter={%22FIELDS%22:[%22ID%22,%22MODIFIED_DATE%22,%22LOB_ID.LOB_DESC%22,%22INVTERM_CD.TERMS_DESC%22],%22FILTER%22:[]}&silent=null'
        url = "{0}distributors/{1}/customer/{2}/customer-invoice-terms{3}".format(CUST_END_POINT_URL,
                                                                               dist_id, cust_id, extension)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${invoice_term_id}", response.json()[0]['ID'])
            BuiltIn().set_test_variable("${curr_invoice_term_ls}", response.json())
            body_result = response.json()
        return response.status_code

    @keyword("user gets customer invoice term details")
    def user_gets_customer_invoice_term_details(self):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        cust_id = BuiltIn().get_variable_value(self.CUSTOMER_ID)
        invoice_term_id = BuiltIn().get_variable_value(self.INVOICE_TERM_ID)
        url = "{0}distributors/{1}/customer/{2}/customer-invoice-terms/{3}".format(CUST_END_POINT_URL,
                                                                               dist_id, cust_id, invoice_term_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        body_result = response.json()
        return body_result

    @keyword("user retrieve customer open items")
    def user_retrives_customer_open_items(self):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        cust_id = BuiltIn().get_variable_value(self.CUSTOMER_ID)
        url = "{0}distributors/{1}/customer/{2}/customer-open-items".format(CUST_END_POINT_URL,
                                                                               dist_id, cust_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        body_result = response.json()
        return body_result

    @keyword("user retrieve customer order status")
    def user_retrives_customer_order_status(self):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        cust_id = BuiltIn().get_variable_value(self.CUSTOMER_ID)
        url = "{0}distributors/{1}/customer/{2}/order-status".format(CUST_END_POINT_URL,
                                                                               dist_id, cust_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        body_result = response.json()
        return body_result

    @keyword("user retrieve customer license")
    def user_retrives_customer_license(self):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        cust_id = BuiltIn().get_variable_value(self.CUSTOMER_ID)
        extension = "?filter={%22FIELDS%22:[%22ID%22,%22MODIFIED_DATE%22,%22LIC_CD%22,%22LIC_NUM%22,%22START_DT%22,%22END_DT%22,%22CREATION_DATE%22],%22FILTER%22:[]}&silent=null"
        url = "{0}distributors/{1}/customer/{2}/customer-license{3}".format(CUST_END_POINT_URL,
                                                                               dist_id, cust_id, extension)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        BuiltIn().set_test_variable("${license_id}", response.json()[0]['ID'])
        body_result = response.json()
        return body_result

    @keyword("user retrieve customer license details")
    def user_retrives_customer_license_details(self):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        cust_id = BuiltIn().get_variable_value(self.CUSTOMER_ID)
        license_id = BuiltIn().get_variable_value(self.LICNESE_ID)
        url = "{0}distributors/{1}/customer/{2}/customer-license/{3}".format(CUST_END_POINT_URL,
                                                                               dist_id, cust_id, license_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().get_variable_value(self.LICNESE_ID)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        body_result = response.json()
        return body_result

    @keyword("user gets customer posm listing")
    def user_gets_customer_posm_listing(self):
        cust_id = BuiltIn().get_variable_value(self.CUSTOMER_ID)
        url = "{0}customer/{1}/customer-posm".format(CUST_END_POINT_URL, cust_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        body_result = response.json()
        return

    @keyword("user gets customer trade asset listing")
    def user_gets_customer_trade_asset_listing(self):
        cust_id = BuiltIn().get_variable_value(self.CUSTOMER_ID)
        url = "{0}customer/{1}/asset-master".format(MERCHANDISING_END_POINT_URL, cust_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        body_result = response.json()
        return body_result

    def user_retrieves_random_cust(self):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        url = "{0}distributors/{1}/customer".format(CUST_END_POINT_URL, dist_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        body_result = response.json()
        if response.status_code == 200:
            rand = secrets.choice(body_result)
            cust_id = rand['ID']
            BuiltIn().set_test_variable("${cust_id}", cust_id)
            BuiltIn().set_test_variable("${res_bd_cust_id}", cust_id)
        self.user_retrieves_cust_by_id()
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        return body_result

    @keyword("user retrieve customer order status")
    def user_retrives_customer_order_status(self):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        cust_id = BuiltIn().get_variable_value(self.CUSTOMER_ID)
        url = "{0}distributors/{1}/customer/{2}/order-status".format(CUST_END_POINT_URL,
                                                                               dist_id, cust_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        body_result = response.json()
        return body_result

    @keyword("user gets random customer type")
    def user_gets_random_customer_type(self):
        url = "{0}module-data/customer-type".format(METADATA_END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${cust_type}", response.json())
        return response.json()

    @keyword("user gets fixed customer type ${cust_type_desc}")
    def user_gets_customer_type(self, cust_type_desc):
        url = "{0}module-data/customer-type".format(METADATA_END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        cust_type_ls = response.json()
        if response.status_code == 200:
            for cust_type in cust_type_ls:
                if cust_type['CUST_TYPE_DESC'] == cust_type_desc:
                    return cust_type['ID']
            BuiltIn().set_test_variable("${cust_type}", response.json())
        return response.json()
