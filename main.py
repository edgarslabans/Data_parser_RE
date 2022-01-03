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
geolocator = Nominatim(user_agent="sample app")

# ua = UserAgent()
region_of_interest = ["aizkraukle", "aluksne", "balvi", "bauska", "cesis", "daugavpils", "dobele", "gulbene", "jelgava",
                      "kraslava", "kuldiga", "jekabpils", "liepaja", "limbazi", "ludza", "madona", "ogre", "preili",
                      "rezekne", "saldus", "talsi", "tukums", "valka", "valmiera", "ventspils"]


# region_of_interest = ["aluksne"]


def parse_all():
    for i in range(len(region_of_interest)):
        get_all_pages(region_of_interest[i])
        collect_data(region_of_interest[i])


# save raw html data for the region
def get_all_pages(region):
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
    with open(f"data/page_1.html", encoding="utf-8") as file:
        data = []
        src = file.read()

        soup = BeautifulSoup(src, "lxml")
        table_rows = soup.find_all("tr", id=re.compile("^tr_"))  # "tr_"

        print("Processing: ", region, " Number of rows find: ", len(table_rows))
        time.sleep(4 + random.randint(0, 4))

    for item in table_rows:
        td_tags = item.find_all("td")

        # print("Item:",item)

        if len(td_tags) > 4:
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

    with open("data.json", "a", encoding='utf8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# maximal number of pages per region - currently not in use
def findPageNum():
    with open(f"data/page_1.html", encoding="utf-8") as file:
        page_nums = []
        src = file.read()
        soup = BeautifulSoup(src, "lxml")

        page_nums = soup.find_all(attrs={'class': ['navi', 'navia']})
        print("Outp", len(page_nums), page_nums[-2].text)


def process_json():
    with open('data.json', encoding='utf8') as a:
        dict1 = json.load(a)

        for key in dict1:
            print(key, ":", dict1[key])



def geocoder_test():
    #location = geolocator.geocode("Rīga, Latvija")
    location = geolocator.geocode("Riga, Latvia")

    print((location.latitude, location.longitude))


def main():
    # parse_all()

    process_json()
    # geocoder_test()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
