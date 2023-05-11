import secrets

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.MasterDataMgmt.Customer import CustomerGet
fake = Faker()


END_POINT_URL = PROTOCOL + "customer-transactions" + APP_URL


class OutletNotePut(object):

    @keyword("user updates ${data_type} outlet note")
    def user_retrieves_outlet_note(self, data_type):
        note_id = '00000000C765B1A897D249DE82D9F01437D749E1'
        url = "{0}outletnote/{1}".format(END_POINT_URL, note_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return str(response.status_code), response.json()



