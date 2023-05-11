import json
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.MasterDataMgmt.Customer import CustomerGet
from resources.restAPI.MasterDataMgmt.Product import ProductGet
import secrets
END_POINT_URL = PROTOCOL + "promotion" + APP_URL

class CustomerGroupDiscountGet(object):

    @keyword('user gets all customer group disc')
    def user_gets_all_customer_group_discount(self):
        url = "{0}cust-group-discount".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
            if len(body_result) > 1:
                rand_so = secrets.randbelow(len(body_result))
            else:
                rand_so = 0
            BuiltIn().set_test_variable("${res_bd_grpdisc_id}", body_result[rand_so]["ID"])
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_gets_customer_group_disc_by_id(self):
        res_bd_grpdisc_id = BuiltIn().get_variable_value("${res_bd_grpdisc_id}")
        url = "{0}cust-group-discount/{1}".format(END_POINT_URL, res_bd_grpdisc_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            assert res_bd_id == res_bd_grpdisc_id, "ID retrieved not matched"
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return body_result

