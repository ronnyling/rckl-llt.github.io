import json
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
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY, LLT_URL, LLT_TOKEN, GMAPS_TOKEN, PHONE_ID, TOKEN, NUMBER, \
    MESSAGE, TEST_URL

# from resources.restAPI.Common import APIMethod

MAIN_URL_LLT = PROTOCOL + LLT_URL
# TEST_URL_LLT = PROTOCOL + TEST_URL
# MAIN_URL_IP = PROTOCOL + IP_URL
gmaps = googlemaps.Client(key=GMAPS_TOKEN)
icon_url_durian_runtuh_attention = 'https://i0.wp.com/www.exabytes.com/blog/wp-content/uploads/2010/05/blog-durianruntuh-5.jpg'
icon_url_durian_runtuh_landed = 'https://cdn.dribbble.com/users/1370570/screenshots/6180828/media/3de2eda53bad9fc0e604b1e328e44716.png'
icon_url_durian_runtuh_expired_nobidder = "https://image.shutterstock.com/image-vector/vector-cute-durian-cartoon-style-260nw-2305237017.jpg"
icon_url_durian_runtuh_lrd = "https://image.shutterstock.com/image-vector/vector-cute-durian-cartoon-style-260nw-2305237019.jpg"
icon_url_durian_runtuh_others = "https://image.shutterstock.com/image-vector/vector-cute-durian-cartoon-style-260nw-2305237021.jpg"
icon_0_1 = "https://raw.githubusercontent.com/ronnyling/rckl-llt.github.io/main/Lelongtips/docs/0_1.png"
icon_0_2 = "https://raw.githubusercontent.com/ronnyling/rckl-llt.github.io/main/Lelongtips/docs/0_2.png"
icon_0_3 = "https://raw.githubusercontent.com/ronnyling/rckl-llt.github.io/main/Lelongtips/docs/0_3.png"
icon_size_s = (70, 35)
icon_size = (35, 35)
today_date = datetime.today().date()
testing = True


