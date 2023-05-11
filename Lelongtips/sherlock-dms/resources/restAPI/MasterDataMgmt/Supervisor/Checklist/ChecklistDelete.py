import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.MasterDataMgmt.Supervisor.Checklist import ChecklistGet

END_POINT_URL = PROTOCOL+"customer-transfer"+APP_URL


class ChecklistDelete(object):

    @keyword('user deletes created checklist using ${type} id')
    def user_deletes_checklist(self, type):
        if type == "valid":
            res_bd_checklist_id = BuiltIn().get_variable_value("${res_bd_checklist_id }")
        elif type == "past start date":
            ChecklistGet.ChecklistGet.user_retrieves_all_checklists(self)
            res_bd_checklist_id = BuiltIn().get_variable_value("${past_checklist_id}")
        else:
            res_bd_checklist_id = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(45))
        url = "{0}supervisor-checklist/{1}".format(END_POINT_URL, res_bd_checklist_id )
        response = APIMethod.APIMethod().trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)


