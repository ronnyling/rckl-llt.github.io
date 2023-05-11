import re

from urllib.parse import quote, unquote

from resources.restAPI.Common.RefererSession import RefererSession
from setup.yaml import YamlDataManipulator
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

hq = "${hq_token}"
dist = "${dist_token}"
sysimp = "${sysimp_token}"

ENV_DETAILS = YamlDataManipulator.YamlDataManipulator().user_retrieves_data_from_yaml("loginCredential.yaml",
                                                                                BuiltIn().get_variable_value("${ENV}"))


class RabbitHoleGet(object):
    user_role = "sysimp"

    @keyword('user going down rabbit hole')
    def rabbit_hole_inspected(self):
        login_data = self.trigger_NP_TCN02_Bulk_Printing_The_Invoice_01_Launch()
        # session = self.trigger_NP_TCN02_Bulk_Printing_The_Invoice_02_Login(login_data)
        # token = self.get_token(session)
        # print("token " + str(token))

    def get_token(self, s):
        base_url_2 = ENV_DETAILS['Detail'].get('BaseUrl2')
        r = s.get(url=base_url_2 + "/passcode")
        s.close()

        # print("here here " + s)
        token = None
        return token

    def trigger_NP_TCN02_Bulk_Printing_The_Invoice_02_Login(self, login_data):
        base_url_1 = ENV_DETAILS['Detail'].get('BaseUrl1')
        base_url_1_1 = ENV_DETAILS['Detail'].get('BaseUrl1_1')
        base_url_2 = ENV_DETAILS['Detail'].get('BaseUrl2')
        base_url_3 = ENV_DETAILS['Detail'].get('BaseUrl3')
        base_url_3_1 = ENV_DETAILS['Detail'].get('BaseUrl3_1')
        client_id = ENV_DETAILS['Detail'].get('Client_id')
        alias_name = ENV_DETAILS['Detail'].get('AliasName')

        s = login_data["session_obj"]
        c_saml_request = unquote(login_data["c_saml_request"])
        c_signature = unquote(login_data["c_signature"])
        c_authenticity_token = login_data["c_authenticity_token"]
        c_xsrf_protection = login_data["c_xsrf_protection"]
        sp_id = login_data["sp_id"]
        saml2_url = login_data["saml2_url"]

        param = {
            "SAMLRequest": c_saml_request,
            "RelayState": "cloudfoundry-uaa-sp",
            "SigAlg": "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256",
            "Signature": c_signature
        }
        data = {
            "authenticity_token": str(c_authenticity_token),
            "xsrfProtection": str(c_xsrf_protection),
            "method": "GET",
            "idpSSOEndpoint": ("{0}/saml2/idp/sso/{1}".format(base_url_3, base_url_3_1)),
            "SAMLRequest": str(c_saml_request),
            "SigAlg": ("http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"),
            "Signature": str(c_signature),
            "spId": sp_id,
            "spName": (base_url_2),
            "j_username": ENV_DETAILS['Credential'][self.user_role].get('Username'),
            "j_password": ENV_DETAILS['Credential'][self.user_role].get('Password')
        }
        data.update((k, unquote(v)) for k, v in data.items())
        # r = s.get(url=base_url_3 + "/saml2/idp/sso", params=param, data=data)
        # new_url = base_url_3+"/saml2/idp/sso?"+"SAMLRequest="+c_saml_request+"&RelayState="+\
        #           "cloudfoundry-uaa-sp"+"&SigAlg="+"http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"+\
        #           "&Signature="+c_signature
        with RefererSession() as s:
            # r = s.post(url=new_url, data=data, allow_redirects=True)
            r = s.post(url=base_url_3 + "/saml2/idp/sso", params=param, data=data, allow_redirects=True)
        # r = s.post(url=saml2_url, data=data)
        print("seeing double " + str(r.url))
        print("seeing correct " + str(data))
        print("seeing check " + str(r.text))

        c_saml_response = (re.findall(".*?name=\"SAMLResponse\" value=\"(.*?)\"/>.*?", r.text))[0]
        print("seeing last " + str(c_saml_response))

        param = {
            "redirect": "true"
        }
        with RefererSession() as s:
            r = s.get(url=base_url_3 + "/saml2/idp/sso", params=param, allow_redirects=True)
        print("final check " + str(r.text))
        print("final check " + str(r.url))

        data = {
            "utf8": "%E2%9C%93",
            "authenticity_token": c_authenticity_token,
            "SAMLResponse": c_saml_response,
            "RelayState": "cloudfoundry-uaa-sp"
        }
        print("really is last " + c_saml_response)
        print("really is last data " + str(data))
        # saml_url = base_url_2+"/saml/SSO/alias/"+alias_name
        with RefererSession() as s:
            r = s.post(url=base_url_2 + "/saml/SSO/alias/{0}".format(alias_name), data=data, allow_redirects=True)
        print("never back " + str(r.text))
        print("never back " + str(r.url))


        param = {
            "utf8": "%E2%9C%93",
            "response_type": "code",
            "client_id": str(client_id),
            "redirect_uri": "{0}/login/callback".format(base_url_1)
        }
        with RefererSession() as s:
            r = s.get(url=base_url_2 + "/oauth/authorize", params=param, allow_redirects=True)
        print("last sprint " + r.text)
        c_code = (re.findall(".*?code=(.*?)\n*?", r.text))[0]
        param = {
            "code": c_code
        }
        with RefererSession() as s:
            r = s.get(url=base_url_1 + "/login/callback", params=param, allow_redirects=True)

        print("response " + str(r.text))
        # print("mytext " + str(c_cookie_signature))
        # print("mytext " + str(c_cookie_signature.groups()))
        BuiltIn().set_test_variable("${status_code}", r.status_code)
        return s

    def get_passcode(self, user_name, user_password):
        base_url_1 = ENV_DETAILS['Detail'].get('BaseUrl1')
        base_url_1_1 = ENV_DETAILS['Detail'].get('BaseUrl1_1')
        base_url_2 = ENV_DETAILS['Detail'].get('BaseUrl2')
        base_url_3 = ENV_DETAILS['Detail'].get('BaseUrl3')
        base_url_3_1 = ENV_DETAILS['Detail'].get('BaseUrl3_1')
        client_id = ENV_DETAILS['Detail'].get('Client_id')
        alias_name = ENV_DETAILS['Detail'].get('AliasName')
        login_data = {}
        s = RefererSession()
        s.get(base_url_1)
        r = s.get(base_url_1 + "/index.html")
        c_cookie_signature = re.match(".*?signature=(.*?);.*?", r.text)
        param = {
            "response_type": "code",
            "client_id": client_id,
            "redirect_uri": "{0}/login/callback".format(base_url_1)
        }
        # with RefererSession() as s:
        s.get(url=base_url_2 + "/oauth/authorize", params=param, allow_redirects=True)
        # with RefererSession() as s:
        s.get(url=base_url_2 + "/login", allow_redirects=True)
        param = {
            "returnIDParam": "idp",
            "entityID": base_url_2,
            "idp": base_url_3_1,
            "isPassive": "true"
        }
        # with RefererSession() as s:
        s.get(url=base_url_2 + "/saml/discovery", params=param, allow_redirects=True)
        param = {
            "disco": "true",
            "idp": base_url_3_1
        }
        # with RefererSession() as s:
        r = s.get(url=base_url_2 + "/saml/login/alias/{0}".format(alias_name), params=param, allow_redirects=True)
        # print("response hehe1 " + r.history[1].request.headers)
        # for i in r.history:
        #     print(i.url)
        print("response hehe2 " + str(r.url))
        c_saml_request = (re.match(".*?SAMLRequest=(.*?)&.*?", r.url)).group(1)
        c_signature = (re.match(".*?&Signature=(.*?)$", r.url)).group(1)
        # print( "Ronny "+ c_saml_request).groups()[0])
        saml2_url = r.url
        # with RefererSession() as s:
        r = s.get(url=r.url, allow_redirects=True)

        # param = {
        #     "SAMLRequest": c_saml_request,
        #     "RelayState": "cloudfoundry-uaa-sp",
        #     "SigAlg": "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256",
        #     "Signature": c_signature,
        # }
        # print("saml2 param " + str(param))
        #
        # with RefererSession() as s:
        #     r = s.get(url=base_url_3 + "/saml2/idp/sso/{0}".format(base_url_3_1), params=param, allow_redirects=True)
        # c_saml_request_1 = re.match(".*?SAMLRequest=(.*?)&amp;.*?", r.text)).groups()[0]
        # c_saml_request_2 = re.match(".*?<input type=\"hidden\" name=\"SAMLRequest\" value=\"(.*?)\">.*?", r.text)
        print("saml2 call " + r.text)

        c_authenticity_token = (re.findall(".*?name=\"authenticity_token\" value=\"(.*?)\" /><.*?", r.text))[0]
        c_xsrf_protection = (re.findall("name=\"xsrfProtection\" value=\"(.*?)\" ><", r.text))[0]
        sp_id = (re.findall(".*?name='spId' type='hidden' value='(.*?)'>.*?", r.text))[0]

        print("response text" + str(r.text))
        print("response content" + str(r.content))
        # print("mytext " + str(c_cookie_signature))
        # print("mytext " + str(c_cookie_signature.groups()))
        BuiltIn().set_test_variable("${status_code}", r.status_code)

        login_data.update({"session_obj": s})
        login_data.update({"c_saml_request":  c_saml_request})
        login_data.update({"c_signature":  c_signature})
        login_data.update({"c_authenticity_token":  c_authenticity_token})
        login_data.update({"c_xsrf_protection":  c_xsrf_protection})
        login_data.update({"sp_id":  sp_id})
        login_data.update({"saml2_url": saml2_url})
        print("login data here " + str(login_data))


        param = {
            "SAMLRequest": c_saml_request,
            "RelayState": "cloudfoundry-uaa-sp",
            "SigAlg": "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256",
            "Signature": c_signature
        }
        data = {
            "utf8": unquote("%E2%9C%93"),
            "authenticity_token": (c_authenticity_token),
            "xsrfProtection": (c_xsrf_protection),
            "method": "GET",
            "idpSSOEndpoint": ("{0}/saml2/idp/sso/{1}".format(base_url_3, base_url_3_1)),
            "SAMLRequest": unquote(c_saml_request),
            "SigAlg": ("http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"),
            "Signature": unquote(c_signature),
            "spId": sp_id,
            "spName": (base_url_2),
            "j_username": user_name,
            "j_password": user_password
        }
        # data.update((k, unquote(v)) for k, v in data.items())
        # r = s.get(url=base_url_3 + "/saml2/idp/sso", params=param, data=data)
        # new_url = base_url_3+"/saml2/idp/sso?"+"SAMLRequest="+c_saml_request+"&RelayState="+\
        #           "cloudfoundry-uaa-sp"+"&SigAlg="+"http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"+\
        #           "&Signature="+c_signature
        raw_url_1 = (re.findall("^(.*?)/atjobprqo\.accounts\.ondemand\.com\?", saml2_url))
        raw_url_2 = (re.findall("atjobprqo\.accounts\.ondemand\.com\?(.*?)$", saml2_url))
        new_url = raw_url_1[0]+ "?" +raw_url_2[0]

        print("new url " + raw_url_1[0])
        print("new url " + raw_url_2[0])
        print("new url " + new_url)
        data['utf8'] = quote(data['utf8'], safe='')
        data['authenticity_token'] = quote(data['authenticity_token'], safe='')
        data['xsrfProtection'] = quote(data['xsrfProtection'], safe='')
        data['idpSSOEndpoint'] = quote(data['idpSSOEndpoint'], safe='')
        data['SAMLRequest'] = quote(data['SAMLRequest'], safe='')
        data['Signature'] = quote(data['Signature'], safe='')
        data['SigAlg'] = quote(data['SigAlg'], safe='')
        data['spName'] = quote(data['spName'], safe='')
        data['j_password'] = quote(data['j_password'], safe='')
        # data = json.dumps(data)
        # with RefererSession() as s:
        new_data = ''.join('{}={}&'.format(key, val) for key, val in data.items())
        patched_data = (re.findall("^(.*?)&$", new_data))[0]
        print("seeing data " + str(patched_data))

        s.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
        r = s.post(url=saml2_url, data=patched_data, allow_redirects=True)
        # r = s.post(url=base_url_3 + "/saml2/idp/sso", params=param, data=data, allow_redirects=True)
        # r = s.post(url=new_url, data=data, allow_redirects=True)

        # r = s.post(url=saml2_url, data=data)
        BuiltIn().set_test_variable("${status_code}", r.status_code)

        print("seeing data " + str(patched_data))
        print("seeing first " + str(s.headers))
        print("seeing double " + str(r.url))
        print("seeing correct " + str(data))
        print("seeing check " + str(r.text))
        c_saml_response = (re.findall("name=\"SAMLResponse\" id=\"SAMLResponse\" value=\"(.*?)\" /><input type=", r.text))[0]
        c_authenticity_token = (re.findall("name=\"authenticity_token\" value=\"(.*?)\" /><input type=", r.text))[0]
