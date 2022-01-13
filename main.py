# from fake_useragent import UserAgent
import requests
import json
from bs4 import BeautifulSoup
import os
import lxml
import re
import time
import random
import csv
from geopy.geocoders import Nominatim
import googlemaps

import drawOnMap

# from config import api_key

# map_client = googlemaps.Client(api_key) # key in riga ...

geolocator = Nominatim(user_agent="sample app")

# ua = UserAgent()
# region_of_interest = ["aizkraukle", "aluksne", "balvi", "bauska", "cesis", "daugavpils", "dobele", "gulbene", "jelgava",
#     "kraslava", "kuldiga", "jekabpils", "liepaja", "limbazi", "ludza", "madona", "ogre", "preili",
#     "rezekne", "saldus", "talsi", "tukums", "valka", "valmiera", "ventspils"]

region_of_interest = "ludza"  # test range


def parse_all():
    for i in range(len(region_of_interest)):
        collect_data(region_of_interest[i])


# save raw html data for the region
def get_all_html(region):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }
    r = requests.get(url="https://www.ss.lv/lv/real-estate/plots-and-lands/" + region + "-and-reg/sell/page1.html",
                     headers=headers)

    if not os.path.exists("data"):
        os.mkdir("data")

    with open("data/page_1.html", "w", encoding="utf-8") as file:
        file.write(r.text)


# extract useful data from saved html and save in json file
def collect_data(region):
    get_all_html(region)

    with open(f"data/page_1.html", encoding="utf-8") as file:
        data = []
        src = file.read()

        soup = BeautifulSoup(src, "lxml")
        table_rows = soup.find_all("tr", id=re.compile("^tr_"))  # "tr_"

        print("Processing: ", region, " Number of rows find: ", len(table_rows))
        time.sleep(4 + random.randint(0, 4))

    for item in table_rows:
        td_tags = item.find_all("td")

        n = 0

        if len(td_tags) > 4:
            if not check_if_ad_exists(td_tags[2].text, td_tags[4].text, td_tags[5].text, td_tags[6].text):
                n = +1
                data.append(
                    {
                        "regio": region,
                        "descr": td_tags[2].text,
                        "address": td_tags[3].text,
                        "area": td_tags[4].text,
                        "price1m2": td_tags[5].text,
                        "totalPrice": td_tags[6].text
                    }
                )

    with open("data3.json", "a", encoding='utf8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(n, "new ads found in ", region)


# function to find new advertisements on the website
def check_if_ad_exists(descr, area, price1m2, totalPrice):
    dati = []
    with open('data2.json', encoding='utf8') as json_file:
        dati = json.loads(json_file.read())

    new_data_point = [descr, area, price1m2, totalPrice]
    outp = False

    for i in range(len(dati)):
        existing_data_point = [dati[i]["descr"], dati[i]["area"], dati[i]["price1m2"], dati[i]["totalPrice"]]
        if new_data_point == existing_data_point:
            outp = True

    return outp


# maximal number of pages per region - currently not in use
def findPageNum():
    with open(f"data/page_1.html", encoding="utf-8") as file:
        page_nums = []
        src = file.read()
        soup = BeautifulSoup(src, "lxml")

        page_nums = soup.find_all(attrs={'class': ['navi', 'navia']})
        print("Outp", len(page_nums), page_nums[-2].text)


def process_json():
    with open('data2.json', encoding='utf8') as json_file:
        dati = json.loads(json_file.read())

    n = 0

    for i in range(len(dati)):
        adrese = dati[i]["address"].replace("pag.", "pagasts, ")
        dati[i]['address'] = adrese
        # dati[i]['coord'] = geocoder_test(adrese)

        if dati[i]['coord'][0] == 0:
            dati[i]['coord'] = geocoder_test(adrese)

        print(i, adrese, dati[i]["totalPrice"], dati[i]['coord'])

    with open("data2.json", "w", encoding='utf8') as file:
        json.dump(dati, file, indent=4, ensure_ascii=False)

    # print("Total processed: ", len(dati), "coordinate not found: ", n)


def geocoder_test(adr):
    # location = geolocator.geocode("Rīga, Latvija")
    location = geolocator.geocode(adr)

    if location is not None:
        coord = location.latitude, location.longitude
        time.sleep(0.2)
    else:  # google maps api if local is not enoght
        try:
            pass
            # geocode_rez = map_client.geocode(adr)
            # coord = geocode_rez[0]["geometry"]["location"]["lat"], geocode_rez[0]["geometry"]["location"]["lng"]
        except:
            coord = 0, 0

    return coord


def main():
    # parse_all()
    # process_json()
    # print (geocoder_test("Mazzalves pagasts, Lielmēmele"))
    # drawOnMap.test_draw()

    collect_data(region_of_interest)


if __name__ == '__main__':
    main()
