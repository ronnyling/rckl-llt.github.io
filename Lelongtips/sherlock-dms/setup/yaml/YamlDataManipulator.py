import os
from os.path import join
import ruamel.yaml
import json


class YamlDataManipulator(object):

    def user_retrieves_data_from_yaml(self, file_name, data=None):
        file_path = self.find_yaml_file_path(file_name)
        respond = self.loads_yaml_records(file_path)
        if data is None:
            return respond
        return respond[data]

    def loads_yaml_records(self, file_path):
        respond, ind, bsi = ruamel.yaml.util.load_yaml_guess_indent(open(file_path))
        respond = json.loads(json.dumps(respond))
        return respond

    def user_updates_yaml_data(self, file_name, data, **details):
        file_path = self.find_yaml_file_path(file_name)
        respond = self.loads_yaml_records(file_path)
        if details:
            for key in respond[data].keys():
                    if details.get(key):
                        respond[data][key].update((k, v) for k, v in details[key].items())
        with open(file_path, 'w') as stream:
            ruamel.yaml.dump(respond, stream, Dumper=ruamel.yaml.RoundTripDumper)
        respond = self.loads_yaml_records(file_path)
        return respond

    def find_yaml_file_path(self, file_name):
        current_dir = os.getcwd()
        for root, dirs, files in os.walk(current_dir):
            if file_name in files:
                file_path = join(root, file_name)
                file_path = file_path.replace("\\", "/")
                break
        return file_path

