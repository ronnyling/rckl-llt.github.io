import math
import os
import secrets
import re
import time
from datetime import datetime

import googlemaps
from folium.plugins import MarkerCluster
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
            # print("Total number of records retrieved are ", len(body_result))
            # print("Response body= ", str(body_result))
        else:
            raise Exception("Initial load failed")
        if draft_content:
            self.save_draft(draft_content)

    def map_gen(self, draft_content):
        m = folium.Map(location=(3.064119, 101.669488), tiles="OpenStreetMap", zoom_start=10)
        # map = folium.Map(location=[0, 0], zoom_start=4)
        fg_l = folium.FeatureGroup(name='Landed', show=False)
        fg_lrd = folium.FeatureGroup(name='Low Risk Deals', show=False)
        fg_gptd = folium.FeatureGroup(name='GPT Deals', show=False)
        fg_o = folium.FeatureGroup(name='Others', show=False)
        html = '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <title>sidebar-v2 example</title>
            
                <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
                <meta charset="utf-8">
            
                <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
                <link rel="stylesheet" href="https://unpkg.com/leaflet@1.0.1/dist/leaflet.css" />
                <!--[if lte IE 8]><link rel="stylesheet" href="https://cdn.leafletjs.com/leaflet-0.7.2/leaflet.ie.css" /><![endif]-->
            
                <link rel="stylesheet" href="../Lelongtips/sherlock-dms/resources/components/leaflet-sidebar.css" />
            
                <style>
                    body {
                        padding: 0;
                        margin: 0;
                    }
            
                    html, body, #map {
                        height: 100%;
                        font: 10pt "Helvetica Neue", Arial, Helvetica, sans-serif;
                    }
            
                    .lorem {
                        font-style: italic;
                        color: #AAA;
                    }
                </style>
            </head>
            <body>
                <div id="sidebar" class="sidebar collapsed">
                    <!-- Nav tabs -->
                    <div class="sidebar-tabs">
                        <ul role="tablist">
                            <li><a href="#home" role="tab"><i class="fa fa-bars"></i></a></li>
                            <li><a href="#profile" role="tab"><i class="fa fa-user"></i></a></li>
                            <li class="disabled"><a href="#messages" role="tab"><i class="fa fa-envelope"></i></a></li>
                            <li><a href="https://github.com/Turbo87/sidebar-v2" role="tab" target="_blank"><i class="fa fa-github"></i></a></li>
                        </ul>
            
                        <ul role="tablist">
                            <li><a href="#settings" role="tab"><i class="fa fa-gear"></i></a></li>
                        </ul>
                    </div>
            
                    <!-- Tab panes -->
                    <div class="sidebar-content">
                        <div class="sidebar-pane" id="home">
                            <h1 class="sidebar-header">
                                sidebar-v2
                                <span class="sidebar-close"><i class="fa fa-caret-left"></i></span>
                            </h1>
            
                            <p>A responsive sidebar for mapping libraries like <a href="http://leafletjs.com/">Leaflet</a> or <a href="http://openlayers.org/">OpenLayers</a>.</p>
            
                            <p class="lorem">Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.</p>
            
                            <p class="lorem">Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.</p>
            
                            <p class="lorem">Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.</p>
            
                            <p class="lorem">Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.</p>
                        </div>
            
                        <div class="sidebar-pane" id="profile">
                            <h1 class="sidebar-header">Profile<span class="sidebar-close"><i class="fa fa-caret-left"></i></span></h1>
                        </div>
            
                        <div class="sidebar-pane" id="messages">
                            <h1 class="sidebar-header">Messages<span class="sidebar-close"><i class="fa fa-caret-left"></i></span></h1>
                        </div>
            
                        <div class="sidebar-pane" id="settings">
                            <h1 class="sidebar-header">Settings<span class="sidebar-close"><i class="fa fa-caret-left"></i></span></h1>
                        </div>
                    </div>
                </div>
            
                <div id="map" class="sidebar-map"></div>
            
                <a href="https://github.com/Turbo87/sidebar-v2/"><img style="position: fixed; top: 0; right: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_right_darkblue_121621.png" alt="Fork me on GitHub"></a>
            
                <script src="https://unpkg.com/leaflet@1.0.1/dist/leaflet.js"></script>
                <script src="../Lelongtips/sherlock-dms/resources/components/leaflet-sidebar.js"></script>
            
                <script>
                    var map = L.map('map');
                    map.setView([51.2, 7], 9);
            
                    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                        maxZoom: 18,
                        attribution: 'Map data &copy; OpenStreetMap contributors'
                    }).addTo(map);
            
                    var marker = L.marker([51.2, 7]).addTo(map);
            
                    var sidebar = L.control.sidebar('sidebar').addTo(map);
                </script>
            </body>
            </html>
        '''
        # sidebar = folium.Div()
        # sidebar.html(html)
        # sidebar = folium.Html(data=html, script=True)
        # m.add_child(folium.CssLink('../Lelongtips/sherlock-dms/resources/components/leaflet-sidebar.css'))
        # m.add_child(folium.JavascriptLink('../Lelongtips/sherlock-dms/resources/components/leaflet-sidebar.js'))
        # m.get_root().html.add_child(sidebar)
        # m.get_root().html.add_child(Element(html))

        # sidebar_html = m.add_child(sidebar)
        # folium.Div().add_to(sidebar_html)

        html = """
        <div style="position:fixed;
                    top:10px;
                    right:10px;
                    z-index:1000;
                    background-color:white;
                    padding:10px;">
            <h4>Custom Sidebar</h4>
            <p>This is a custom sidebar added using Folium.</p>
            <p>You can add any HTML content here.</p>
        </div>
        """
        html2 = """
        <div style="position:fixed;
                    top:10px;
                    right:10px;
                    z-index:1000;
                    background-color:white;
                    padding:10px;">
            <h4>Custom Sidebar</h4>
            <p>This is a custom sidebar added using Folium.</p>
            <p>You can add any HTML content here.</p>
        </div>
        """

        # Create a custom HTML element
        sidebar = folium.Html(html)

        # css_link = CssLink(css_file)
        # js_link = JsLink(js_file)
        fig = folium.Figure()
        # fig.add_child(container)
        fig.add_child(sidebar)
        fig.add_child(m)
        container = folium.Element()
        container.add_child(fig)
        # fig.add_child(css_link)
        # fig.add_child(js_link)

        m.add_child(fg_l)
        m.add_child(fg_lrd)
        m.add_child(fg_gptd)
        m.add_child(fg_o)
        marker_cluster_l = MarkerCluster().add_to(fg_l)
        marker_cluster_lrd = MarkerCluster().add_to(fg_lrd)
        marker_cluster_gptd = MarkerCluster().add_to(fg_gptd)
        marker_cluster_o = MarkerCluster().add_to(fg_o)
        folium.LayerControl().add_to(m)
        # sidebar = folium.plugins.FloatSidebar(
        #     position='left',
        #     title='Cities',
        #     pane='sidebar'
        # ).add_to(m)

        print("draft_content= " + str(len(draft_content)))
        print("draft_content[0]= " + str(len(draft_content[0])))
        for j in draft_content:
            for i in j:
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
                                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M47.6 300.4L228.3 469.1c7.5 7 17.4 10.9 27.7 10.9s20.2-3.9 27.7-10.9L464.4 300.4c30.4-28.3 47.6-68 47.6-109.5v-5.8c0-69.9-50.5-129.5-119.4-141C347 36.5 300.6 51.4 268 84L256 96 244 84c-32.6-32.6-79-47.5-124.6-39.9C50.5 55.6 0 115.2 0 185.1v5.8c0 41.5 17.2 81.2 47.6 109.5z"/></svg>
                                        </div>"""
                    elif i['prop_type'] and (re.findall(".*(torey).*", i['prop_type']) or re.findall(".*(tory).*", i['prop_type'])):
                        div_icon = f"""
                                    <div>
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M543.8 287.6c17 0 32-14 32-32.1c1-9-3-17-11-24L512 185V64c0-17.7-14.3-32-32-32H448c-17.7 0-32 14.3-32 32v36.7L309.5 7c-6-5-14-7-21-7s-15 1-22 8L10 231.5c-7 7-10 15-10 24c0 18 14 32.1 32 32.1h32v69.7c-.1 .9-.1 1.8-.1 2.8V472c0 22.1 17.9 40 40 40h16c1.2 0 2.4-.1 3.6-.2c1.5 .1 3 .2 4.5 .2H160h24c22.1 0 40-17.9 40-40V448 384c0-17.7 14.3-32 32-32h64c17.7 0 32 14.3 32 32v64 24c0 22.1 17.9 40 40 40h24 32.5c1.4 0 2.8 0 4.2-.1c1.1 .1 2.2 .1 3.3 .1h16c22.1 0 40-17.9 40-40V455.8c.3-2.6 .5-5.3 .5-8.1l-.7-160.2h32z"/></svg>
                                    </div>"""
                        i['tags'] = "l"
                    else:
                        div_icon = f"""
                                        <div>
                                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M215.7 499.2C267 435 384 279.4 384 192C384 86 298 0 192 0S0 86 0 192c0 87.4 117 243 168.3 307.2c12.3 15.3 35.1 15.3 47.4 0zM192 128a64 64 0 1 1 0 128 64 64 0 1 1 0-128z"/></svg>
                                        </div>"""
                    if price < 300000:
                        i['tags'] = "lrd"

                if not location:
                    continue
                add_marker = None
                if i['tags'] == "l":
                    add_marker = marker_cluster_l
                elif i['tags'] == "lrd":
                    add_marker = marker_cluster_lrd
                else:
                    add_marker = marker_cluster_o

                iframe_target = str(i['prop_name'])
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
                    <p>And that's a <a href="{{8}}" target=window.name>link</a></p>
                    """.format(i['prop_name'], i['prop_type'], build_up, i['date'], price, i['psf'], i['others'],
                               formatted_address_name, i['h_ref'], iframe_target)
                # print(i['prop_name'] + " is this gg= " + html)
                iframe = folium.IFrame(html=html, width=300, height=200)
                # iframe.add_child(iframe.get_name())
                # iframe_name = iframe.get_name()
                # print("iframe name= " + iframe_name)
                # iframe = folium.IFrame(html=html, width='90%', height='90%')
                # folium.folium.Element.render()
                popup = folium.Popup(iframe, max_width=2650)

                # popup = folium.Popup(iframe)
                folium.Marker(
                    location=(location['latitude'], location['longitude']),
                    popup=popup,
                    icon=folium.DivIcon(html=div_icon)
                ).add_to(add_marker)
                folium.Marker(
                    location=(location['latitude'], location['longitude']),
                    popup=popup,
                    icon=folium.DivIcon(html=div_icon)
                ).add_to(sidebar)
        date_now = str(datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"))
        date_file = re.sub(r'[^\w]', '', date_now)
        # m.save(f"../../docs/index.html")
        # fig.save(f"../../docs/index.html")
        container.save(f"../../docs/index.html")
        # m.save(f"../../docs/LLT_" + date_file + ".html")

    def git_controls(self):
        save_folder = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
        repo = git.Repo(save_folder, search_parent_directories=True)  # ex. "/User/some_user/some_dir"
        repo.git.add(update=True)
        repo.index.commit("Update map html")
        origin = repo.remote(name='origin')
        origin.push()

        # print("hi")

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
            # print(response.text)
            if response.status_code == 200:
                response_json = response.json()
                # url = response_json["data"]["url"]
                # print(url)
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
            print("now i am at page " + str(i))
            response = requests.get(
                url=MAIN_URL + str(i)
            )
            # response = common.trigger_api_request("GET", MAIN_URL + str(i), "")
            body_result = response.text
            content_list = self.get_contents(body_result)
            print("size of content_list= " + str(len(content_list)))
            print("size of draft_content= " + str(len(draft_content)))
            draft_content.append(content_list)
            sleep_time = secrets.choice(range(5, 10))
            # print("i've slept for seconds= " + str(k) +" "+ str(sleep_time))
            time.sleep(sleep_time)
            k = k + 1
            if k > 0:
                break
            #     raise Exception("Test end")
        return draft_content

    def get_contents(self, body_text):
        parsed_html = BeautifulSoup(body_text)
        content_list = []
        contents_raw = parsed_html.body.find_all('div', attrs={'class': 'col details-col flex-grow-1'})
        for i in contents_raw:
            # print("iii= " + str(i))
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
            content_details['h_ref'] = re.findall(".*<a class=\"stretched-link\" href=\"(.*)\" title=.*", str(i))[0]
            content_details['restriction'] = self.handle_value(i, 'div', 'class', 'fs-5 mb-1 me-2 me-md-1 me-lg-2 grid-none list-none')
            tag = None

            content_details['tags'] = tag
            content_list.append(content_details)
            # print("content_details= " + str(content_details))
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
        # print("hi " + str(page_no_upper))
        return page_no_upper


        #     if len(body_result) > 1:
        #         rand_claims = secrets.choice(range(0, len(body_result)))
        #     else:
        #         rand_claims = 0
        #     BuiltIn().set_test_variable("${rand_claims_selection}", body_result[rand_claims]["ID"])
        # BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
