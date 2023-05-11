import secrets

from resources import COMMON_KEY
from resources.hht_api.Setup.SetupGet import SetupGet
from resources.restAPI.Config.ReferenceData.Country.CountryDelete import CountryDelete
from resources.restAPI.Config.ReferenceData.Country.CountryGet import CountryGet
from resources.restAPI.Config.ReferenceData.Country.CountryPost import CountryPost
from resources.restAPI.Config.ReferenceData.Locality.LocalityDelete import LocalityDelete
from resources.restAPI.Config.ReferenceData.Locality.LocalityGet import LocalityGet
from resources.restAPI.Config.ReferenceData.Locality.LocalityPost import LocalityPost
from resources.restAPI.Config.ReferenceData.State.StateDelete import StateDelete
from resources.restAPI.Config.ReferenceData.State.StateGet import StateGet
from resources.restAPI.Config.ReferenceData.State.StatePost import StatePost
from resources.restAPI.MasterDataMgmt.Customer import CustomerDelete
from resources.restAPI.MasterDataMgmt.Customer.CustomerGet import CustomerGet
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from resources.restAPI.MasterDataMgmt.PriceGroup.PriceGroupGet import PriceGroupGet
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
import json
import datetime
from resources.restAPI.Common import TokenAccess
from resources.restAPI.SysConfig.Maintenance.LOB.LobGet import LobGet

CUST_END_POINT_URL = PROTOCOL + "profile-cust" + APP_URL
HIERARCHY_END_POINT_URL = PROTOCOL + "dynamic-hierarchy" + APP_URL


