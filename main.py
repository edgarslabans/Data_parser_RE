# from fake_useragent import UserAgent
import requests
import json
from bs4 import BeautifulSoup
import os
import lxml


# ua = UserAgent()


def get_all_pages():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }

    r = requests.get(url="https://www.ss.lv/lv/real-estate/plots-and-lands/riga/centre/sell/", headers=headers)

    if not os.path.exists("data"):
        os.mkdir("data")

    with open("data/page_1.html", "w", encoding="utf-8") as file:
        file.write(r.text)


def collect_data():
    with open(f"data/page_1.html", encoding="utf-8") as file:
        src = file.read()

        soup = BeautifulSoup(src, "lxml")
        items_cards = soup.find_all("tr",id="tr_50831706")

    for item in items_cards:
        #price = item.find("a", class_="amopt").text
        print(item)


def main():
    # get_all_pages()
    collect_data()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
