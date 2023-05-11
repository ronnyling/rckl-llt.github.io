import json
import secrets
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "vs-scorecard" + APP_URL


class VSKpiTypePost(object):

    @keyword("user creates kpi type using ${data_type} data")
    def user_creates_kpi_type_using_data(self, data_type):
        url = "{0}vs-kpi-type".format(END_POINT_URL)
        print(url)
        common = APIMethod.APIMethod()
        payload = self.payload_kpi_type("create")
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 201:
            res_bd_kpi_id = response.json()['ID']
            res_bd_kpi_cd = response.json()['KPI_TYPE_CODE']
            BuiltIn().set_test_variable("${res_bd_kpi_id}", res_bd_kpi_id)
            BuiltIn().set_test_variable("${res_bd_kpi_cd}", res_bd_kpi_cd)
        try:
            data = response.json()
            return data['ID'], str(response.status_code),  data['ROLE']['NAME']
        except Exception as e:
            print(e.__class__, "occured")
            return " ", str(response.status_code), print(response.text)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_kpi_type(self, action):
        if action == 'update':
            kpi_type_code = BuiltIn().get_variable_value("${res_bd_kpi_cd}")
        else :
            kpi_type_code = "".join(secrets.choice('gydurfc') for _ in range(5))
        payload = {
            'KPI_TYPE_CODE': kpi_type_code,
            "KPI_TYPE_DESC": f'qa{fake.word()}{fake.word()}halo',
            "TYPE": 'VSSC',
            "CHART_COLOR": 'blank',
        }
        details = BuiltIn().get_variable_value("${vskpitype_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print(payload)
        return payload
