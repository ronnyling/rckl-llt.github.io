from robot.libraries.BuiltIn import BuiltIn
import requests
import urllib3
import logging
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class APIMethod(object):

    def trigger_api_request(self, method, url, payload, **custom_param):
        method = method.upper()
        logging.warning(f'----------------------------------')
        logging.warning(f'{method}:{url}')
        files = BuiltIn().get_variable_value("${files}")
        print("Files in APImethod: ", files)
        if files is not None:
            my_token = BuiltIn().get_variable_value("${my_token}")
            headers = {
                'Authorization': 'Bearer {0}'.format(str(my_token))
            }
            response = requests.request(method, url, data=payload, files=files, headers=headers)
        else:
            response = requests.request(method, url, data=payload, headers=self.common_header(**custom_param),
                                        verify=False)
        print("Status code is " + str(response.status_code))
        print("Response in common file is", response)
        if response.status_code == 400:
            print("Error details = ", response.text)
        return response

    def common_header(self, **custom_data):
        my_token = BuiltIn().get_variable_value("${my_token}")
        headers = {
            'Content-Type': "application/json",
            'Accept': "application/json",
            'Authorization': 'Bearer {0}'.format(str(my_token))
        }
        if custom_data:
            headers.update((k, v) for k, v in custom_data.items())
        return headers