# name="authenticity_token" value="
# name="SAMLResponse" id="SAMLResponse" value="
        print("seeing last " + str(c_authenticity_token))

        param = {
            "redirect": "true"
        }
        # with RefererSession() as s:
        # r = s.get(url=base_url_3 + "/saml2/idp/sso", params=param, allow_redirects=True)
        # print("final check " + str(r.text))
        # print("final check " + str(r.url))

        data = {
            "utf8": unquote("%E2%9C%93"),
            "authenticity_token": c_authenticity_token,
            "SAMLResponse": c_saml_response,
            "RelayState": "cloudfoundry-uaa-sp"
        }
        data['utf8'] = quote(data['utf8'], safe='')
        data['authenticity_token'] = quote(data['authenticity_token'], safe='')
        data['SAMLResponse'] = quote(data['SAMLResponse'], safe='')
        data['RelayState'] = quote(data['RelayState'], safe='')

        new_data = ''.join('{}={}&'.format(key, val) for key, val in data.items())
        patched_data = (re.findall("^(.*?)&$", new_data))[0]
        # print("really is last " + c_saml_response)
        print("really is last data " + str(patched_data))
        # saml_url = base_url_2+"/saml/SSO/alias/"+alias_name
        # with RefererSession() as s:
        s.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
        r = s.post(url=base_url_2 + "/saml/SSO/alias/{0}".format(alias_name), data=patched_data, allow_redirects=False)
        print("never back " + str(r.text))
        print("never back " + str(r.url))
        # r = s.get(url=r.url, allow_redirects=True)
        # print("ahahahaha " + str(r.history[0].url))
        # print("ahahahaha " + str(r.history[1].url))
        # print("ahahahaha " + str(r.history[1].text))
        # print("ahahahaha " + str(r.history[1].content))
        # print("ahahahaha " + str(r.history[1].headers))

        param = {
            "response_type": "code",
            "client_id": str(client_id),
            "redirect_uri": quote("{0}/login/callback".format(base_url_1),safe='')
        }
        # with RefererSession() as s:
        param_new = ''.join('{}={}&'.format(key, val) for key, val in param.items())
        param_new = (re.findall("^(.*?)&$", param_new))[0]
        newest_url = base_url_2+"/oauth/authorize?"+param_new
        print("param new " + newest_url)
        r = s.get(url=newest_url, allow_redirects=True)
        # r = s.get(url=base_url_2 + "/oauth/authorize", params=param, allow_redirects=True)
        print("last sprint " + str(r.status_code))
        print("last sprint " + str(r.url))
        print("last sprint " + str(r.text))
        print("last sprint " + str(r.content))
        print("last sprint " + str(s.headers))
        print("last sprint " + str(s.cookies))
        c_code = (re.findall(".*?code=(.*?)\n*?", r.url))[0]
        param = {
            "code": c_code
        }
        # with RefererSession() as s:
        r = s.get(url=base_url_1 + "/login/callback", params=param, allow_redirects=True)

        print("response " + str(r.text))
        # print("mytext " + str(c_cookie_signature))
        # print("mytext " + str(c_cookie_signature.groups()))

        r = s.get(url=base_url_2 + "/passcode", allow_redirects=True)
        print("response " + str(r.content))
        print("response " + str(r.text))

        passcode = (re.findall("<h2><samp id=\"passcode\">(.*?)</samp>", r.text))[0]

        print("passcode " + str(passcode))


        BuiltIn().set_test_variable("${status_code}", r.status_code)
        return passcode
