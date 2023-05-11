import json
import re
import datetime
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "collection" + APP_URL
DATE_FORMAT = "%Y-%m-%d %H:%M:%S.%f"

class ChequeProcessingPost(object):

    def user_retrieves_cheque_by_distributor(self):
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributors/{1}/collection-details".format(END_POINT_URL,dist_id)
        payload = self.payload_cheque()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of collections retrieved are ", len(body_result))
            print(body_result)

            cheque_details = None
            col_id = BuiltIn().get_variable_value("${col_id}")
            for col in body_result:
                if col['COLLECTION_ID'] == col_id:
                    cheque_details = col
                    break
            BuiltIn().set_test_variable("${cheque_details}", cheque_details)

            collection_id = BuiltIn().get_variable_value("${collection_id}")
            if collection_id is not None:
                collection_id = str(BuiltIn().get_variable_value('${collection_id}'))
                collection_id = re.sub(r'(.{8})(.{8})(.{4})(.{4})(.{4})(.{4})', r'\1:\2-\3-\4-\5-\6', collection_id)
                BuiltIn().set_test_variable("${collection_id}", collection_id)
                if len(body_result) > 1:
                    for i in range(len(response.json())):
                        if response.json()[i]["COLLECTION_ID"] == collection_id:
                            BuiltIn().set_test_variable("${cheque_no}", response.json()[i]["CHEQUE_NO"])
                            BuiltIn().set_test_variable("${cheque_id}", response.json()[i]["ID"])
                            break
        print("Status Code : " + str(response.status_code))
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @keyword('user processes cheque as ${status}')
    def user_updates_cheque_status(self, status):
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributors/{1}/saveAndprocessCheques".format(END_POINT_URL, dist_id)
        if status == "Clear" or status == "clear" :
            status= "CL"
        elif status == "Bank In" or status == "bank in":
            status = "BI"
        elif status == "Bounce" or status == "bounce":
            status = "BC"
        else :
            status = "CC"
        payload = self.payload_cheque_processing(status)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print("Status Code : " + str(response.status_code))
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_cheque(self):
        current_date = datetime.datetime.today().strftime('%Y-%m-%d')
        payload = {
            "COLLECTION_FROM_DATE":current_date,
            "COLLECTION_TO_DATE":current_date,
            "STATUS":"All"
        }
        details = BuiltIn().get_variable_value("${filter_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Cheque Filter Payload : ",payload)
        return payload

    def payload_cheque_processing(self, status):
        details = BuiltIn().get_variable_value("${cheque_details}")
        if details is None:
            collection_id = BuiltIn().get_variable_value('${collection_id}')
            cheque_id = BuiltIn().get_variable_value('${cheque_id}')
            cheque_no = BuiltIn().get_variable_value('${cheque_no}')

        else :
            collection_id = details['COLLECTION_ID']
            cheque_id = details['ID']
            cheque_no = details['CHEQUE_NO']

        rand_reason = BuiltIn().get_variable_value('${rand_reason}')
        if status == "CL" or status == "BI" :
            req_process = True
            bounce_reason = None
        elif status == "BC" or status == "CC":
            req_process = False
            bounce_reason = rand_reason

        payload = [{
                "ID": cheque_id,
                "COLLECTION_ID": collection_id,
                "STATUS": status,
                "CHEQUE_NO": cheque_no,
                "REQUIRED_PROCESS": req_process,
                "BOUNCE_REASON_ID": bounce_reason
            }]

        payload = json.dumps(payload)
        print("Payload is :",payload)
        return payload


