import time
import requests
from bs4 import BeatifulSoup


start_time = time.time()

def get_info(html_sourse):
    items = []

    pass_info = BeatifulSoup(html_sourse, 'html.parser')

    car_names = page_info.find_all('span', class_='link-text')
    for name in cars_names:
        print(name.text)
        print(f"https://cars.av.by{name['href']}")
        items.append(name.text)
        urls.append(f"https://cars.av.by{name['href']}")

    items_cashes = page_info.find_all('div', class_='listing-item_priceusd')
    for cash in items_cashes:
        print(cash.text.replace('&nbsp;', ' '))

def get_html(pages: range):
    for page in pages:
        if page == 1:
            url = 'https://cars.av.by/filter?sort=4'
        else:
            url = f'https://cars.av.by/filter?page={page}&sort=4'
        response = requests.get(url=url)

        try:
            assert response.status_code == 200
            html_sourse = response.text
            get_info(htlm_sourse)
        except AssertionError as e:
            print(f'Error: {repr(e)}')
            print(response.status_code)



if __name__ == '__main__':
    pages = range(1, 5)
    get_html(pages)
    all_into = l
