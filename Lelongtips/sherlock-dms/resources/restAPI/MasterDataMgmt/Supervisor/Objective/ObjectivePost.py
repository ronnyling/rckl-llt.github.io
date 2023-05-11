import json, secrets, datetime
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from setup.hanaDB import HanaDB
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.MasterDataMgmt.Supervisor.WorkPlan import WorkPlanGet
from resources.restAPI.Common import APIMethod
NOW = datetime.datetime.now()
END_POINT_URL = PROTOCOL + "customer-transfer" + APP_URL


class ObjectivePost(object):
    DT_FORMAT = "%Y-%m-%d"

    @keyword("user creates supervisor objective with ${cond} data")
    def user_creates_objective_with_data(self, cond):
        """ Function to create objective """
        payload = self.objective_payload()
        print("payload", payload)
        url = "{0}supervisor-objective".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            body_result = response.json()
            print("testing", body_result)
            BuiltIn().set_test_variable("${objective_id}", body_result['ID'])
            BuiltIn().set_test_variable("${objective_cd}", body_result['OBJECTIVE_CD'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)


    def objective_payload(self):
        work_plan = WorkPlanGet.WorkPlanGet().get_random_work_plan_by_field_and_value("FEEDBACK_REQUIRED", "true")
        a_type = secrets.choice(['AC', 'ME'])
        if a_type == 'AC':
            kpi = secrets.choice(['MSLC', 'SV'])
        else:
            kpi = None
        payload = {
            "ACHIEVEMENT_TYPE": a_type,
            "STATUS": secrets.choice(['A', 'I']),
            "OBJECTIVE_CD": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20)),
            "OBJECTIVE_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(15)),
            "OBJECTIVE_TARGET": 1,
            "WORK_PLAN_ITEM": [work_plan],
            "START_DT": str((NOW + datetime.timedelta(days=1)).strftime(self.DT_FORMAT)),
            "END_DT":  str((NOW + datetime.timedelta(days=1000)).strftime(self.DT_FORMAT)),
            "KPI": kpi
        }
        objective_details = BuiltIn().get_variable_value("${objective_details}")
        if objective_details:
            payload.update((k, v) for k, v in objective_details.items())
        BuiltIn().set_test_variable("${payload_objective}", payload)
        payload = json.dumps(payload)
        return payload

    @keyword("user update objective ${cond} date to ${value}")
    def update_objective_date(self, start_or_end, date):
        if start_or_end == 'start':
            field_id = '551282318D9559C753954104BDCEBA6B7C1D9F66'
        else:
            field_id = '55128231D3D2F0A6E5BC4989AFD23551967CC962'
        objective_id = BuiltIn().get_variable_value("${objective_id}")
        objective_id = objective_id.replace(":", "")
        objective_id = objective_id.replace("-", "")
        query = "SELECT CAST(ROW_ID as varchar) FROM MODULE_DATA_FIELDS R INNER JOIN METADATA_FIELD F\
                           ON R.FIELD_ID = F.ID WHERE R.ROW_ID IN (SELECT ROW_ID FROM MODULE_DATA_FIELDS R\
                           INNER JOIN METADATA_FIELD F ON R.FIELD_ID = F.ID INNER JOIN MODULE_DATA_ROWS D\
                           ON D.MODULE_ID = F.MODULE_ID WHERE F.MODULE_ID= (SELECT ID FROM METADATA_MODULE WHERE\
                            LOGICAL_ID='supervisor-objective' AND FIELD_ID='{0}' AND IS_DELETED=false)\
                           AND R.ROW_ID LIKE '%{1}%' AND D.IS_DELETED=false GROUP BY ROW_ID)".format(field_id, objective_id)
        HanaDB.HanaDB().connect_database_to_environment()
        row_details = HanaDB.HanaDB().fetch_one_record(query)
        print("db record", row_details)
        update_query = "UPDATE MODULE_DATA_FIELDS \
        SET FIELD_VALUE = '{0}'\
        WHERE FIELD_ID ='{1}'\
        AND ROW_ID ='{2}'".format(date, field_id, row_details)
        HanaDB.HanaDB().execute_sql_string(update_query)
        HanaDB.HanaDB().disconnect_from_database()
