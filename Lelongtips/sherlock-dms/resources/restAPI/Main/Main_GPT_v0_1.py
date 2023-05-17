import math
import os
import re
from datetime import datetime

import googlemaps
from geopy.geocoders import Nominatim
import git
import folium
import requests
from bs4 import BeautifulSoup
from robot.api.deco import keyword

from resources.restAPI import LLT_URL, PROTOCOL, GMAPS_TOKEN


MAIN_URL = PROTOCOL + LLT_URL
GMAPS_TOKEN = GMAPS_TOKEN

gmaps = googlemaps.Client(key=GMAPS_TOKEN)


class Main_GPT_v0_1(object):
    @keyword("user runs main gpt flow")
    def user_runs_main_flow(self):
        response = requests.get(url=MAIN_URL + str(1))
        draft_content = []
        if response.status_code == 200:
            body_result = response.text
            page_no_upper = self.set_pages(body_result)
            draft_content = self.get_pages(page_no_upper)
            self.map_gen(draft_content)
            self.git_controls()
        else:
            raise Exception("Initial load failed")
        if draft_content:
            self.save_draft(draft_content)

    def map_gen(self, draft_content):
        m = folium.Map(location=(3.064119, 101.669488), tiles="OpenStreetMap", zoom_start=10)
        for i in draft_content[0]:
            location = {}
            loc = i["address"]
            geocode_result = gmaps.geocode(loc)
            location_raw = geocode_result[0]["geometry"]["location"]
            formatted_address_name = geocode_result[0]["formatted_address"]
            location.update({"latitude": location_raw["lat"]})
            location.update({"longitude": location_raw["lng"]})
            div_icon = self.get_div_icon(i)
            if not location:
                continue
            html = self.generate_html(i, formatted_address_name)
            iframe = folium.IFrame(html=html, width=300, height=200)
            popup = folium.Popup(iframe, max_width=2650)
            folium.Marker(
                location=(location["latitude"], location["longitude"]),
                popup=popup,
                icon=folium.DivIcon(html=div_icon),
            ).add_to(m)
        self.save_map_html(m)

    def get_div_icon(self, i):
        div_icon = None
        price = i["price"]
        build_up = i["build_up"]
        if not price or not build_up:
            div_icon = """
                <div>
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512">
                <path d="M215.7 499.2C267 435 384 279.4 384 192C384 86 298 0 192 0S0 86 0 192c0 87.4 117 243 168.3 307.2c12.3 15.3 35.1 15.3 47.4 0zM192 128a64 64 0 1 1 0 128 64 64 0 1 1 0-128z"/>
                </svg>
                </div>"""
        else:
            price = float(price)
            build_up = float(build_up)
            if price / build_up >= 700:
                return None
            elif price / build_up <= 300 and price <= 800000:
                div_icon = """
                        <div>
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                        <path d="M47.6 300.4L228.3 469.1c7.5 7 17.4 10.9 27.7 10.9s20.2-3.9 27.7-10.9l180.7-168.7c7.6-7.1 12.3-17.3 12.3-28.4V192c0-35.3-28.7-64-64-64H64C28.7 128 0 156.7 0 192v79.9c0 11.1 4.7 21.3 12.3 28.4zm168.4-72.4c-15.9 0-28.9-13-28.9-28.9 0-15.9 13-28.9 28.9-28.9s28.9 13 28.9 28.9c0 15.9-13 28.9-28.9 28.9zm152.2 0c-15.9 0-28.9-13-28.9-28.9 0-15.9 13-28.9 28.9-28.9s28.9 13 28.9 28.9c0 15.9-13 28.9-28.9 28.9zm-176.5 0c-15.9 0-28.9-13-28.9-28.9 0-15.9 13-28.9 28.9-28.9s28.9 13 28.9 28.9c0 15.9-13 28.9-28.9 28.9zm0-56.7c-6.9 0-12.5 5.6-12.5 12.5s5.6 12.5 12.5 12.5s12.5-5.6 12.5-12.5s-5.6-12.5-12.5-12.5zm152.2 0c-6.9 0-12.5 5.6-12.5 12.5s5.6 12.5 12.5 12.5s12.5-5.6 12.5-12.5s-5.6-12.5-12.5-12.5zm-176.5 0c-6.9 0-12.5 5.6-12.5 12.5s5.6 12.5 12.5 12.5s12.5-5.6 12.5-12.5s-5.6-12.5-12.5-12.5z"/>
                        </svg>
                        </div>"""
            elif price / build_up > 300 and price <= 1500000:
                div_icon = """
                        <div>
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
                        <path d="M352 320h48v128H48V320h48V176c0-17.67 14.33-32 32-32h96V48c0-26.51 21.49-48 48-48h32c26.51 0 48 21.49 48 48v96h96c17.67 0 32 14.33 32 32zm32-224h-32V48h32v48zm-96 0h-32V48h32v48zM144 384H64v96h80v-96zm256 96v-96h80v96h-80zm32-128h-32V224h32v128z"/>
                        </svg>
                        </div>"""
        return div_icon

    def generate_html(self, i, formatted_address_name):
        html = f"""
            <h4>{i["name"]}</h4>
            <p><b>Address:</b> {formatted_address_name}</p>
            <p><b>Price:</b> {i["price"]} RM</p>
            <p><b>Build Up:</b> {i["build_up"]} sqft</p>
            <p><b>Bedrooms:</b> {i["bedroom"]}</p>
            <p><b>Bathrooms:</b> {i["bathroom"]}</p>
            """
        return html

    def save_map_html(self, m):
        map_path = os.path.join(os.getcwd(), "map.html")
        m.save(map_path)
        m.save(f"../../docs/index.html")

        print(f"Map saved at {map_path}")

    def save_draft(self, draft_content):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_path = os.path.join(os.getcwd(), f"draft_{timestamp}.txt")
        with open(file_path, "w") as f:
            for item in draft_content:
                f.write(f"{item}\n")
        print(f"Draft saved at {file_path}")

    def set_pages(self, body_result):
        soup = BeautifulSoup(body_result, "html.parser")
        page_no = soup.find_all("a", class_="page-link")
        page_no_upper = page_no[0].get("href").split("/")[0]
        return page_no_upper

    def get_pages(self, page_no_upper):
        draft_content = []
        for i in range(1, int(page_no_upper) + 1):
            url = MAIN_URL + str(i)
            print(f"Crawling {url}")
            response = requests.get(url)
            if response.status_code == 200:
                body_result = response.text
                draft_content.append(self.process_content(body_result))
            else:
                print(f"Failed to crawl {url}")
        return draft_content

    def process_content(self, body_result):
        soup = BeautifulSoup(body_result, "html.parser")
        data = soup.find_all("div", class_="col-lg-9 mb-30")
        draft_data = []
        for i in data:
            try:
                name = i.find("a", class_="fw-medium text-grey mb-4 d-inline-block").text.strip()
                price = i.find("span", class_="text-primary d-block fs-16").text.strip()
                details = i.find_all("span", class_="text-dark")
                bedroom = details[0].text.strip()
                bathroom = details[1].text.strip()
                build_up = details[2].text.strip()
                address = i.find("address", class_="mb-2").text.strip()
                draft_data.append(
                    {
                        "name": name,
                        "price": price,
                        "bedroom":bedroom,
                        "bathroom": bathroom,
                        "build_up": build_up,
                        "address": address,
                    }
                )
            except Exception as e:
                print(f"Failed to process data: {e}")
            return draft_data

    def git_controls(self):
        repo = git.Repo(os.getcwd())
        if repo.is_dirty():
            repo.git.add(update=True)
            repo.git.commit("-m", "Updated draft content and map")
            repo.remotes.origin.pull()
            repo.remotes.origin.push()
        else:
            print("No changes to commit")

    def run(self):
        self.user_runs_main_flow()
