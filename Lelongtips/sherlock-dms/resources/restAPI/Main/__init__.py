from resources.Common import Common
from robot.libraries.BuiltIn import BuiltIn
from setup.yaml import YamlDataManipulator

COMMON_KEY = Common()
ENV_DETAILS = YamlDataManipulator.YamlDataManipulator().user_retrieves_data_from_yaml("loginCredential.yaml",
                                                                            BuiltIn().get_variable_value("${ENV}"))
APP_URL = ENV_DETAILS['Detail'].get('RestAPI_EndPoint')
PROTOCOL = 'https://'