class CustomerPost(object):
    DISTRIBUTOR_ID = "${distributor_id}"
    CUSTOMER_ID = "${cust_id}"
    CUSTOMER_CONTACT_ID = "${contact_id}"
    INVOICE_TERM_ID = "${invoice_term_id}"
    LICNESE_ID = "${license_id}"

    @keyword('user creates customer with random data')
    def user_creates_customer_with(self):
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributors/{1}/customer".format(CUST_END_POINT_URL, dist_id)
        payload = self.payload_customer()
        payload = json.dumps(payload)
        print(payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        assert response.status_code == 200
        body_result = response.json()
        customer_id = body_result['ID']
        print("CUST ID IS {0}".format(customer_id))
        print("response payload = " + str(body_result))
        BuiltIn().set_test_variable("${res_bd_cust_id}", customer_id)
        BuiltIn().set_test_variable("${cust_id}", customer_id)
        BuiltIn().set_test_variable("${distributor_id}", body_result["DIST_ID"])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_customer(self):
        locality_br = LocalityGet().user_gets_all_localities_data_new()
        state_br = StateGet().user_gets_all_states_data_new()
        country_br = CountryGet().user_gets_all_countries_data_new()
        type_cash_id = CustomerGet().user_gets_customer_type("Cash")

        print("cust type = ", str(type_cash_id))
        locality_id = {}
        state_id = {}
        country_id = {}
        cust_type_id = {}

        cust_type_id["ID"] = type_cash_id
        locality_id["ID"] = locality_br[0]['ID']
        state_id["ID"] = state_br[0]['ID']
        country_id["ID"] = country_br[0]['ID']

        locality = BuiltIn().get_variable_value("${locality_details}")
        if locality is None:
            locality = BuiltIn().get_variable_value("${locality}")
        state = BuiltIn().get_variable_value("${state_details}")
        if state is None:
            state = BuiltIn().get_variable_value("${state}")
        country = BuiltIn().get_variable_value("${country_details}")
        if country is None:
            country = BuiltIn().get_variable_value("${country}")
        price_grp = BuiltIn().get_variable_value("${price_grp_details}")
        if price_grp is None:
            PriceGroupGet().user_retrieves_all_price_group()
            price_group_ls = BuiltIn().get_variable_value("${price_group_ls}")
            rand = secrets.choice(price_group_ls)
            price_grp ={}
            price_grp["ID"] = rand['ID']

        payload = {
            "VISION_STORE": secrets.choice([True, False]),
            "ADDRESS_CD": {
                "ADD1": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(10)),
                "ADD2": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(10)),
                "ADD3": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(10)),
                "POST_CD": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(5)),
                "LOCALITY": locality_id,
                "STATE": state_id,
                "COUNTRY": country_id,
            },
            "STATUS": secrets.choice(["Active", "Inactive"]),
            "OPEN_ACC": "2020-07-16",
            "BLOCK": "0",
            "RELATIONSHIP": "0",
            "SUB_DIST": "0",
            "TAX_EXMP": "0",
            "SEASON_CUST": False,
            "CUSTOMER_TRANSFER": secrets.choice([True, False]),
            "CUST_NAME": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(10)),
            "CUST_NAME2": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(10)),
            "TYPE": cust_type_id,
            "GRP_DISC": secrets.choice(["Group1", "Group2", "Group3"]),
            "PRICE_GRP": price_grp,
            "REG_TYPE": secrets.choice(["UR", "R", "C"]),
            "TAX_EXMP_NUM": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(10))
        }
        details = BuiltIn().get_variable_value("${customer_details}")
        if payload["REG_TYPE"] == "R":
            payload.update({"TAX_REG_NUM":''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(10))})
        if details:
            payload.update((k, v) for k, v in details.items())
        return payload

    def user_assign_hierarchy(self):
        customer_id = BuiltIn().get_variable_value("${res_bd_cust_id}")
        if customer_id is None:
            customer_id = BuiltIn().get_variable_value("${cust_id}")
        url = "{0}customer/{1}/nodes".format(HIERARCHY_END_POINT_URL, customer_id)
        payload = self.payload_hierarchy()
        common = APIMethod.APIMethod()
        print("hierarchy payload is {0}".format(payload))
        response = common.trigger_api_request("PUT", url, payload)
        body_result = response.json()
        assert response.status_code == 200
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return body_result

    def payload_hierarchy(self):
        payload = [{
            "END_DATE": "2999-01-01",
            "NODE_ID": "B3EA05F1:5110767D-3A74-49FD-A7F9-341BD1CDF971",
            "START_DATE": (datetime.datetime.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        }]
        payload = json.dumps(payload)
        return payload

    @keyword("set customer prerequisites")
    def set_customer_prerequisites(self):
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        DistributorGet.DistributorGet().user_gets_distributor_by_using_code('DistEgg')
        CountryPost().user_creates_country_as_prerequisite()
        StatePost().user_creates_state_as_prerequisite()
        LocalityPost().user_creates_locality_as_prerequisite()
        TokenAccess.TokenAccess().user_retrieves_token_access_as("hqadm")
        CustomerGet().user_gets_customer_type_with_code("random")
        PriceGroupGet().get_price_group_by_code("random")

    def set_customer_teardown(self):
        TokenAccess.TokenAccess().get_token_by_role("hqadm")
        LocalityDelete().user_deletes_created_locality_as_teardown()
        StateDelete().user_deletes_created_state_as_teardown()
        CountryDelete().user_deletes_created_country_as_teardown()
        TokenAccess.TokenAccess().get_token_by_role("distadm")
        CustomerDelete.CustomerDelete().user_deletes_created_customer_data()

    def user_creates_customer_as_prerequisite(self):
        self.set_customer_prerequisites()
        TokenAccess.TokenAccess().get_token_by_role("distadm")
        self.user_creates_customer_with("random")
        self.user_assign_hierarchy()

    @keyword("user create customer contacts")
    def user_create_customer_contacts(self):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        cust_id = BuiltIn().get_variable_value(self.CUSTOMER_ID)
        url = "{0}distributors/{1}/customer/{2}/customer-contact".format(CUST_END_POINT_URL, dist_id, cust_id)
        common = APIMethod.APIMethod()
        payload = self.payload_customer_contacts()
        response = common.trigger_api_request("POST", url, payload)
        print("payload = " + str(payload))
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${cust_contact_id}", body_result['ID'])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def payload_customer_contacts(self):
        payload = {
                    "CUST_CONTACT_NAME": "my father" + str(secrets.randbelow(9999)),
                    "CUST_CONTACT_POSITION": "father",
                    "CUST_CONTACT_TEL": "0123456789",
                    "CUST_CONTACT_MOBILE": "0123456789"
                }
        payload = json.dumps(payload)
        return payload

    @keyword("user creates customer invoice term")
    def user_creates_customer_invoice_term(self):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        cust_id = BuiltIn().get_variable_value(self.CUSTOMER_ID)
        url = "{0}distributors/{1}/customer/{2}/customer-invoice-terms".format(CUST_END_POINT_URL,
                                                                               dist_id, cust_id)
        common = APIMethod.APIMethod()
        payload = self.payload_invoice_term()
        payload = json.dumps(payload)
        response = common.trigger_api_request("POST", url, payload)
        body_result = response.json()
        print("payload = " + payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${invoice_term_id}", body_result['ID'])
            body_result = response.json()
        return body_result

    def payload_invoice_term(self):
        CustomerGet().user_gets_customer_invoice_term_list()
        SetupGet().get_setting_invoice_term("")
        LobGet().user_retrieves_lob(True)
        current_invoice_term = BuiltIn().get_variable_value("${curr_invoice_term_ls}")
        invoice_term_ls = BuiltIn().get_variable_value("${invoice_term_ls}")
        lob_ls = BuiltIn().get_variable_value("${lob_reponse_body}")
        used_lob = []
        used_inv_term = []
        if current_invoice_term is not None:
            for inv_term in current_invoice_term:
                used_lob.append(inv_term['LOB_ID']['ID'])
                used_inv_term.append(inv_term['INVTERM_CD']['ID'])
            for lob in lob_ls:
                if lob not in used_lob:
                    lob_id = lob['ID']
            for inv_term in invoice_term_ls:
                if inv_term not in used_inv_term:
                    inv_term_id = inv_term['ID']
        elif invoice_term_ls is not None and lob_ls is not None:
            lob_id = lob_ls[0]['ID']
            inv_term_id = invoice_term_ls[0]['ID']
        BuiltIn().set_test_variable("${invoice_term_id}", inv_term_id)

        payload = {
            "LOB_ID": {
                "ID": lob_id
            },
            "INVTERM_CD": {
                "ID": inv_term_id
            }
        }
        return payload