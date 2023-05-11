import json
import datetime
import secrets

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod, TokenAccess, APIAssertion
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Config.ReferenceData.PlaybookType.PlaybookTypeGet import PlaybookTypeGet
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure.StructureGet import StructureGet
from resources.restAPI.Config.DynamicHierarchy.ProductCustomerHierarchy.ValueGet import ValueGet
from resources.restAPI.Config.AppSetup.AppSetupGet import AppSetupGet
from setup.hanaDB import HanaDB
from pathlib import Path
import logging

current_date = datetime.datetime.now()
END_POINT_URL = PROTOCOL + "message" + APP_URL
OBJ_STORE_ENDPOINT_URL = PROTOCOL + "objectstore" + APP_URL
PRD_HIER_END_POINT_URL = PROTOCOL + "dynamic-hierarchy" + APP_URL
prd_hier_url = "{0}structure/hier".format(PRD_HIER_END_POINT_URL)
start_date = str((current_date + datetime.timedelta(days=2)).strftime("%Y-%m-%d"))
end_date = str((current_date + datetime.timedelta(days=45)).strftime("%Y-%m-%d"))
image_file_type = [
    "jpeg",
    "jpg",
    "png",
    "svg"
]
max_thumbnail_size = 500
thumbnail_path = 'playbk-setup/ATTACHMENT/'
b_res = "${body_result}"

