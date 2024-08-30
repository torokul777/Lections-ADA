import requests
from bs4 import BeautifulSoup as BS
import csv


def get_html(url):
    response = requests.get(url)
    return response.text


def get_data(html):
    soup = BS(html, 'lxml')
    catalog = soup.find('div', class_='browse-view')
    laptops = catalog.find_all('div', class_='row')
    for laptop in laptops:
        try:
            title = laptop.find('a', class_='product-image-link').get('title')
        except:
            title = ''
        try:
            image = laptop.find('img').get('src')
            image = f'https://enter.kg{image}'
        except:
            image = ''
        try:
            price = laptop.find('span', class_='price').text
        except:
            price = ''

        data = {
            'title': title,
            'image': image,
            'price': price,
        }

        write_csv(data)


def write_csv(data):
    with open('enter_kg_laptops.csv', 'a') as csv_file:
        name = ['title', 'price', 'image']
        writer = csv.DictWriter(csv_file, delimiter='|', fieldnames=name)
        writer.writerow(data)


def get_last_page(html):
    """
    Эта функция находит ссылку на последнюю страницу
    """
    soup = BS(html, 'lxml')
    url_last_page = soup.find('li', class_='pagination-end').find('a').get('href')
    # print(url_last_page, '1111111111111111111111111')
    last_page = '' # 3901-3900
    for digit in url_last_page:
        if digit.isdigit() or digit=='-':
            last_page += digit
    last_page = last_page.split('-')
    return int(last_page[0])


def main():
    url = 'https://enter.kg/computers/noutbuki_bishkek'
    html = get_html(url)
    last_page = get_last_page(html)
    for page in range(1, last_page+1):
        url = f'https://enter.kg/computers/noutbuki_bishkek/results,{page}-{page-1}'
        html = get_html(url)
        data = get_data(html)

main()