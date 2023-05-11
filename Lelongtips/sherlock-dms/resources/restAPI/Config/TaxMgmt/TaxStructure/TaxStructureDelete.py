from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import TokenAccess, APIMethod
from resources.restAPI.Config.TaxMgmt.TaxGroup.TaxGroupDelete import TaxGroupDelete
import secrets

TG_DEL = TaxGroupDelete()
END_POINT_URL = PROTOCOL + "taxation" + APP_URL

class TaxStructureDelete(object):
    @keyword('user deletes ${cond} tax structure')
    def user_deletes_tax_structure(self, cond):
        if cond == 'invalid':
            tax_def_id = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(45))
        else:
            tax_def_id = BuiltIn().get_variable_value("${tax_struct_id}")
        url = "{0}tax-structure/{1}".format(END_POINT_URL, tax_def_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user deletes tax structure prerequisite ')
    def user_deletes_created_tax_structure(self):
        other_tax = BuiltIn().get_variable_value("${Others_TG}")
        print("Other tax is :", other_tax)
        if other_tax != '' and other_tax is not None:
            TokenAccess.TokenAccess().user_retrieves_token_access_as("hqadm")
            tg_id = other_tax['ID']
            BuiltIn().set_test_variable("${tax_group_id}", tg_id)
            TG_DEL.user_deletes_tax_group()
            status_code = BuiltIn().get_variable_value(COMMON_KEY.STATUS_CODE)
            assert status_code == 200, "Others Tax Group Deleted Successfully"

        prd_tax = BuiltIn().get_variable_value("${Product_TG}")
        print("Prd tax is", prd_tax)
        if prd_tax != '' and prd_tax is not None:
            TokenAccess.TokenAccess().user_retrieves_token_access_as('distadm')
            tg_id = prd_tax['ID']
            BuiltIn().set_test_variable("${tax_group_id}", tg_id)
            TG_DEL.user_deletes_tax_group()
            status_code = BuiltIn().get_variable_value(COMMON_KEY.STATUS_CODE)
            assert status_code == 200, "Prd Tax Group Deleted Unsuccessful"