class Main(object):

    @keyword("user runs main flow")
    def user_runs_main_flow(self):
        # self.iprop_scrape()
        # self.lelongtips_scrape_demo()
        self.lelongtips_scrape()

    def notify_me(self):

        URL = "https://graph.facebook.com/v13.0/" + PHONE_ID + "/messages"
        headers = {
            "Authorization": "Bearer " + TOKEN,
            "Content-Type": "application/json"
        }
        data = {
            "messaging_product": "whatsapp",
            "to": NUMBER,
            "type": "text",
            "text": json.dumps({"preview_url": False, "body": MESSAGE})
        }
        response = requests.post(URL, headers=headers, data=data)
        response_json = response.json()
        print(response_json)

    def lelongtips_scrape(self):
        operating_url = MAIN_URL_LLT
        if testing and TEST_URL:
            operating_url = PROTOCOL + TEST_URL

        # print("url = xx" + str(operating_url) + " xx " + str(MAIN_URL_LLT) + " xx " + str(TEST_URL_LLT))
        response = requests.get(
            url=operating_url + str(1)
        )
        draft_content = []
        if response.status_code == 200:
            body_result = response.text
            page_no_upper = self.set_pages(body_result)
            draft_content = self.get_pages(page_no_upper, operating_url)
            self.map_gen(draft_content)
            self.git_controls()
            self.notify_me()
            # print("Total number of records retrieved are ", len(body_result))
            # print("Response body= ", str(body_result))
        else:
            raise Exception("Initial load failed")
        # if draft_content:
        #     self.save_draft(draft_content)

    def lelongtips_scrape_demo(self):
        long = 3.064119
        lat = 101.669488
        x = 0.05
        m = folium.Map(location=(long, lat), tiles="OpenStreetMap", zoom_start=10,control_scale=True)
        fg_l = folium.FeatureGroup(name='Landed', show=False)
        fg_lrd = folium.FeatureGroup(name='Low Risk Deals', show=False)
        # m.add_child(fg_l)
        fg_l.add_to(m)
        fg_lrd.add_to(m)
        # m.add_child(fg_lrd)
        marker_cluster_l = folium.plugins.MarkerCluster().add_to(fg_l)
        marker_cluster_lrd = folium.plugins.MarkerCluster().add_to(fg_lrd)
        html = f"""
            <p> Sample </p>
            """
        iframe = folium.IFrame(html=html, width=300, height=200)
        popup = folium.Popup(iframe, max_width=2650)

        icon_file = f"""
                        <div>
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M215.7 499.2C267 435 384 279.4 384 192C384 86 298 0 192 0S0 86 0 192c0 87.4 117 243 168.3 307.2c12.3 15.3 35.1 15.3 47.4 0zM192 128a64 64 0 1 1 0 128 64 64 0 1 1 0-128z"/></svg>
                        </div>"""
        div_icon = folium.DivIcon(html=icon_file, icon_size=icon_size)
    # marker_cluster_o.add_child(
        marker_cluster_l.add_child(folium.Marker(
            location=(long + x, lat + x),
            popup=popup,
            icon=div_icon
        ))

        div_icon = folium.features.CustomIcon(icon_url_durian_runtuh_lrd, icon_size=icon_size)
        (folium.Marker(
            location=(long + x*2, lat + x*2),
            popup=popup,
            icon=div_icon
        )).add_to(marker_cluster_lrd)
        folium.LayerControl().add_to(m)
        m.save(f"../../docs/fixit.html")

        map = folium.Map(location=[0, 0], zoom_start=4)
        fg = folium.FeatureGroup(name='My Points', show=False)
        fg1 = folium.FeatureGroup(name='My Points1', show=False)
        map.add_child(fg)
        map.add_child(fg1)
        marker_cluster = MarkerCluster().add_to(fg)
        marker_cluster1 = MarkerCluster().add_to(fg1)
        folium.TileLayer('openstreetmap').add_to(map)
        folium.TileLayer('Stamen Terrain').add_to(map)
        info = 'test'
        folium.Marker(location=[long, lat], popup=info).add_to(marker_cluster)
        folium.Marker(location=(long + x, lat + x), popup=info).add_to(marker_cluster1)

        fg2 = folium.FeatureGroup(name='My Points2', show=False)
        map.add_child(fg2)
        marker_cluster2 = MarkerCluster()
        fg2.add_child(marker_cluster2)
        marker2 = folium.Marker(location=(long + x, lat + x), popup=info, icon=div_icon)
        marker_cluster2.add_child(marker2)
        # print("huehue " + map.to_json())
        folium.LayerControl().add_to(map)
        print("huehue " + map.to_json())

        map.save(f"../../docs/fixit.html")



    def map_gen(self, draft_content):
        m = folium.Map(location=(3.064119, 101.669488), tiles="OpenStreetMap", zoom_start=10,control_scale=True)
        # m = self.add_sidebar(m)
        # map = folium.Map(location=[0, 0], zoom_start=4)
        fg_l = folium.FeatureGroup(name='Landed', show=False)
        fg_lrd = folium.FeatureGroup(name='Low Risk Deals', show=False)
        fg_att = folium.FeatureGroup(name='Attention', show=False)
        fg_o = folium.FeatureGroup(name='ALL', show=False)
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
        css_link = folium.CssLink('../Lelongtips/sherlock-dms/resources/components/leaflet-sidebar.css')
        js_link = folium.JavascriptLink('../Lelongtips/sherlock-dms/resources/components/leaflet-sidebar.js')
        # m.get_root().html.add_child(sidebar)
        # m.get_root().html.add_child(Element(html))

        # sidebar_html = m.add_child(sidebar)
        # folium.Div().add_to(sidebar_html)

        html = """
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
        """
        html2 = """
        <div style="position:fixed;
                    top:10px;
                    right:10px;
                    z-index:2000;
                    background-color:white;
                    padding:10px;">
            <h4>Custom Sidebar</h4>
            <p>This is a custom sidebar added using Folium.</p>
            <p>You can add any HTML content here.</p>
        </div>
        """

        # Create a custom HTML element
        # sidebar = folium.Html(html)
        # container = folium.Element()
        # container.add_child(sidebar)
        # container.add_child(m)
        # css_link = CssLink(css_file)
        # js_link = JsLink(js_file)
        # fig = folium.Figure()
        # fig.add_child(container)
        # fig.add_child(container)
        # fig.add_child(m)
        # container.add_child(fig)
        # container.add_child(css_link)
        # container.add_child(js_link)
        m.get_root().header.add_child(css_link)
        m.get_root().html.add_child(js_link)
        # m.get_root().html.add_child(sidebar)
        # m.get_root().html.add_child(html)
        # m.html.add_child(container)
        # m.get_root().html.add_child(fig)
        # fg_search = folium.FeatureGroup(html)
        # folium.plugins.Search(layer=fg_search, search_label="Codice").add_to(m)

        m.add_child(fg_l)
        m.add_child(fg_lrd)
        m.add_child(fg_att)
        m.add_child(fg_o)

        marker_cluster_l = MarkerCluster()
        fg_l.add_child(marker_cluster_l)
        marker_cluster_lrd = MarkerCluster()
        fg_lrd.add_child(marker_cluster_lrd)
        marker_cluster_attention = MarkerCluster()
        fg_att.add_child(marker_cluster_attention)
        marker_cluster_o = MarkerCluster()
        fg_o.add_child(marker_cluster_o)

        folium.LayerControl().add_to(m)

        # marker_cluster_l = folium.plugins.MarkerCluster()
        # marker_cluster_lrd = folium.plugins.MarkerCluster()
        # marker_cluster_attention = folium.plugins.MarkerCluster()
        # marker_cluster_o = folium.plugins.MarkerCluster()


        # marker_cluster_l.add_to(fg_l)
        # marker_cluster_lrd.add_to(fg_lrd)
        # marker_cluster_attention.add_to(fg_att)
        # marker_cluster_o.add_to(fg_o)

        # flag_l = False
        # flag_lrd = False
        # flag_attention = False
        # flag_o = False

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
                try:
                    location_raw = geocode_result[0]['geometry']['location']
                except:
                    continue
                formatted_address_name = geocode_result[0]['formatted_address']
                location.update({'latitude': location_raw['lat']})
                location.update({'longitude': location_raw['lng']})
                div_icon = None
                price = i['price']
                build_up = i['build_up']
                print("prior to storm " + str(price) + " " + str(build_up))

                iframe_target = str(i['prop_name'])
                html = f"""
                    <p> {{3}} </p>
                    <p> RM {{4}} </p>
                    {{1}}
                    <h1> {{0}} </h1>
                    <p>Details:- </p>
                    <ul>
                        <li>buildup= {{2}}</li>
                        <li>others= {{6}} </li>
                        <li> status= {{5}} </li>
                        <li>FormattedAddress= {{7}} </li>                    
                    </ul>
                    </p>
                    <p>More details  <a href="{{8}}" target=window.name> click here </a></p>
                    """.format(i['prop_name'],
                               '<h2> ' + i['prop_type'] + ' </h2>' if i['prop_type'] else '',
                               build_up,
                               i['date'],
                               price,
                               i['listing_status'],
                               i['others'],
                               formatted_address_name,
                               i['h_ref'],
                               iframe_target)
                iframe = folium.IFrame(html=html, width=300, height=200)
                popup = folium.Popup(iframe, max_width=2650)

                if not price or not build_up:
                    # print("i am in not price " + html)
                    icon_file = f"""
                                    <div>
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M215.7 499.2C267 435 384 279.4 384 192C384 86 298 0 192 0S0 86 0 192c0 87.4 117 243 168.3 307.2c12.3 15.3 35.1 15.3 47.4 0zM192 128a64 64 0 1 1 0 128 64 64 0 1 1 0-128z"/></svg>
                                    </div>"""
                    div_icon = folium.DivIcon(html=icon_file, icon_size=icon_size)
                    add_marker = folium.Marker(
                                    location=(location['latitude'], location['longitude']),
                                    popup=popup,
                                    icon=div_icon
                                )
                    marker_cluster_o.add_child(add_marker)
                    # ).add_to(marker_cluster_o)
                    # )
                else:
                    # print("i am in okay price " + html)
                    price = float(price)
                    build_up = float(build_up)
                    if price < 300000 and not i['tags'] == 'attention':
                        i['tags'] = "lrd"
                        # add_marker = folium.Marker(
                        #                 location=(location['latitude'], location['longitude']),
                        #                 popup=popup,
                        #                 icon=div_icon
                        #             )
                        # marker_cluster_lrd.add_child(add_marker)

                    if i['tags'] == "attention":
                        div_icon = folium.features.CustomIcon(icon_0_1,
                                                              icon_size=icon_size_s)
                        if i['listing_status']:
                            div_icon = folium.features.CustomIcon(icon_url_durian_runtuh_expired_nobidder,
                                                                  icon_size=icon_size)
                            # div_icon = f"""
                            #             <div>
                            #             <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="-25 -25 550.00 550.00" xml:space="preserve" width="32px" height="32px" fill="#000000" transform="rotate(0)"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round" stroke="#CCCCCC" stroke-width="100"> <style type="text/css"> .st0{{fill:#0d0d0d;stroke:#0d0d0d;stroke-width:50;stroke-miterlimit:10;}} .st1{{fill:#FFED1F;}} .st2{{fill:#E32B43;}} </style> <g id="border"> <path class="st0" d="M454.7,403.9L266.2,77.4c-7.2-12.4-25.1-12.4-32.3,0L45.3,403.9c-7.2,12.4,1.8,28,16.2,28h377.1 C452.9,431.9,461.9,416.4,454.7,403.9z"></path> </g> <g id="object" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:svg="http://www.w3.org/2000/svg"> <g> <path class="st1" d="M232,80.6L47.2,400.7c-8,13.9,2,31.2,18,31.2h369.6c16,0,26-17.3,18-31.2L268,80.6 C260,66.7,240,66.7,232,80.6z"></path> <path class="st2" d="M250,152.2c-21.2,0-38.4,19.6-38.4,43.8c0,73.8,17.2,133.6,38.4,133.6s38.4-59.8,38.4-133.6 C288.4,171.8,271.2,152.2,250,152.2z"></path> <circle class="st2" cx="250" cy="379.9" r="26.9"></circle> </g> </g> </g><g id="SVGRepo_iconCarrier"> <style type="text/css"> .st0{{fill:#0d0d0d;stroke:#0d0d0d;stroke-width:50;stroke-miterlimit:10;}} .st1{{fill:#FFED1F;}} .st2{{fill:#E32B43;}} </style> <g id="border"> <path class="st0" d="M454.7,403.9L266.2,77.4c-7.2-12.4-25.1-12.4-32.3,0L45.3,403.9c-7.2,12.4,1.8,28,16.2,28h377.1 C452.9,431.9,461.9,416.4,454.7,403.9z"></path> </g> <g id="object" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:svg="http://www.w3.org/2000/svg"> <g> <path class="st1" d="M232,80.6L47.2,400.7c-8,13.9,2,31.2,18,31.2h369.6c16,0,26-17.3,18-31.2L268,80.6 C260,66.7,240,66.7,232,80.6z"></path> <path class="st2" d="M250,152.2c-21.2,0-38.4,19.6-38.4,43.8c0,73.8,17.2,133.6,38.4,133.6s38.4-59.8,38.4-133.6 C288.4,171.8,271.2,152.2,250,152.2z"></path> <circle class="st2" cx="250" cy="379.9" r="26.9"></circle> </g> </g> </g></svg>
                            #             </div>"""
                        add_marker = folium.Marker(
                                        location=(location['latitude'], location['longitude']),
                                        popup=popup,
                                        icon=div_icon
                                    )
                        marker_cluster_attention.add_child(add_marker)
                        # ).add_to(marker_cluster_attention)
                        # )
                    if price / build_up >= 700:
                        continue

                    if (price / build_up <= 300 and price <= 800000) or (i['tags'] == "lrd"):
                        div_icon = folium.features.CustomIcon(icon_0_2, icon_size=icon_size_s)
                        add_marker = folium.Marker(
                                location=(location['latitude'], location['longitude']),
                                popup=popup,
                                icon=div_icon
                            )
                        marker_cluster_lrd.add_child(add_marker)
                            # .add_to(marker_cluster_lrd)


                        # div_icon = f"""
                        #                 <div>
                        #                 <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M47.6 300.4L228.3 469.1c7.5 7 17.4 10.9 27.7 10.9s20.2-3.9 27.7-10.9L464.4 300.4c30.4-28.3 47.6-68 47.6-109.5v-5.8c0-69.9-50.5-129.5-119.4-141C347 36.5 300.6 51.4 268 84L256 96 244 84c-32.6-32.6-79-47.5-124.6-39.9C50.5 55.6 0 115.2 0 185.1v5.8c0 41.5 17.2 81.2 47.6 109.5z"/></svg>
                        #                 </div>"""
                    if i['prop_type'] and (
                            re.findall(".*(torey).*", i['prop_type']) or re.findall(".*(tory).*", i['prop_type'])):
                        div_icon = folium.features.CustomIcon(icon_0_3, icon_size=icon_size_s)

                        # div_icon = f"""
                        #             <div>
                        #             <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M543.8 287.6c17 0 32-14 32-32.1c1-9-3-17-11-24L512 185V64c0-17.7-14.3-32-32-32H448c-17.7 0-32 14.3-32 32v36.7L309.5 7c-6-5-14-7-21-7s-15 1-22 8L10 231.5c-7 7-10 15-10 24c0 18 14 32.1 32 32.1h32v69.7c-.1 .9-.1 1.8-.1 2.8V472c0 22.1 17.9 40 40 40h16c1.2 0 2.4-.1 3.6-.2c1.5 .1 3 .2 4.5 .2H160h24c22.1 0 40-17.9 40-40V448 384c0-17.7 14.3-32 32-32h64c17.7 0 32 14.3 32 32v64 24c0 22.1 17.9 40 40 40h24 32.5c1.4 0 2.8 0 4.2-.1c1.1 .1 2.2 .1 3.3 .1h16c22.1 0 40-17.9 40-40V455.8c.3-2.6 .5-5.3 .5-8.1l-.7-160.2h32z"/></svg>
                        #             </div>"""
                        # i['tags'] = "l"
                        add_marker = folium.Marker(
                                location=(location['latitude'], location['longitude']),
                                popup=popup,
                                icon=div_icon
                            )
                        marker_cluster_l.add_child(add_marker)
                            # .add_to(marker_cluster_l)



                # div_icon = folium.features.CustomIcon(icon_url_durian_runtuh_others, icon_size=icon_size)
                # add_marker = folium.Marker(
                #         location=(location['latitude'], location['longitude']),
                #         popup=popup,
                #         icon=div_icon
                #     )
                # marker_cluster_o.add_child(add_marker)
                        # .add_to(marker_cluster_o)


                        # div_icon = f"""
                        #                 <div>
                        #                 <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M215.7 499.2C267 435 384 279.4 384 192C384 86 298 0 192 0S0 86 0 192c0 87.4 117 243 168.3 307.2c12.3 15.3 35.1 15.3 47.4 0zM192 128a64 64 0 1 1 0 128 64 64 0 1 1 0-128z"/></svg>
                        #                 </div>"""

                # add_marker = None



                # popup = folium.Popup(iframe)
                # folium.Marker(
                #     location=(location['latitude'], location['longitude']),
                #     popup=popup,
                #     icon=div_icon
                #     # icon = folium.DivIcon(html=div_icon, icon_size=(20, 20))
                # ).add_to(add_marker)
                # folium.Marker(
                #     location=(location['latitude'], location['longitude']),
                #     popup=popup,
                #     icon=folium.DivIcon(html=div_icon)
                # ).add_to(sidebar)
        # print(str(marker_cluster_o.to_json()))
        # print(str(marker_cluster_lrd.to_json()))
        # print(str(marker_cluster_attention.to_json()))
        # print(str(marker_cluster_l.to_json()))
        # m.add_child(fg_att)
        # fg_att.add_child(marker_cluster_attention)

        # print("ultimate boss1 " + str(m.to_dict()))
        print("ultimate boss " + str(m.to_json()))
        # print("ultimate boss3 " + str(m.__dict__()))
        # print("ultimate boss4 " + str(m.__str__()))

        date_now = str(datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"))
        date_file = re.sub(r'[^\w]', '', date_now)
        # m.save(f"../../docs/index.html")
        # fig.save(f"../../docs/index.html")
        if testing:
            m.save(f"../../docs/testing.html")
        else:
            m.save(f"../../docs/index.html")
        # m.save(f"../../docs/LLT_" + date_file + ".html")

    def add_sidebar(self, m):
        # Create the sidebar HTML structure
        sidebar_html = '''
            <div id="sidebar" style="
                position: fixed;
                top: 50px;
                left: 10px;
                width: 200px;
                height: 100%;
                overflow: auto;
                z-index: 9999;
                background-color: white;
                opacity: 0.8;
                padding: 10px;
            "></div>
        '''

        # Create a custom tile layer
        tile_layer = folium.TileLayer('OpenStreetMap').add_to(m)

        # Add the sidebar to the map
        m.get_root().html.add_child(folium.Element(sidebar_html))

        # Set the CSS style for the sidebar
        style = '''
            <style>
                #sidebar::-webkit-scrollbar {
                    width: 5px;
                }

                #sidebar::-webkit-scrollbar-track {
                    background: #f1f1f1;
                }

                #sidebar::-webkit-scrollbar-thumb {
                    background: #888;
                }

                #sidebar::-webkit-scrollbar-thumb:hover {
                    background: #555;
                }
            </style>
        '''
        m.get_root().html.add_child(folium.Element(style))

        return m

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
            "content": "<h1>hihi</h1><p>" + str(
                draft_content) + "</p>\n \n \n <p>https://codepen.io/Meet-Ronny/pen/xxyWeNG</p>",
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

    def get_pages(self, page_no_upper, operating_url):
        # common = APIMethod.APIMethod()
        k = 0
        draft_content = []
        for i in range(1, int(page_no_upper) + 1):
            print("now i am at page " + str(i))
            response = requests.get(
                url=operating_url + str(i)
            )
            # response = common.trigger_api_request("GET", MAIN_URL + str(i), "")
            body_result = response.text
            content_list = self.get_contents(body_result)
            # print("size of content_list= " + str(len(content_list)))
            # print("size of draft_content= " + str(len(draft_content)))
            draft_content.append(content_list)
            sleep_time = secrets.choice(range(2, 5))
            # print("i've slept for seconds= " + str(k) +" "+ str(sleep_time))
            time.sleep(sleep_time)
            k = k + 1
            if k > 10 and testing:
                break
            #     raise Exception("Test end")
        # print(str(draft_content))
        return draft_content

    def get_contents_2(self, body_text):
        # print("\n***\n" + body_text)

        parsed_html = BeautifulSoup(body_text)
        content_list = []
        contents_raw = parsed_html.body.find_all('div', attrs={'class': 'col details-col flex-grow-1'})

        # border_info = parsed_html.find_all('div', attrs={'class': 'fs-5 mb-1 me-2 me-md-1 me-lg-2'})
        # print("iii= " + str(border_info))

        for i in contents_raw:
            print("xx= " + str(i))

            markup_i = BeautifulSoup(str(i), "xml")
            # parsed_border_info = BeautifulSoup(str(i))

            # border_info = markup_i.find_all('div', attrs={'class': 'd-flex flex-row pb-2'})
            for EachPart in markup_i.select('div[class*="fs-5 mb-1 me-2 me-md-1 me-lg-2"]'):
                print("mytype2= " + str(EachPart.get_text()))
                if EachPart.select('i[class*="fas fa-bed"]'):
                    print("this is bed== ")
                elif EachPart.select('i[class*="fas fa-fw fa-wifi"]'):
                    print("this is online bidding== ")
                elif EachPart.select('i[class*="fas fa-fw fa-neuter"]'):
                    print("this is offline bidding== ")

                elif not EachPart.get_text():
                    raise Exception("clean this mess")

            # for info in border_info:
            #     info_items = BeautifulSoup(str(info), "xml")

            # border_info = BeautifulSoup(str(border_info), "xml")
            # print("mytype= " + str(border_info))
            # for html in border_info:
            #     print("mytype2= " + str(html.span))

            # parsed_border_info = BeautifulSoup(str(border_info))
            # border_info_list = border_info.find_all('div')
            # print("iii= " + str(border_info_list))

            # print("iii= " + str(i))

            # border_info = i.find('div', attrs={'class': 'fs-5 mb-1 me-2 me-md-1 me-lg-2'})

            content_details = {}
            # content_details['auction_type'] = self.handle_value(i, 'h5', 'class', "fw-bold crop-text-3 mb-0")
            # content_details['nth_auction'] = self.handle_value(i, 'h5', 'class', "fw-bold crop-text-3 mb-0")
            # content_details['size'] = self.handle_value(i, 'h5', 'class', "fw-bold crop-text-3 mb-0")
            # content_details['tenure'] = self.handle_value(i, 'h5', 'class', "fw-bold crop-text-3 mb-0")
            # content_details['beds'] = self.handle_value(i, 'h5', 'class', "fw-bold crop-text-3 mb-0")
            # content_details['auction_mode'] = self.handle_value(i, 'h5', 'class', "fw-bold crop-text-3 mb-0")
            # content_details['restriction'] = self.handle_value(i, 'h5', 'class', "fw-bold crop-text-3 mb-0")

            # content_details['address'] = self.handle_value(i, 'h5', 'class', "fw-bold crop-text-3 mb-0")
            # content_details['prop_name'] = self.handle_value(i, 'p', 'class', "text-muted mb-0 text-truncate")
            # content_details['prop_type'] = self.handle_value(i, 'p', 'class', "text-info crop-text-2 list-none mb-2")
            # raw_str = re.findall("(\d+)", str(self.handle_value(i, 'div', 'class', "fs-5 mb-1 me-2 me-md-1 me-lg-2 list-none")))
            # if raw_str:
            #     build_up_raw = ''.join(raw_str)
            # else:
            #     build_up_raw = None
            # # print("builup raw= " + build_up_raw)
            # content_details['build_up'] = build_up_raw
            # content_details['date'] = self.handle_value(i, 'div', 'class', "fs-6 d-block fw-bold")
            # content_details['price'] = ''.join(re.findall("\d+", self.handle_value(i, 'h4', 'class', "fw-bold text-nowrap d-flex flex-row flex-sm-column position-relative")))
            # psf_raw = self.handle_value(i, 'div', 'class', 'fs-5 mb-1 me-2 me-md-1 me-lg-2 grid-none')
            # psf = re.findall("\d+", psf_raw[0] if psf_raw else "0")
            # content_details['psf'] = ''.join(psf)
            # content_details['others'] = self.handle_value(i, 'td', 'class', "position-relative")
            # content_details['h_ref'] = re.findall(".*<a class=\"stretched-link\" href=\"(.*)\" title=.*", str(i))[0]
            # content_details['restriction'] = self.handle_value(i, 'div', 'class', 'fs-5 mb-1 me-2 me-md-1 me-lg-2 grid-none list-none')
            # tag = None
            #
            # content_details['tags'] = tag
            content_list.append(content_details)
            # print("content_details= " + str(content_details))
            counter = 0
            # for i in content_details

            # print("testitem " + str(content_list))
        return content_list

    def get_contents(self, body_text):
        # print("\n***\n" + body_text)

        parsed_html = BeautifulSoup(body_text)
        content_list = []
        contents_raw = parsed_html.body.find_all('div', attrs={'class': 'col details-col flex-grow-1'})
        for i in contents_raw:
            markup_i = BeautifulSoup(str(i), "xml")
            misc = ''
            tag = ''
            nth = ''
            listing_status = None
            for EachPart in markup_i.select('div[class*="fs-5 mb-1 me-2 me-md-1 me-lg-2"]'):
                info = str(EachPart.get_text())
                if EachPart.select('sup'):
                    if int(re.findall("(\d+)", info)[0]) > 2:
                        tag = 'attention'
                if EachPart.select('i[class*="fas fa-bed"]'):
                    misc = self.add_string(misc, info + ' bedroom')
                    # print("this is bed== ")
                elif EachPart.select('i[class*="fas fa-fw fa-wifi"]'):
                    misc = self.add_string(misc, info + ' online bidding')
                    # print("this is online bidding== ")
                elif EachPart.select('i[class*="fas fa-fw fa-neuter"]'):
                    misc = self.add_string(misc, info + ' offline bidding')
                    # print("this is offline bidding== ")
                elif not EachPart.get_text():
                    raise Exception("clean this mess")
                else:
                    misc = self.add_string(misc, info)
                    # misc = misc + ' ' + str(EachPart.get_text())

            content_details = {}
            content_details['address'] = self.handle_value(i, 'h5', 'class', "mb-0")
            content_details['prop_name'] = self.handle_value(i, 'p', 'class', "mb-0")
            content_details['prop_type'] = self.handle_value(i, 'p', 'class', "mb-2")
            raw_str = re.findall("(\d+)",
                                 str(self.handle_value(i, 'div', 'class', "fs-5 mb-1 me-2 me-md-1 me-lg-2 list-none")))
            if raw_str:
                build_up_raw = ''.join(raw_str)
            else:
                build_up_raw = None
            # print("builup raw= " + build_up_raw)
            content_details['build_up'] = build_up_raw
            if markup_i.select('div[class*="list-none status-label bg-cyan"]'):
                listing_status = "No Bidder"
            elif markup_i.select('div[class*="list-none status-label bg-purple"]'):
                listing_status = "Expired"
            content_details['date'] = self.handle_value(i, 'div', 'class', "fs-6 d-block fw-bold")
            try:
                auction_date = datetime.strptime(content_details['date'], '%d %b %Y (%a)').date()
                if auction_date < today_date:
                    continue
            except:
                listing_status = "No Bidder"
            content_details['listing_status'] = listing_status
            content_details['price'] = ''.join(re.findall("\d+", self.handle_value(i, 'h4', 'class',
                                                                                   "text-nowrap d-flex flex-row flex-sm-column position-relative")))
            # psf_raw = self.handle_value(i, 'div', 'class', 'fs-5 mb-1 me-2 me-md-1 me-lg-2 grid-none')
            # psf = re.findall("\d+", psf_raw[0] if psf_raw else "0")
            # content_details['psf'] = ''.join(psf)
            content_details['others'] = misc
            content_details['nth'] = nth
            content_details['h_ref'] = re.findall(".*<a class=\"stretched-link\" href=\"(.*)\" title=.*", str(i))[0]
            content_details['restriction'] = self.handle_value(i, 'div', 'class',
                                                               'fs-5 mb-1 me-2 me-md-1 me-lg-2 grid-none list-none')
            content_details['tags'] = tag
            content_list.append(content_details)
            # print("content_details= " + str(content_details))
            counter = 0
            # for i in content_details

            # print("testitem " + str(content_list))
        return content_list
        # print(parsed_html.body.find('div', attrs={'class': 'col details-col flex-grow-1'}).text)

    def add_string(self, misc, info):

        if not misc:
            return info
        misc = misc + ', ' + info
        return misc

    def handle_value(self, i, name_div, name_class, name_subclass):
        value = None
        # print("me again " + str(i.find(name_div, attrs={name_class: re.compile(name_subclass)})))
        if i.find(name_div, attrs={name_class: re.compile(name_subclass)}):
            value = i.find(name_div, attrs={name_class: re.compile(name_subclass)}).text.strip()
        # print("me again after " + value)
        return value

    def set_pages(self, body_text):
        page_no_raw = re.findall(r"Result\(s\): (.*)</p>", body_text)[0]
        page_no_refined = re.findall("(\d)", page_no_raw)
        page_no = ''.join(i for i in page_no_refined)
        page_no_upper = math.ceil(int(page_no) / 12)
        # print("hi " + str(page_no_upper))
        return page_no_upper

        #     if len(body_result) > 1:
        #         rand_claims = secrets.choice(range(0, len(body_result)))
        #     else:
        #         rand_claims = 0
        #     BuiltIn().set_test_variable("${rand_claims_selection}", body_result[rand_claims]["ID"])
        # BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def iprop_scrape(self):
        response = requests.get(
            # url=MAIN_URL_IP + str(1)

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
