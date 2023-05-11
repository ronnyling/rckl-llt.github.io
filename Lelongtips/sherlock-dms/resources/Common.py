from datetime import datetime
from setup.yaml.YamlDataManipulator import YamlDataManipulator
from setup.hanaDB import HanaDB
from robot.libraries.BuiltIn import BuiltIn
import re
import importlib
import secrets
import pytz

class Common(object):
    LOAD_TIME = "0.5 min"
    RETRY_TIME = "2 sec"
    STATUS_CODE = "${status_code}"
    BODY_RESULT = "${body_result}"
    USER_ROLE = "${user_role}"
    RANDOM_ID = "${random_id}"
    PRINCIPAL = "${principal}"
    DISTRIBUTOR_ID = '${distributor_id}'
    RECORD_ADDED = "Record added"
    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.000Z"

    def generate_random_id(self, prefix):
        random_string = prefix + ''.join(secrets.choice('0123456789ABCDEF') for _ in range(39))
        random_id = re.sub(r'(.{8})(.{8})(.{4})(.{4})(.{4})(.{4})', r'\1:\2-\3-\4-\5-\6', random_string)
        return random_id

    def convert_string_to_id(self, string):
        converted_id = re.sub(r'(.{8})(.{8})(.{4})(.{4})(.{4})(.{4})', r'\1:\2-\3-\4-\5-\6', string)
        return converted_id

    def convert_string_tenant_id_to_tenant_id(self, string):
        converted_id = re.sub(r'(.{8})(.{4})(.{4})(.{4})(.{12})', r'\1-\2-\3-\4-\5', string)
        return converted_id

    def convert_id_to_string(self, hex_id):
        print("hex id",hex_id)
        hex_id = hex_id.replace(':', "")
        hex_id = hex_id.replace('-', "")
        return hex_id

    def get_tenant_id(self):
        dist_id = self.convert_id_to_string(BuiltIn().get_variable_value(self.DISTRIBUTOR_ID))
        route_id = self.convert_id_to_string(BuiltIn().get_variable_value('${route_id}'))
        cust_id = self.convert_id_to_string(BuiltIn().get_variable_value('${cust_id}'))
        query = "SELECT distinct cast(tenant_id as varchar) " \
                "FROM TXN_OPENITEMS " \
                "WHERE CREATED_BY = '{0}' ".format(dist_id)# where dist_id = '{0}' ".format(dist_id)
              #  "and route_id = '{1}' " \
              #  "and cust_id = '{2}' and is_deleted = 'false'"\

        print ("QUERY:" , query)
        HanaDB.HanaDB().connect_database_to_environment()
        tenant_id = HanaDB.HanaDB().fetch_one_record(query)
        HanaDB.HanaDB().disconnect_from_database()
        BuiltIn().set_test_variable("${tenant_id}", tenant_id)
        return tenant_id

    def execute_prerequisite(self, yaml_file):
        param = 'module_object.{0}()'
        self.post_action(param, yaml_file)

    def post_action(self, param, yaml_file):
        prerequisite_by_post = YamlDataManipulator().user_retrieves_data_from_yaml(yaml_file, 'PrerequisiteByPost')
        if prerequisite_by_post is not None:
            self.loop_and_post_by_module(prerequisite_by_post, param, yaml_file)
            self.get_action(param, yaml_file)

    def check_and_set_user_from_yaml(self, post_key):
        if 'user' in post_key:
            from resources.restAPI.Common import TokenAccess
            TokenAccess.TokenAccess().get_token_by_role(post_key['get_user_token'])

    def loop_and_post_by_module(self, prerequisite_by_post, param, yaml_file):
        for module in prerequisite_by_post:
            module_call = module.split('_')[1]
            module_object = importlib.import_module(prerequisite_by_post[module]['module_location'])
            print('Imported module: ', module_object)
            test_variable_name = '${' + prerequisite_by_post[module]['test_variable_name'] + '}'
            BuiltIn().set_test_variable(test_variable_name, prerequisite_by_post[module])
            self.check_and_set_user_from_yaml(prerequisite_by_post[module])
            if 'data_type' in prerequisite_by_post[module]:
                getattr(eval(param.format(module_call)), prerequisite_by_post[module]['method'])(
                    prerequisite_by_post[module]['data_type'])
            else:
                getattr(eval(param.format(module_call)), prerequisite_by_post[module]['method'])()
            body_result = BuiltIn().get_variable_value("${body_result}")
            self.check_and_return_data(body_result, prerequisite_by_post[module], yaml_file, module)

    def check_and_return_data(self, body_result, post_key, yaml_file, module):
        if body_result is not None and 'return_data' in post_key:
            return_data = post_key['return_data']
            return_data = return_data.split(",")
            for item in return_data:
                output_data = {item: body_result[item]}
                output = {module: output_data}
                YamlDataManipulator().user_updates_yaml_data(yaml_file, 'Output', **output)

    def get_action(self, param, yaml_file):
        prerequisite_by_get = YamlDataManipulator().user_retrieves_data_from_yaml(yaml_file, 'PrerequisiteByGet')
        if prerequisite_by_get is not None:
            for module in prerequisite_by_get:
                module_call = module.split('_')[1]
                module_object = importlib.import_module(prerequisite_by_get[module]['module_location'])
                print('Imported module: ', module_object)
                getattr(eval(param.format(module_call)), prerequisite_by_get[module]['method'])(
                    list(prerequisite_by_get[module].values())[2])

    def wait_keyword_success(self, action, *args):
        BuiltIn().wait_until_keyword_succeeds(Common.LOAD_TIME, Common.RETRY_TIME, action, *args)

    def get_local_time(self):
        utc_now = datetime.utcnow()
        HanaDB.HanaDB().connect_database_to_environment()
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        dist_id = self.convert_id_to_string(dist_id)
        query = HanaDB.HanaDB().metadata_db_query('distributors', dist_id)
        record = HanaDB.HanaDB().fetch_all_record(query)
        HanaDB.HanaDB().disconnect_from_database()
        for i in record:
            if i[1] == 'TIMEZONE':
                dist_timezone = i[0]
                break
        local_tz = pytz.timezone(dist_timezone)
        local_dt = utc_now.replace(tzinfo=pytz.utc).astimezone(local_tz)
        local_dt = local_dt.strftime(self.DATE_FORMAT)
        print(local_dt)
        return local_dt
