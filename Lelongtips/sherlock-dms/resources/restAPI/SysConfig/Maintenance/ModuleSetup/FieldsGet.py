""" Python file related to fields in module setup API """

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.SysConfig.Maintenance.ModuleSetup import ModuleSetupGet
import secrets

END_POINT_URL_METADATA_MODULE = PROTOCOL + "metadata" + APP_URL + "metadata-module"
END_POINT_URL_MODULES = PROTOCOL + "metadata" + APP_URL + "modules"
END_POINT_URL_OBJECTSTORE = PROTOCOL + "objectstore" + APP_URL + "storage"


class FieldsGet:
    """ Functions related to fields in module setup GET request """

    @keyword("user retrieves ${data_type} fields in module setup")
    def user_retrieves_fields_in_module_setup(self, data_type):
        """ Functions to retrieve all/created fields in module setup """
        module_setup_id = BuiltIn().get_variable_value("${module_setup_id}")
        url = "{0}/{1}/metadata-field".format(END_POINT_URL_METADATA_MODULE, module_setup_id)

        ModuleSetupGet.ModuleSetupGet().retrieves_variable_value(data_type, "${module_fields_id}", url)

    def user_retrieves_random_attachment_from_objectstore(self, module, field, type):
        """ Functions to retrieve random attachment from module """
        url = "{0}/{1}/{2}".format(END_POINT_URL_OBJECTSTORE, module, field)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve any record"
        body_result = response.json()
        data_list = []
        for count in range(0, len(body_result)):
            if type in body_result[count]["Key"]:
                data_list.append(body_result[count]["Key"])
        if data_list:
            random_file = "/objectstore-svc/api/v1.0/storage/{0}".format(secrets.choice(data_list))
        else:
            random_file = "/objectstore-svc/api/v1.0/storage/{0}/{1}/".format(module, field)
        return random_file