class DigitalPlaybookPost(object):
    """ Functions to create playbook """

    @keyword('user creates playbook with ${type} data')
    def user_creates_playbook_with(self, type):
        """ Function to create playbook with random/fixed data"""
        url = "{0}playbk-setup".format(END_POINT_URL)
        general_payload = self.get_general_payload(type)
        content_assignment = []
        content_payload = self.get_content_payload()
        content_assignment.append(content_payload)
        payload = self.payload_playbook(type, general_payload, content_assignment)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            # HanaDB.HanaDB().connect_database_to_environment()
            # HanaDB.HanaDB().user_validates_database_data("playbk-setup", body_result['GENERAL_INFO'])
            # HanaDB.HanaDB().disconnect_from_database()
            BuiltIn().set_test_variable("${playbook_id}", body_result['GENERAL_INFO']['ID'])
            BuiltIn().set_test_variable("${playbk_cd}", body_result['GENERAL_INFO']['PLAYBK_CD'])
            BuiltIn().set_test_variable("${playbk_ass_to}", body_result['GENERAL_INFO']['PLAYBK_ASSIGN_TO'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @keyword('validates content file length saved')
    def validates_content_file_length(self):
        pb_id = BuiltIn().get_variable_value("${playbook_id}")
        pb_id = COMMON_KEY.convert_id_to_string(pb_id)
        HanaDB.HanaDB().connect_database_to_environment()
        query = "select FILE_LENGTH from PLAYBK, PLAYBK_CT_ASS, PLAYBK_CT where PLAYBK.ID = PLAYBK_CT_ASS.PLAYBK_ID AND " \
                "PLAYBK_CT_ASS.CONTENT_ID = PLAYBK_CT.ID AND PLAYBK.ID = '{0}'".format(pb_id)
        file_length = HanaDB.HanaDB().fetch_one_record(query)
        HanaDB.HanaDB().disconnect_from_database()
        assert file_length != "NULL", "File Length is not saved"

    def get_general_payload(self, type):
        StructureGet().user_get_hierid_from_hierarchy_structure_name("General Product Hierarchy")
        hier_structure_details = StructureGet().user_get_hierarchy_structure_info_by_hierarchy_id()
        hier_id = hier_structure_details['hierId']
        AppSetupGet().user_retrieves_details_of_application_setup()
        body_res = BuiltIn().get_variable_value(b_res)
        tree_id = body_res['PLAYBK_PROD_HIERARCHY_LEVEL']
        BuiltIn().set_test_variable("${tree_id}", tree_id)
        ValueGet().get_all_values_from_hierarchy_tree()
        node_id = ValueGet().get_value_by_random_data()

        general_payload = self.set_general_payload(hier_id, tree_id, node_id)
        if type == 'existing':
            general_payload['PLAYBK_DESC'] = BuiltIn().get_variable_value("${playbook_desc}")

        general_details = BuiltIn().get_variable_value("${playbook_general_details}")
        if type == 'fixed' and general_details:
            if 'PLAYBOOK_TYPE_CODE' in general_details.keys():
                general_payload['PLAYBK_TYPE_ID'] = PlaybookTypeGet().user_gets_playbook_type_by_using_field("PLAYBOOK_TYPE_CD", general_details['PLAYBOOK_TYPE_CODE'])
            if 'PRODUCT_HIERARCHY_DESCRIPTION' in general_details.keys():
                StructureGet().user_get_hierid_from_hierarchy_structure_name(general_details['PRODUCT_HIERARCHY_DESCRIPTION'])
                hier_structure_details = StructureGet().user_get_hierarchy_structure_info_by_hierarchy_id()
                hier_id = hier_structure_details['hierId']
                AppSetupGet().user_retrieves_details_of_application_setup()
                body_res = BuiltIn().get_variable_value(b_res)
                tree_id = body_res['PLAYBK_PROD_HIERARCHY_LEVEL']
                BuiltIn().set_test_variable("${tree_id}", tree_id)
                ValueGet().get_all_values_from_hierarchy_tree()
                node_id = ValueGet().get_value_by_random_data()
                general_payload['PRD_HIER_ID'] = hier_id
                general_payload['PRDCAT_ID'] = tree_id
                general_payload['PRDCAT_VALUE_ID'] = node_id
            general_payload.update((k, v) for k, v in general_details.items())
        return general_payload

    def set_general_payload(self, hier_id, tree_id, node_id):
        rand_thumbnail = self.get_objectstore_attachment()
        thumbnail_file_name = rand_thumbnail['Key'].replace(thumbnail_path, '')
        thumbnail_file_type = self.get_file_type_by_key(thumbnail_file_name, "thumbnail")
        thumbnail_file_size = rand_thumbnail['Size']
        thumbnail_file_url = rand_thumbnail['Key']
        general_payload = {
            "PLAYBK_CD": ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "PLAYBK_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20)),
            "PRIORITY": secrets.choice(["H", "M", "L"]),
            "PLAYBK_TYPE_ID": PlaybookTypeGet().user_gets_playbook_type_by_using_field("PLAYBOOK_PRD_HIER_REQ", "0"),
            "PLAYBK_ASSIGN_TO": secrets.choice(["C", "R"]),
            "PRD_HIER_ID": hier_id,
            "PRDCAT_ID": tree_id,
            "PRDCAT_VALUE_ID": node_id,
            "START_DATE": start_date,
            "END_DATE": end_date,
            "THUMBNAIL_FILE_NAME": thumbnail_file_name,
            "THUMBNAIL_FILE_TYPE": thumbnail_file_type,
            "THUMBNAIL_FILE_SIZE": thumbnail_file_size,
            "THUMBNAIL_URL": thumbnail_file_url,
            "STATUS": secrets.choice([True, False])
        }
        return general_payload

    def get_file_type_by_key(self, key, type):
        array = key.split(".")
        file_type = array[len(array)-1]
        if type == "content":
            if file_type == "mp4":
                file_type = "video/" + file_type
            elif file_type in image_file_type:
                file_type = "image/" + file_type
            elif file_type == "ppt":
                file_type = "application/vnd.ms-powerpoint"
            elif file_type == "pdf":
                file_type = "application/" + file_type
        return file_type

    def get_content_payload(self):
        rand_content = self.get_objectstore_attachment()
        ct_file_name = rand_content['Key'].replace(thumbnail_path, '')
        ct_file_size = str(rand_content['Size'])[:-3]
        ct_file_type = self.get_file_type_by_key(ct_file_name, "content")
        if ct_file_type == 'application/pdf' or ct_file_type.startswith('video'):
            ct_file_length = str(secrets.randbelow(30))
        else:
            ct_file_length = None
        ct_file_url = "/objectstore-svc/api/v1.0/storage/playbook_content/ATTACHMENT/" + ct_file_name

        rand_thumbnail = self.get_objectstore_attachment()
        thumbnail_file_name = rand_thumbnail['Key'].replace(thumbnail_path, '')
        thumbnail_file_type = self.get_file_type_by_key(thumbnail_file_name, "thumbnail")
        thumbnail_file_size = rand_thumbnail['Size']
        thumbnail_file_url = rand_thumbnail['Key']

        content_payload = {
            "CONTENT_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "THUMBNAIL_FILE_NAME": thumbnail_file_name,
            "THUMBNAIL_FILE_TYPE": thumbnail_file_type,
            "THUMBNAIL_FILE_SIZE": thumbnail_file_size,
            "THUMBNAIL_URL": thumbnail_file_url,
            "CONTENT_ATTACHMENT": {
                "FILE_NAME": ct_file_name,
                "FILE_SIZE": ct_file_size,
                "FILE_TYPE": ct_file_type,
                "FILE_LENGTH": ct_file_length,
                "URL": ct_file_url
            }
        }

        content_details = BuiltIn().get_variable_value("${playbook_content_details}")
        if content_details:
            if 'ATTACHMENT_FILE_NAME' in content_details.keys():
                content_payload['CONTENT_ATTACHMENT']['FILE_NAME'] = content_details['ATTACHMENT_FILE_NAME']
            if 'ATTACHMENT_FILE_SIZE' in content_details.keys():
                content_payload['CONTENT_ATTACHMENT']['FILE_SIZE'] = content_details['ATTACHMENT_FILE_SIZE']
            if 'ATTACHMENT_FILE_TYPE' in content_details.keys():
                content_payload['CONTENT_ATTACHMENT']['FILE_TYPE'] = content_details['ATTACHMENT_FILE_TYPE']
            if 'ATTACHMENT_FILE_LENGTH' in content_details.keys():
                content_payload['CONTENT_ATTACHMENT']['FILE_LENGTH'] = content_details['ATTACHMENT_FILE_LENGTH']
            if 'ATTACHMENT_URL' in content_details.keys():
                content_payload['CONTENT_ATTACHMENT']['URL'] = content_details['ATTACHMENT_URL']
            content_payload.update((k, v) for k, v in content_details.items())
        return content_payload

    def get_objectstore_attachment(self):
        """ Function to retrieve all objectstore attachment """
        url = "{0}storage/playbk-setup/ATTACHMENT".format(OBJ_STORE_ENDPOINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            if len(body_result) > 1:
                rand_so = secrets.randbelow(len(body_result))
            else:
                rand_so = 0
        return body_result[rand_so]

    @keyword('user uploads ${type} file with ${size} size to object store')
    def upload_file_to_object_store(self, type, size):
        base_path = Path(__file__).parent.parent.parent.parent.parent.parent
        base_path = str(base_path).replace("\\", "//")
        file_path = base_path + "//setup//testdata//PlaybookContent//"
        url = "https://objectstore-svc-intg.cfapps.jp10.hana.ondemand.com/api/v1.0/storage/playbook_content" \
              "/ATTACHMENT?appSetup=PLAYBK_MAX_CONTENT_SIZE"
        max_size = self.get_max_playbook_content_file_size()
        max_size = int(max_size)
        print("Max size: ", max_size)
        if type == 'valid':
            if size == 'valid':
                file = self.get_file_with_valid_size(max_size)
            elif size == 'invalid':
                file = self.get_file_with_invalid_size(max_size)
        else:
            file = 'images.jfif'

        print("file: ", file)
        file_path = file_path + file
        files = [
            ('', (file,
                  open(file_path, 'rb'),
                  'application/octet-stream'))
        ]
        print("files: ", files)
        BuiltIn().set_test_variable("${files}", files)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, "")
        logging.warning(f'{response}')
        print("Response: ", response)
        if response.status_code == 201:
            body_result = response.json()
            print("Body result: ", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def get_file_with_valid_size(self, max_size):
        if max_size == 5000:
            file = 'dusk_till_dawn.mp4'
        elif max_size == 1000:
            file = 'file_example_JPG_500kB.jpg'
        elif max_size == 500:
            file = '400KB.PNG'
        elif max_size == 100:
            file = 'PDF_B002.pdf'
        return file

    def get_file_with_invalid_size(self, max_size):
        if max_size == 5000:
            file = '10mb.pdf'
        elif max_size == 1000:
            file = 'videoplayback.mp4'
        elif max_size == 500:
            file = 'file_example_JPG_500kB.jpg'
        elif max_size == 100:
            file = 'test.jpg'
        return file

    def get_max_playbook_content_file_size(self):
        TokenAccess.TokenAccess().user_retrieves_token_access_as("hqadm")
        AppSetupGet().user_retrieves_details_of_application_setup()
        body_res = BuiltIn().get_variable_value(b_res)
        if body_res['PLAYBK_MAX_CONTENT_SIZE'] is not None:
            max_size = body_res['PLAYBK_MAX_CONTENT_SIZE']['SIZE']
        else:
            max_size = '5000'
        print("Max size in function: ", max_size)
        return max_size

    def payload_playbook(self, type, g_payload, c_assignment):
        """ Function for playbook payload content """
        payload = {
            "GENERAL_INFO":
                g_payload
            ,
            "CONTENT_ASSIGNMENT":
                c_assignment
        }
        payload = json.dumps(payload)
        print("Playbook Payload: ", payload)
        return payload
