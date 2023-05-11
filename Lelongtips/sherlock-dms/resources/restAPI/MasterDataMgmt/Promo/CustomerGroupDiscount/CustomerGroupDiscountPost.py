import json
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from resources.restAPI.MasterDataMgmt.Customer import CustomerGet
from resources.restAPI.MasterDataMgmt.Product import ProductGet
import secrets
import datetime
NOW = datetime.datetime.now()
END_POINT_URL = PROTOCOL + "promotion" + APP_URL
DT_FORMAT = "%Y-%m-%dT00:00:00.000Z"

class CustomerGroupDiscountPost(object):
    DT_FORMAT = "%Y-%m-%dT00:00:00.000Z"

    @keyword('user retrieves customer group discount with ${id_type} customer and product')
    def user_retrieves_customer_group_discount(self, id_type):
        url = "{0}cust-group-discount/customer-product".format(END_POINT_URL)
        payload = self.payload(id_type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
            BuiltIn().set_test_variable("${res_grpdisc}", response.json())
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload(self, id_type):
        if id_type == "invalid":
            cust_id = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(45))
            prod_id =  ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(45))
        else :
            details = BuiltIn().get_variable_value("${discountDetails}")
            cust_name = details['CUST_NAME']
            prod_cd = details['PROD_CD']
            cust_id = (CustomerGet.CustomerGet().user_retrieves_cust_name(cust_name))['ID']
            prod_id = (ProductGet.ProductGet().user_retrieves_prd_by_prd_code(prod_cd))['ID']
        payload = {
            "CUST_ID": cust_id,
            "PRD_ID": [prod_id]
            }
        payload = json.dumps(payload)
        return payload

    def user_creates_customer_group_discount(self):
        url = "{0}cust-group-discount".format(END_POINT_URL)
        payload = self.payload_new()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            body_result = response.json()
            print("Body Result: ", body_result)
            BuiltIn().set_test_variable("${disc_code}", body_result["GRPDISC_CD"])
            BuiltIn().set_test_variable("${res_bd_grpdisc_id}", body_result["ID"])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_new(self):
        days = secrets.choice(range(1000, 5000))
        st_date = str((NOW + datetime.timedelta(days=days)).strftime(DT_FORMAT))
        end_date = str((NOW + datetime.timedelta(days=days+3)).strftime(DT_FORMAT))
        grplevel = "C"
        DistributorGet.DistributorGet().user_gets_distributor_by_using_code('DistEgg')
        CustomerGet.CustomerGet().user_retrieves_all_cust()
        custgrp_lvl_id = BuiltIn().get_variable_value("${rand_cust_id}")
        payload = {
               "ID":None,
               "GRPDISC_CD":None,
               "GRPDISC_DESC":''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
               "REF_NO":''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
               "PRDASSIGN_IND": secrets.choice([True, False]),
               "CUSTGRP_LVL": grplevel,
               "CUSTGRP_VAL_ID":"B3EA05F1:B5D0CECA-B33C-4D26-8DF7-3F612E50E5C5",
               "DISC_TYPE":"P",
               "DISCOUNT":secrets.choice(range(1, 10)),
               "APPLY_ON":"S",
               "CLAIMABLE_IND":False,
               "START_DT": st_date,
               "END_DT": end_date,
               "STATUS": secrets.choice(["A", "I"]),
               "CUSTGRP_LVL_ID": custgrp_lvl_id
            }
        #details = BuiltIn().get_variable_value("${discountDetails}")
        #if details:
        #    payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("CGD Payload", payload)
        return payload