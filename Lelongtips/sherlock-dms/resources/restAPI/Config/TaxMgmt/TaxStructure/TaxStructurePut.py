
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Config.TaxMgmt.TaxStructure.TaxStructurePost import TaxStructurePost
END_POINT_URL = PROTOCOL + "taxation" + APP_URL
ts = TaxStructurePost()

class TaxStructurePut(object):
    @keyword('user edits created tax structure')
    def user_update_tax_structure(self):

        tax_def_id = BuiltIn().get_variable_value("${tax_struct_id}")
        url = "{0}tax-structure/{1}".format(END_POINT_URL, tax_def_id)
        payload = ts.payload_tax_structure('edit')
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)