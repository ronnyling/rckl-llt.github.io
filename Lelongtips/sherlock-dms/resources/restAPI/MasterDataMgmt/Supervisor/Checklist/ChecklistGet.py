import secrets
from resources.restAPI import PROTOCOL, APP_URL,COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from datetime import datetime
END_POINT_URL = PROTOCOL + "customer-transfer" + APP_URL

class ChecklistGet(object):


    @keyword('user retrieves all checklists')
    def user_retrieves_all_checklists(self):
        url = "{0}supervisor-checklist".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            respond_len = len(response.json())
            for i in range(respond_len):
                start_date_str = response.json()[i]['START_DT']
                if start_date_str != None:
                    start_date_obj = datetime.strptime(response.json()[i]['START_DT'], '%Y-%m-%d')
                    print('start obj', start_date_obj)
                    if start_date_obj < datetime.now():
                        past_date = True
                        past_checklist_cd = response.json()[i]['CHECKLIST_CD']
                        past_checklist_id = response.json()[i]['ID']
                        break
                    else:
                        past_date = False
                        past_checklist_id = ''
            BuiltIn().set_test_variable("${past_date}", past_date)
            BuiltIn().set_test_variable("${past_checklist_cd}", past_checklist_cd)
            BuiltIn().set_test_variable("${past_checklist_id}", past_checklist_id)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves checklist using ${type} id')
    def user_gets_checklist_by_id(self, type):
        if type == "invalid":
            res_bd_checklist_id = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(45))
        else:
            res_bd_checklist_id = BuiltIn().get_variable_value("${res_bd_checklist_id}")
        url = "{0}supervisor-checklist/{1}".format(END_POINT_URL, res_bd_checklist_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            assert res_bd_id == res_bd_checklist_id, "ID retrieved not matched"
            return body_result

