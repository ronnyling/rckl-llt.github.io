import re
import time

import requests
import os
import urllib
from urllib.parse import quote, unquote
from selenium.webdriver.common.by import By
from resources.restAPI.Common.RefererSession import RefererSession
from setup.yaml import YamlDataManipulator
from selenium import webdriver
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from sys import platform

hq = "${hq_token}"
dist = "${dist_token}"
sysimp = "${sysimp_token}"

ENV_DETAILS = YamlDataManipulator.YamlDataManipulator().user_retrieves_data_from_yaml("loginCredential.yaml",
                                                                                BuiltIn().get_variable_value("${ENV}"))

class TokenAccess(object):
    @keyword('user retrieves token access as ${user_role}')
    def user_retrieves_token_access_as(self, user_role):
        my_token = BuiltIn().get_variable_value("${my_token}")
        current_role = BuiltIn().get_variable_value("${current_role}")
        if (user_role == 'hqadm' and current_role == 'hqadm' and my_token) or \
                (user_role == 'distadm' and current_role == 'distadm' and my_token) or \
                (user_role == 'sysimp' and current_role == 'sysimp' and my_token):
            pass
        else:
            response = self.get_token(user_role)
            if response[0] == "401":
                trial_time = 0
                while trial_time < 10:
                    trial_time = trial_time + 1
                    response = self.get_token(user_role)
                    if response[0] == '200':
                        break
                    time.sleep(1)
                    print("tried times = " + str(trial_time))
                    assert trial_time < 10, "Could not retrieve token access, please check connection"
            BuiltIn().set_test_variable("${my_token}", response[1]['access_token'])
            if user_role == 'hqadm':
                BuiltIn().set_test_variable(hq, response[1]['access_token'])
                BuiltIn().set_test_variable("${current_role}", 'hqadm')
            elif user_role == 'distadm':
                BuiltIn().set_test_variable(dist, response[1]['access_token'])
                BuiltIn().set_test_variable("${current_role}", 'distadm')
            else:
                BuiltIn().set_test_variable(sysimp, response[1]['access_token'])
                BuiltIn().set_test_variable("${current_role}", 'sysimp')

    @keyword('user set user token to ${user_role}')
    def get_token_by_role(self, role):
        if role == 'hqadm':
            token = BuiltIn().get_variable_value(hq)
        elif role == 'distadm':
            token = BuiltIn().get_variable_value(dist)
        else:
            token = BuiltIn().get_variable_value(sysimp)
        BuiltIn().set_test_variable("${my_token}", token)

    def get_token(self, user_role):

        login_credential = self.user_logins_web(user_role)
        user_name = login_credential[0]
        user_password = login_credential[1]
        passcode = self.get_passcode(user_name, user_password)
        url = "{0}oauth/token".format(ENV_DETAILS['Detail'].get('TokenURL'))
        conn_data = {
            'username': user_name,
            'password': user_password,
            'client_id': ENV_DETAILS['Detail'].get('Client_id'),
            'client_secret': ENV_DETAILS['Detail'].get('Client_secret'),
            'response_type': 'token',
            'passcode': passcode
        }
        username = conn_data['username']
        password = conn_data['password']
        client_id = urllib.parse.quote(conn_data['client_id'])
        client_secret = urllib.parse.quote(conn_data['client_secret'])
        response_type = conn_data['response_type']
        passcode = conn_data['passcode']
        payload = "grant_type=password&username=" + username + \
                  "&password=" + password + \
                  "&client_id=" + client_id + \
                  "&client_secret=" + client_secret + \
                  "&response_type=" + response_type + \
                  "&passcode=" + passcode
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Accept': "application/json;charset=utf8"
        }
        response = requests.post(url, data=payload, headers=headers, verify=False)
        print(response.status_code)
        data = response.json()
        return str(response.status_code), data

    def user_logins_web(self, user_type):
        username = ENV_DETAILS['Credential'][user_type].get('Username')
        password = ENV_DETAILS['Credential'][user_type].get('Password')
        return username, password

    def get_passcode(self, user_name, user_password):
        base_url_1 = ENV_DETAILS['Detail'].get('BaseUrl1')
        base_url_2 = ENV_DETAILS['Detail'].get('BaseUrl2')
        base_url_3 = ENV_DETAILS['Detail'].get('BaseUrl3')
        base_url_3_1 = ENV_DETAILS['Detail'].get('BaseUrl3_1')
        client_id = ENV_DETAILS['Detail'].get('Client_id')
        alias_name = ENV_DETAILS['Detail'].get('AliasName')
        login_data = {}
        s = RefererSession()
        s.get(base_url_1)
        r = s.get(base_url_1 + "/index.html")
        param = {
            "response_type": "code",
            "client_id": client_id,
            "redirect_uri": "{0}/login/callback".format(base_url_1)
        }
        s.get(url=base_url_2 + "/oauth/authorize", params=param, allow_redirects=True)
        r = s.get(url=base_url_2 + "/login", allow_redirects=True)
        # 1
        raw_url = (re.findall(".*<meta name=\"redirect\" content=\"(.*?)\">.*", r.text))[0]
        refined_url = raw_url.split("amp;")
        redirected_url = ''.join(i for i in refined_url)
        # raise Exception("stop here =" + str(redirected_url))

        r = s.get(url=redirected_url, allow_redirects=True)
        r = s.get(url=r.url, allow_redirects=True)

        sp = (re.findall(".*?name=\"sp\" value=\"(.*?)\"><.*?", r.text))[0]
        relay_state = (re.findall(".*?/authorize\?(.*)$", redirected_url))[0]
        # c_saml_request = (re.match(".*?SAMLRequest=(.*?)&.*?", r.url)).group(1)
        # c_signature = (re.match(".*?&Signature=(.*?)$", r.url)).group(1)
        c_authenticity_token = (re.findall(".*?name=\"authenticity_token\" value=\"(.*?)\" /><.*?", r.text))[0]
        c_xsrf_protection = (re.findall("name=\"xsrfProtection\" value=\"(.*?)\" ><", r.text))[0]
        sp_id = (re.findall(".*?name='spId' type='hidden' value='(.*?)'>.*?", r.text))[0]
        sp_name = (re.findall(".*?name='spName' type='hidden' value='(.*?)'><.*?", r.text))[0]
        saml2url = "{0}/saml2/idp/sso".format(base_url_3)
        data = {
            "utf8": unquote("%E2%9C%93"),
            "authenticity_token": (c_authenticity_token),
            "xsrfProtection": (c_xsrf_protection),
            "method": "GET",
            "idpSSOEndpoint": ("{0}/saml2/idp/sso".format(base_url_3)),
            "sp": unquote(sp),
            "RelayState": unquote(relay_state),
            "targetUrl": unquote(redirected_url),
            "SigAlg": ("http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"),
            "spId": sp_id,
            "spName": sp_name,
            "j_username": user_name,
            "j_password": user_password
        }
        data['utf8'] = quote(data['utf8'], safe='')
        data['authenticity_token'] = quote(data['authenticity_token'], safe='')
        data['xsrfProtection'] = quote(data['xsrfProtection'], safe='')
        data['idpSSOEndpoint'] = quote(data['idpSSOEndpoint'], safe='')
        data['RelayState'] = quote(data['RelayState'], safe='')
        data['targetUrl'] = quote(data['targetUrl'], safe='')
        data['sp'] = quote(data['sp'], safe='')
        data['SigAlg'] = quote(data['SigAlg'], safe='')
        data['spName'] = quote(data['spName'], safe='')
        data['j_password'] = quote(data['j_password'], safe='')
        new_data = ''.join('{}={}&'.format(key, val) for key, val in data.items())
        patched_data = (re.findall("^(.*?)&$", new_data))[0]
        s.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})

        r = s.post(url=saml2url, data=patched_data, allow_redirects=True)

        r = s.get(url=base_url_2 + "/passcode", allow_redirects=True)
        # print("ronnytest " + str(r.text))
        passcode = (re.findall("<h2><samp id=\"passcode\">(.*?)</samp>", r.text))[0]
        # raise Exception("stop here = " +str(passcode))
        return passcode
        # param = {
        #     "returnIDParam": "idp",
        #     "entityID": base_url_2,
        #     "idp": base_url_3_1,
        #     "isPassive": "true"
        # }
        # s.get(url=base_url_2 + "/saml/discovery", params=param, allow_redirects=True)
        # param = {
        #     "disco": "true",
        #     "idp": base_url_3_1
        # }
        # r = s.get(url=base_url_2 + "/saml/login/alias/{0}".format(alias_name), params=param, allow_redirects=True)
        # # raise Exception ("ggz " + str(r.url))
        # c_saml_request = (re.match(".*?SAMLRequest=(.*?)&.*?", r.url)).group(1)
        # c_signature = (re.match(".*?&Signature=(.*?)$", r.url)).group(1)
        # saml2_url = r.url
        # r = s.get(url=r.url, allow_redirects=True)
        # c_authenticity_token = (re.findall(".*?name=\"authenticity_token\" value=\"(.*?)\" /><.*?", r.text))[0]
        # c_xsrf_protection = (re.findall("name=\"xsrfProtection\" value=\"(.*?)\" ><", r.text))[0]
        # sp_id = (re.findall(".*?name='spId' type='hidden' value='(.*?)'>.*?", r.text))[0]
        # login_data.update({"session_obj": s})
        # login_data.update({"c_saml_request": c_saml_request})
        # login_data.update({"c_signature": c_signature})
        # login_data.update({"c_authenticity_token": c_authenticity_token})
        # login_data.update({"c_xsrf_protection": c_xsrf_protection})
        # login_data.update({"sp_id": sp_id})
        # login_data.update({"saml2_url": saml2_url})
        # data = {
        #     "utf8": unquote("%E2%9C%93"),
        #     "authenticity_token": (c_authenticity_token),
        #     "xsrfProtection": (c_xsrf_protection),
        #     "method": "GET",
        #     "idpSSOEndpoint": ("{0}/saml2/idp/sso/{1}".format(base_url_3, base_url_3_1)),
        #     "SAMLRequest": unquote(c_saml_request),
        #     "SigAlg": ("http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"),
        #     "Signature": unquote(c_signature),
        #     "spId": sp_id,
        #     "spName": (base_url_2),
        #     "j_username": user_name,
        #     "j_password": user_password
        # }
        # data['utf8'] = quote(data['utf8'], safe='')
        # data['authenticity_token'] = quote(data['authenticity_token'], safe='')
        # data['xsrfProtection'] = quote(data['xsrfProtection'], safe='')
        # data['idpSSOEndpoint'] = quote(data['idpSSOEndpoint'], safe='')
        # data['SAMLRequest'] = quote(data['SAMLRequest'], safe='')
        # data['Signature'] = quote(data['Signature'], safe='')
        # data['SigAlg'] = quote(data['SigAlg'], safe='')
        # data['spName'] = quote(data['spName'], safe='')
        # data['j_password'] = quote(data['j_password'], safe='')
        # new_data = ''.join('{}={}&'.format(key, val) for key, val in data.items())
        # patched_data = (re.findall("^(.*?)&$", new_data))[0]
        # s.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
        # r = s.post(url=saml2_url, data=patched_data, allow_redirects=True)
        # c_saml_response = \
        # (re.findall("name=\"SAMLResponse\" id=\"SAMLResponse\" value=\"(.*?)\" /><input type=", r.text))[0]
        # c_authenticity_token = (re.findall("name=\"authenticity_token\" value=\"(.*?)\" /><input type=", r.text))[0]
        # data = {
        #     "utf8": unquote("%E2%9C%93"),
        #     "authenticity_token": c_authenticity_token,
        #     "SAMLResponse": c_saml_response,
        #     "RelayState": "cloudfoundry-uaa-sp"
        # }
        # data['utf8'] = quote(data['utf8'], safe='')
        # data['authenticity_token'] = quote(data['authenticity_token'], safe='')
        # data['SAMLResponse'] = quote(data['SAMLResponse'], safe='')
        # data['RelayState'] = quote(data['RelayState'], safe='')
        # new_data = ''.join('{}={}&'.format(key, val) for key, val in data.items())
        # patched_data = (re.findall("^(.*?)&$", new_data))[0]
        # s.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
        # s.post(url=base_url_2 + "/saml/SSO/alias/{0}".format(alias_name), data=patched_data, allow_redirects=False)
        # param = {
        #     "response_type": "code",
        #     "client_id": str(client_id),
        #     "redirect_uri": quote("{0}/login/callback".format(base_url_1), safe='')
        # }
        # param_new = ''.join('{}={}&'.format(key, val) for key, val in param.items())
        # param_new = (re.findall("^(.*?)&$", param_new))[0]
        # newest_url = base_url_2 + "/oauth/authorize?" + param_new
        # r = s.get(url=newest_url, allow_redirects=True)
        # c_code = (re.findall("^.*?code=(.*?)$", r.url))[0]
        # # print("why fail now " + c_code)
        # param = {
        #     "code": c_code
        # }
        # s.get(url=base_url_1 + "/login/callback", params=param, allow_redirects=True)
        # r = s.get(url=base_url_2 + "/passcode", allow_redirects=True)
        # # print("ronnytest " + str(r.text))
        # passcode = (re.findall("<h2><samp id=\"passcode\">(.*?)</samp>", r.text))[0]
        # return passcode

    def retrieve_driver(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        if platform == "linux" or platform == "linux2":     # check OS type
            chrome_driver = os.path.join(dir_path, "../../../setup/drivers/linux/chromedriver")     # use linux version of chromedriver
        else:
            chrome_driver = os.path.join(dir_path, "../../../setup/drivers/chromedriver.exe")

        os.chmod(chrome_driver, 0o755)      # grants write access to the webdriver file
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        if platform == "linux" or platform == "linux2":
            options.add_argument("--no-sandbox")    # bypass OS security model
            options.add_argument("--disable-dev-shm-usage")    # overcome limited resource problems
            options.add_argument('--remote-debugging-port=9222')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(executable_path=str(chrome_driver), options=options)
        return driver

    def user_logouts_web(self, driver):
        driver.find_element(By.XPATH, '//div[@class="dropdown-trigger"]').click()
        driver.find_element(By.XPATH, '//*[contains(text(), "Sign Out")]').click()
        driver.close()
