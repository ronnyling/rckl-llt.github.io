import math
import secrets
import re
import time

import gmaps
import requests
from bs4 import BeautifulSoup
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY, LLT_URL, LLT_TOKEN
from resources.restAPI.Common import APIMethod

MAIN_URL = PROTOCOL + LLT_URL



class Main(object):

    @keyword("user runs main flow")
    def user_runs_main_flow(self):
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", MAIN_URL + str(1), "")
        draft_content = []
        if response.status_code == 200:
            body_result = response.text
            page_no_upper = self.set_pages(body_result)
            draft_content = self.get_pages(page_no_upper)
            print("Total number of records retrieved are ", len(body_result))
            print("Response body= ", str(body_result))
        else:
            raise Exception("Initial load failed")
        if draft_content:
            self.save_draft(draft_content)

    def save_draft(self, draft_content):
        common = APIMethod.APIMethod()
        url = "https://api.medium.com/v1"
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Host": "api.medium.com",
            "TE": "Trailers",
            "Authorization": f"Bearer {LLT_TOKEN}",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
        }
        data = {
            "title": "This is title",
            "contentFormat": "html",
            "content": "<h1>hihi</h1><p>" + str(draft_content) + "</p>\n \n \n <p>https://codepen.io/Meet-Ronny/pen/xxyWeNG</p>",
            "tags": ["development", "design"],
            "publishStatus": "draft"  # "public" will publish to gibubfor putting draft use value "draft"
        }
        # response = common.trigger_api_request("GET", url + "/me", "", params={"accessToken": LLT_TOKEN})

        # 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

        response = requests.get(
            url=url + "/me",  # https://api.medium.com/me
            headers=header,
            params={"accessToken": LLT_TOKEN},
        )
        if response.status_code == 200:
            response_json = response.json()
            userId = response_json["data"]["id"]
            # response = common.trigger_api_request("POST", f"{url}/users/{userId}/posts", data,
            #                                       headers=header)
            response = requests.post(
                url=f"{url}/users/{userId}/posts",  # https://api.medium.com/me/users/{userId}/posts
                headers=header,
                data=data
            )
            print(response.text)
            if response.status_code == 200:
                response_json = response.json()
                url = response_json["data"]["url"]
                print(url)
    def get_gmaps(self):
        gmaps.configure(api_key='AI...')
        nuclear_power_plants = [
            {'name': 'Atucha', 'location': (-34.0, -59.167), 'active_reactors': 1},
            {'name': 'Embalse', 'location': (-32.2333, -64.4333), 'active_reactors': 1},
            {'name': 'Armenia', 'location': (40.167, 44.133), 'active_reactors': 1},
            {'name': 'Br', 'location': (51.217, 5.083), 'active_reactors': 1},
            {'name': 'Doel', 'location': (51.333, 4.25), 'active_reactors': 4},
            {'name': 'Tihange', 'location': (50.517, 5.283), 'active_reactors': 3}
        ]
        plant_locations = [plant['location'] for plant in nuclear_power_plants]
        info_box_template = """
        <dl>
        <dt>Name</dt><dd>{name}</dd>
        <dt>Number reactors</dt><dd>{active_reactors}</dd>
        </dl>
        """
        plant_info = [info_box_template.format(**plant) for plant in nuclear_power_plants]
        marker_layer = gmaps.marker_layer(plant_locations, info_box_content=plant_info)
        fig = gmaps.figure()
        fig.add_layer(marker_layer)
        fig

    def get_pages(self, page_no_upper):
        common = APIMethod.APIMethod()
        k = 0
        draft_content = []
        for i in range(1, int(page_no_upper)+1):
            response = common.trigger_api_request("GET", MAIN_URL + str(i), "")
            body_result = response.text
            content_list = self.get_contents(body_result)
            draft_content.extend(content_list)
            time.sleep(secrets.randbelow(10))
            k = k + 1
            if k > 2:
                break
                raise Exception("Test end")
        return draft_content

    def get_contents(self, body_text):
        parsed_html = BeautifulSoup(body_text)
        content_list = []
        contents_raw = parsed_html.body.find_all('div', attrs={'class': 'col details-col flex-grow-1'})
        for i in contents_raw:
            # print("i= " + str(i))
            content_details = {}
            content_details['address'] = self.handle_value(i, 'h5', 'class', "fw-bold crop-text-3 mb-0")
            content_details['prop_name'] = self.handle_value(i, 'p', 'class', "text-muted mb-0 text-truncate")
            content_details['prop_type'] = self.handle_value(i, 'p', 'class', "text-info crop-text-2 list-none mb-2")
            content_details['build_up'] = self.handle_value(i, 'div', 'class', "fs-5 mb-1 me-2 me-md-1 me-lg-2 list-none")
            content_details['date'] = self.handle_value(i, 'div', 'class', "fs-6 d-block fw-bold")
            content_details['price'] = self.handle_value(i, 'h4', 'class', "fw-bold text-nowrap d-flex flex-row flex-sm-column position-relative")
            content_details['psf'] = self.handle_value(i, 'div', 'class', 'fs-5 mb-1 me-2 me-md-1 me-lg-2 grid-none')
            content_details['others'] = self.handle_value(i, 'td', 'class', "position-relative")
            # content_details['tenure'] = re.findall()
            # content_details['psf'] = i.find('div', attrs={'class': 'fs-5 mb-1 me-2 me-md-1 me-lg-2 grid-none'}).text
            # content_details['restriction'] = i.find('div', attrs={'class': 'fs-5 mb-1 me-2 me-md-1 me-lg-2 grid-none list-none'}).text
            content_details['restriction'] = self.handle_value(i, 'div', 'class', 'fs-5 mb-1 me-2 me-md-1 me-lg-2 grid-none list-none')
            content_list.append(content_details)
            print("content_details= " + str(content_details))
        return content_list
        # print(parsed_html.body.find('div', attrs={'class': 'col details-col flex-grow-1'}).text)

    def handle_value(self, i, name_div, name_class, name_subclass):
        value = None
        if i.find(name_div, attrs={name_class: name_subclass}):
            value = i.find(name_div, attrs={name_class: name_subclass}).text
        return value

    def set_pages(self, body_text):
        page_no_raw = re.findall(r"Result\(s\): (.*)</p>", body_text)[0]
        page_no_refined = re.findall("(\d)", page_no_raw)
        page_no = ''.join(i for i in page_no_refined)
        page_no_upper = math.ceil(int(page_no)/12)
        print("hi " + str(page_no_upper))
        return page_no_upper


        #     if len(body_result) > 1:
        #         rand_claims = secrets.choice(range(0, len(body_result)))
        #     else:
        #         rand_claims = 0
        #     BuiltIn().set_test_variable("${rand_claims_selection}", body_result[rand_claims]["ID"])
        # BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
