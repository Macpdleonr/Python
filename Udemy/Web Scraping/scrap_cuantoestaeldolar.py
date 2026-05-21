import pdb
import datetime, requests, time, os, json

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

def scrap_web(url):

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(5000)
        html = page.content()
        browser.close()

        return html
    
def parse_rates(html):

    soup = BeautifulSoup(html, 'html.parser')
    houses = soup.find_all(
        'div',
        class_='ExchangeHouseItem_item_col__gudqq'
    )

    results = []

    for house in houses:
        try:

            img = house.find('img')
            name = img.get('alt').strip()
            link = house.find('a', href=True)
            website = link['href'].strip()

            buy_div = house.find(
                'div',
                class_='ValueCurrency_content_buy__Z9pSf'
            )

            buy_value = buy_div.find(
                'p',
                class_='ValueCurrency_item_cost__Eb_37'
            ).text.strip()

            sell_div = house.find(
                'div',
                class_='ValueCurrency_content_sale__fdX_P'
            )

            sell_value = sell_div.find(
                'p',
                class_='ValueCurrency_item_cost__Eb_37'
            ).text.strip()

            item = {
                "name": name,
                "website": website,
                "buy": float(buy_value),
                "sell": float(sell_value)
            }

            results.append(item)

        except Exception as e:
            print(f'Error procesando item: {e}')
    return results

def main():
    data = []
    while data == []:
        print(f'[{datetime.datetime.now()}] Ejecutando scraping...')
        html = scrap_web('https://cuantoestaeldolar.pe')
        data = parse_rates(html)
        print(json.dumps(data, indent=4, ensure_ascii=False))

    url = 'https://.....'
    headers = {
        'Authorization': 'token'
    }
    response = requests.post(
        url,
        json=data,
        headers=headers
    )

    print("STATUS:", response.status_code)
    print("RESPONSE JSON:", response.json())
    print(f'[{datetime.datetime.now()}] Finalizado')

while True:
    try:
        main()
    except Exception as e:
        print(f'ERROR GENERAL: {e}')

    print('Esperando 10 minutos...\n')
    time.sleep(600)