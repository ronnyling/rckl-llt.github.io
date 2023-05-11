import inspect
import re

from robot.libraries.BuiltIn import BuiltIn
import requests
import urllib3
import logging

from resources.restAPI.Common.TokenAccess import TokenAccess
from resources.restAPI.Config.ReferenceData.ReasonType.ReasonGet import ReasonGet
from resources.restAPI.Config.ReferenceData.ReasonType.ReasonPost import ReasonPost
from resources.restAPI.WarehouseInventory.StockOut.StockOutGet import StockOutGet

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class APIMethod(object):

    def trigger_api_request(self, method, url, payload, **custom_param):
        method = method.upper()
        logging.warning(f'----------------------------------')
        logging.warning(f'{method}:{url}')
        files = BuiltIn().get_variable_value("${files}")
        print("Files in APImethod: ", files)
        setup_issue = True
        tries_cnt = 0
        while setup_issue and tries_cnt < 3:
            tries_cnt = tries_cnt + 1
            if files is not None:
                my_token = BuiltIn().get_variable_value("${my_token}")
                headers = {
                    'Authorization': 'Bearer {0}'.format(str(my_token))
                }
                response = requests.request(method, url, data=payload, files=files, headers=headers, **custom_param)
            else:
                response = requests.request(method, url, data=payload, headers=self.common_header(**custom_param),
                                            verify=False)
            invalid_url = re.findall(r".*(None).*$", str(url))
            if response.status_code == 204 or invalid_url:
            # scenarios where response is empty
            # if response.status_code == 404 or response.status_code == 204 or response is None:
                handling_result = self.dynamic_handler(url)
                assert handling_result, "Please add this module to dynamic handling, going to next iteration"
            else:
                setup_issue = False
        if setup_issue:
            self.handler_msg(url)
        assert not setup_issue, "2 - Please handle error 204, 404"

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

    def handler_msg(self, url):
        try:
            print(
                "\n\n\n***************************************************************\n\n Not able to dynamically handle api, please attend.\n\n")
            stack = self.get_stack_info()
            print("\t File \t\t = " + stack[1])
            print("\t Function \t = " + stack[3])
            # print("Not able to get module from stack = " + str(inspect.stack()[3][0]))
            # print("Not able to get module from stack = " + str(inspect.stack()[3][1]))
            # print("Not able to get module from stack = " + str(inspect.stack()[3][2]))
            # print("Not able to get module from stack = " + str(inspect.stack()[3][3]))
        except:
            pass

        print("\t API \t\t = " + url)
        print("\n\n***************************************************************\n\n\n ")

    def dynamic_handler(self, url):
        saved_role = BuiltIn().get_variable_value("${current_role}")
        stack = self.get_stack_info()
        # print("get_api function=  " + str(stack.function))
        get_api = stack.function
        matched = False
        handler = {
            # add failed get function name here with post method as handler
            "user_retrieves_rand_reason_for_stock_out_type": True,
            "setting-reasontype/.*?/setting-reason": self.handle_reasontypes()
        }
        if get_api in handler.keys():
            matched = True
            print("Created data for api " + get_api)
        else:
            for i in handler.keys():
                my_regex = re.compile("^.*?(%s).*$" % i)
                if my_regex.findall(url):
                    get_api = i
                    matched = True
                    break
        if not matched:
            self.handler_msg(url)
        assert matched, "1 - Regex matching failed,Handler not added yet, please attend"
        result = handler.get(get_api, False)
        curr_role = BuiltIn().get_variable_value("${current_role}")
        if saved_role != curr_role:
            TokenAccess().user_retrieves_token_access_as(saved_role)
        return result

    def handle_reasontypes(self):
        TokenAccess().user_retrieves_token_access_as('hqadm')
        ReasonGet().user_retrieves_all_reasons_for_all_operations()
        rsn_all_ops_ls = BuiltIn().get_variable_value("${rsn_all_ops_ls}")
        stack = self.get_stack_info()
        print("gggg0 " + str(stack))
        file_source = str(stack[1])
        source1 = re.findall(r".*\\(.*)\\.*py$", file_source)[0]
        source2 = re.findall(r".*\\(.*)\\.*\\.*py$", file_source)[0]
        source = source1 + "_" + source2
        print("gggg= " + source + file_source)

        # match "ABC".upper():
        #     case "AbC":
        #         print("AbC")
        #     case "abc":
        #         print("abc")
        #     case "ABC":
        #         print("case very sensitive")
        #     case _:
        #         print("nightmare")
        # self.raise_exception("fxxk it")

        curr_op_type = None
        match source:
            case "CreditNoteNonProduct_CompTrx":
                curr_op_type = "SCNNP"
            case "CreditNoteNonProduct_CustTrx":
                curr_op_type = "CNNP"
            case "running_robot234565432":
                curr_op_type = None
            case "StockOut_WarehouseInventory":
                curr_op_type = "ISO"
            case _:
                self.raise_exception("Op type not configured in handler")

        # print("is this gg " + str(source))
        # print("is this gg " + operation_types.get(str.upper((source)), "gg"))
        # curr_op_type = operation_types.get(str.upper(source), None)
        # print("gggg2 " + curr_op_type)
        if curr_op_type:
            type_id = next((i['ID'] for i in rsn_all_ops_ls if i['REASON_TYPE_CD'] == curr_op_type))
        else:
            raise Exception("Issue with METADATA, please setup settingreason reasontype code")
        BuiltIn().set_test_variable("${res_bd_reason_type_id}", type_id)
        ReasonPost().user_creates_reason_with('')
        return True

    def raise_exception(self, msg):
        stack_info = str(inspect.stack())
        raise Exception(msg + ", More info= " + stack_info)

    def get_stack_info(self):
        stack = None
        for i in inspect.stack():
            file = re.findall(r".*\\(.*)\.py.*", str(i))[0]
            if file == "APIMethod":
                continue
            elif file == "librarykeywordrunner":
                raise "Code issue, please fix"
            else:
                print("file= " + file)
                print(str(i))
                stack = i
                break
        return stack
