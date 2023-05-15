from resources.Common import Common
from robot.libraries.BuiltIn import BuiltIn
from setup.yaml import YamlDataManipulator

COMMON_KEY = Common()
ENV_DETAILS = YamlDataManipulator.YamlDataManipulator().user_retrieves_data_from_yaml("loginCredential.yaml",
                                                                            BuiltIn().get_variable_value("${ENV}"))
APP_URL = ENV_DETAILS['Detail'].get('RestAPI_EndPoint')
PROTOCOL = 'https://'
LLT_URL = 'www.lelongtips.com.my/search?keyword=&property_type%5B%5D=1&property_type%5B%5D=4&property_type%5B%5D=5&property_type%5B%5D=3&state=kl_sel&min_price=150000&max_price=1000000&min_size=&max_size=&sort=price-asc&page=' #&page=[1-300]'
LLT_TOKEN = '2a2528f1fe702b30de4754240bfbf1f24a50eddb5928cc5bd0eb30c21ccc22f05'
GMAPS_TOKEN = 'AIzaSyCFnR_9wkfFiy0Xui-qf4tXXe3T5aQ0yZk'