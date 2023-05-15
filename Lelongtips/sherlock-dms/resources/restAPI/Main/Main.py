import math
import os
import secrets
import re
import time
from datetime import datetime

import googlemaps
from geopy.geocoders import Nominatim
import git
import gmaps
import requests
from bs4 import BeautifulSoup
# from folium import folium
import folium
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY, LLT_URL, LLT_TOKEN, GMAPS_TOKEN
# from resources.restAPI.Common import APIMethod

MAIN_URL = PROTOCOL + LLT_URL
gmaps = googlemaps.Client(key=GMAPS_TOKEN)



class Main(object):

    @keyword("user runs main flow")
    def user_runs_main_flow(self):
        # common = APIMethod.APIMethod()


        # response = common.trigger_api_request("GET", MAIN_URL + str(1), "")
        response = requests.get(
            url=MAIN_URL + str(1)
        )
        draft_content = []
        if response.status_code == 200:
            body_result = response.text
            page_no_upper = self.set_pages(body_result)
            draft_content = self.get_pages(page_no_upper)
            self.map_gen(draft_content)
            self.git_controls()
            print("Total number of records retrieved are ", len(body_result))
            print("Response body= ", str(body_result))
        else:
            raise Exception("Initial load failed")
        if draft_content:
            self.save_draft(draft_content)

    def map_gen(self, draft_content):
        m = folium.Map(location=(3.064119, 101.669488), tiles="OpenStreetMap", zoom_start=10)
        print(type(draft_content))
        # apijiu = (loc['address'] for loc in draft_content)
        print(str(asd) for asd in draft_content)
        # big_apijiu = re.findall(".*  (.*)\\n", apijiu)
        # loc = 'Taj Mahal, Agra, Uttar Pradesh 282001'
        # geolocator = Nominatim(user_agent="my_request")
        # location = geolocator.geocode(loc)
        # print(location.address)
        # print((location.latitude, location.longitude))
        # raise Exception("ehehe")
        print(str(draft_content))
        # raise Exception (type(draft_content))
        for i in draft_content[0]:
            # hi = hi + 1
            location = {}
            loc = i['address']
            formatted_address_name = None
            geolocator = Nominatim(user_agent="my_request")
            # location = geolocator.geocode(loc)
            geocode_result = gmaps.geocode(loc)
            # print(str(geocode_result))
            # if len(geocode_result[0]['address_components']) > 1 or geocode_result['status'] is not "OK":
            #     print("Please inspect and fix geocode= " + str(geocode_result))
            location_raw = geocode_result[0]['geometry']['location']
            formatted_address_name = geocode_result[0]['formatted_address']
            location.update({'latitude': location_raw['lat']})
            location.update({'longitude': location_raw['lng']})
            div_icon = None
            price = i['price']
            build_up = i['build_up']
            if not price or not build_up:
                div_icon = f"""
                                <div>
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M215.7 499.2C267 435 384 279.4 384 192C384 86 298 0 192 0S0 86 0 192c0 87.4 117 243 168.3 307.2c12.3 15.3 35.1 15.3 47.4 0zM192 128a64 64 0 1 1 0 128 64 64 0 1 1 0-128z"/></svg>
                                </div>"""
            else:
                price = float(price)
                build_up = float(build_up)
                if price/build_up >= 700:
                    continue
                elif price/build_up <= 300 and price <= 800000:
                    div_icon = f"""
                                    <div>
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L433.6 328.4l26.2 155.6c1.5 9-2.2 18.1-9.6 23.5s-17.3 6-25.3 1.7l-137-73.2L151 509.1c-8.1 4.3-17.9 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l26.2-155.6L31.1 218.2c-6.5-6.4-8.7-15.9-5.9-24.5s10.3-14.9 19.3-16.3l153.2-22.6L266.3 13.5C270.4 5.2 278.7 0 287.9 0zm0 79L235.4 187.2c-3.5 7.1-10.2 12.1-18.1 13.3L99 217.9 184.9 303c5.5 5.5 8.1 13.3 6.8 21L171.4 443.7l105.2-56.2c7.1-3.8 15.6-3.8 22.6 0l105.2 56.2L384.2 324.1c-1.3-7.7 1.2-15.5 6.8-21l85.9-85.1L358.6 200.5c-7.8-1.2-14.6-6.1-18.1-13.3L287.9 79z"/></svg>
                                    </div>"""
                elif re.findall(".*(torey).*", i['prop_type']) or re.findall(".*(tory).*", i['prop_type']):
                    div_icon = f"""
                                    <div>
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M543.8 287.6c17 0 32-14 32-32.1c1-9-3-17-11-24L512 185V64c0-17.7-14.3-32-32-32H448c-17.7 0-32 14.3-32 32v36.7L309.5 7c-6-5-14-7-21-7s-15 1-22 8L10 231.5c-7 7-10 15-10 24c0 18 14 32.1 32 32.1h32v69.7c-.1 .9-.1 1.8-.1 2.8V472c0 22.1 17.9 40 40 40h16c1.2 0 2.4-.1 3.6-.2c1.5 .1 3 .2 4.5 .2H160h24c22.1 0 40-17.9 40-40V448 384c0-17.7 14.3-32 32-32h64c17.7 0 32 14.3 32 32v64 24c0 22.1 17.9 40 40 40h24 32.5c1.4 0 2.8 0 4.2-.1c1.1 .1 2.2 .1 3.3 .1h16c22.1 0 40-17.9 40-40V455.8c.3-2.6 .5-5.3 .5-8.1l-.7-160.2h32z"/></svg>
                                    </div>"""
                else:
                    div_icon = f"""
                                    <div>
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M215.7 499.2C267 435 384 279.4 384 192C384 86 298 0 192 0S0 86 0 192c0 87.4 117 243 168.3 307.2c12.3 15.3 35.1 15.3 47.4 0zM192 128a64 64 0 1 1 0 128 64 64 0 1 1 0-128z"/></svg>
                                    </div>"""
            if not location:
                continue
            html = f"""
                <p> {{3}} </p>
                <h2> {{1}} </h2>
                <h1> {{0}} </h1>
                <p>Details:- </p>
                <ul>
                    <li>buildup {{2}}</li>
                    <li>RM {{4}}</li>
                    <li> {{5}} </li>
                    <li> {{6}} </li>
                    <li> {{7}} </li>                    
                </ul>
                </p>
                <p>And that's a <a href="{{8}}">link</a></p>
                """.format(i['prop_name'], i['prop_type'], build_up, i['date'], price, i['psf'], i['others'],
                           formatted_address_name, i['h_ref'])
            print(i['prop_name'] + " is this gg= " + html)

            iframe = folium.IFrame(html=html, width=400, height=300)
            # iframe = folium.IFrame(html=html, width='90%', height='90%')
            # folium.folium.Element.render()
            popup = folium.Popup(iframe, max_width=2650)
            # popup = folium.Popup(iframe)
            folium.Marker(
                location=(location['latitude'], location['longitude']),
                popup=popup,
                # icon=folium.DivIcon(html=f"""
                # <div><svg>
                #     <circle cx="50" cy="50" r="40" fill="#69b3a2" opacity=".4"/>
                #     <rect x="35", y="35" width="30" height="30", fill="red", opacity=".3"
                # </svg></div>""")

                #green
                # <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M215.7 499.2C267 435 384 279.4 384 192C384 86 298 0 192 0S0 86 0 192c0 87.4 117 243 168.3 307.2c12.3 15.3 35.1 15.3 47.4 0zM192 128a64 64 0 1 1 0 128 64 64 0 1 1 0-128z"/></svg>
                icon=folium.DivIcon(html=div_icon)
                # popup="hehe" + str(hi),
            ).add_to(m)
        date_now = str(datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"))
        date_file = re.sub(r'[^\w]', '', date_now)
        m.save(f"../../docs/index.html")
        # m.save(f"../../docs/LLT_" + date_file + ".html")

    def git_controls(self):
        save_folder = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
        repo = git.Repo(save_folder, search_parent_directories=True)  # ex. "/User/some_user/some_dir"
        repo.git.add(update=True)
        repo.index.commit("Update map html")
        origin = repo.remote(name='origin')
        origin.push()

        print("hi")

    def save_draft(self, draft_content):
        # common = APIMethod.APIMethod()
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
        # common = APIMethod.APIMethod()
        k = 0
        draft_content = []
        for i in range(1, int(page_no_upper)+1):
            response = requests.get(
                url=MAIN_URL + str(i)
            )
            # response = common.trigger_api_request("GET", MAIN_URL + str(i), "")
            body_result = response.text
            content_list = self.get_contents(body_result)
            draft_content.append(content_list)
            time.sleep(secrets.randbelow(10))
            k = k + 1
            if k > 1:
                break
            #     raise Exception("Test end")
        return draft_content

    def get_contents(self, body_text):
        parsed_html = BeautifulSoup(body_text)
        content_list = []
        contents_raw = parsed_html.body.find_all('div', attrs={'class': 'col details-col flex-grow-1'})
        for i in contents_raw:
            print("iii= " + str(i))
            content_details = {}
            content_details['address'] = self.handle_value(i, 'h5', 'class', "fw-bold crop-text-3 mb-0")
            content_details['prop_name'] = self.handle_value(i, 'p', 'class', "text-muted mb-0 text-truncate")
            content_details['prop_type'] = self.handle_value(i, 'p', 'class', "text-info crop-text-2 list-none mb-2")
            raw_str = re.findall("(\d+)", str(self.handle_value(i, 'div', 'class', "fs-5 mb-1 me-2 me-md-1 me-lg-2 list-none")))
            if raw_str:
                build_up_raw = ''.join(raw_str)
            else:
                build_up_raw = None
            # print("builup raw= " + build_up_raw)
            content_details['build_up'] = build_up_raw
            content_details['date'] = self.handle_value(i, 'div', 'class', "fs-6 d-block fw-bold")
            content_details['price'] = ''.join(re.findall("\d+", self.handle_value(i, 'h4', 'class', "fw-bold text-nowrap d-flex flex-row flex-sm-column position-relative")))
            psf_raw = self.handle_value(i, 'div', 'class', 'fs-5 mb-1 me-2 me-md-1 me-lg-2 grid-none')
            psf = re.findall("\d+", psf_raw[0] if psf_raw else "0")
            content_details['psf'] = ''.join(psf)
            content_details['others'] = self.handle_value(i, 'td', 'class', "position-relative")
            content_details['h_ref'] = self.handle_value(i, 'a', 'class', "stretched-link")
            # content_details['tenure'] = re.findall()
            # content_details['psf'] = i.find('div', attrs={'class': 'fs-5 mb-1 me-2 me-md-1 me-lg-2 grid-none'}).text
            # content_details['restriction'] = i.find('div', attrs={'class': 'fs-5 mb-1 me-2 me-md-1 me-lg-2 grid-none list-none'}).text
            content_details['restriction'] = self.handle_value(i, 'div', 'class', 'fs-5 mb-1 me-2 me-md-1 me-lg-2 grid-none list-none')
            content_list.append(content_details)
            print("content_details= " + str(content_details))
            counter = 0
            # for i in content_details

            # print("testitem " + str(content_list))
        return content_list
        # print(parsed_html.body.find('div', attrs={'class': 'col details-col flex-grow-1'}).text)

    def handle_value(self, i, name_div, name_class, name_subclass):
        value = None
        if i.find(name_div, attrs={name_class: name_subclass}):
            value = i.find(name_div, attrs={name_class: name_subclass}).text.strip()
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
