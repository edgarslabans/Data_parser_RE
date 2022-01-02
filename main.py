# from fake_useragent import UserAgent
import requests
import json
from bs4 import BeautifulSoup
import os
import lxml
import re


# ua = UserAgent()


def get_all_pages():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }

    r = requests.get(url="https://www.ss.lv/lv/real-estate/flats/riga/imanta/sell/page3.html", headers=headers)

    if not os.path.exists("data"):
        os.mkdir("data")

    with open("data/page_1.html", "w", encoding="utf-8") as file:
        file.write(r.text)
    print("Html data saved")


def collect_data():
    with open(f"data/page_1.html", encoding="utf-8") as file:
        data = []
        src = file.read()

        soup = BeautifulSoup(src, "lxml")
        table_rows = soup.find_all("tr", id=re.compile("^tr_"))  # "tr_"

        print("Ņumber or rows", len((table_rows)))

    for item in table_rows:
        td_tags = item.find_all("td")

        # print("Item:",item)

        if len(td_tags) > 4:
            data.append(
                {
                    "address": td_tags[3].text,
                    "area": td_tags[4].text,
                    "price1m2": td_tags[5].text,
                    "totalPrice": td_tags[6].text
                }
            )
            address = td_tags[3].text
            area = td_tags[4].text
            price1m2 = td_tags[5].text
            totalPrice = td_tags[6].text
            # print(address, area, price1m2, totalPrice)

            with open("data.json", "a", encoding='utf8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)


def findPageNum():

    with open(f"data/page_1.html", encoding="utf-8") as file:
        page_nums = []
        src = file.read()
        soup = BeautifulSoup(src, "lxml")

        page_nums = soup.find_all("a",  attrs={'name':'nav_id'})

        print("Outp" ,len(page_nums), page_nums[0].text)


def main():
    #get_all_pages()
    #collect_data()
    findPageNum()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
