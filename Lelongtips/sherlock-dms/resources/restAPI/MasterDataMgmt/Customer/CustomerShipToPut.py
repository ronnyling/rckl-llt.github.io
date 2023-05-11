import secrets

from resources.restAPI.Config.ReferenceData.Country.CountryGet import CountryGet
from resources.restAPI.Config.ReferenceData.Locality.LocalityGet import LocalityGet
from resources.restAPI.Config.ReferenceData.State.StateGet import StateGet
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
import json

from resources.restAPI.MasterDataMgmt.Customer.CustomerShipToGet import CustomerShipToGet

CUST_END_POINT_URL = PROTOCOL + "profile-cust" + APP_URL


class CustomerShipToPut(object):
    SHIPTO_ID = "${shipto_id}"
    DISTRIBUTOR_ID = "${distributor_id}"
    CUSTOMER_ID = "${cust_id}"

    @keyword('user puts customer shipto')
    def user_puts_customer_shipto(self):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        cust_id = BuiltIn().get_variable_value(self.CUSTOMER_ID)
        CustomerShipToGet().user_retrieves_ship_to_details()
        shipto_id = BuiltIn().get_variable_value("${shipto_id}")
        shipto_details = BuiltIn().get_variable_value("${shipto_details}")

        url = "{0}distributors/{1}/customer/{2}/cust-shipto/{3}".format(CUST_END_POINT_URL,
                                                                    dist_id, cust_id, shipto_id)
        common = APIMethod.APIMethod()
        payload = json.dumps(shipto_details)
        response = common.trigger_api_request("PUT", url, payload)
        body_result = response.json()
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        return body_result
