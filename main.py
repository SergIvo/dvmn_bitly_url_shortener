import requests
import os
from urllib.parse import urlparse
from argparse import ArgumentParser
from dotenv import load_dotenv


def shorten_link(token, url):
    api_url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(
        api_url,
        headers=headers,
        json={'long_url': url},
    )
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, link):
    url_parts = urlparse(link)
    base_api_url = 'https://api-ssl.bitly.com'
    api_url = f'{base_api_url}/v4/bitlinks/{url_parts.netloc}{url_parts.path}/clicks/summary'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, link):
    url_parts = urlparse(link)
    api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{url_parts.netloc}{url_parts.path}'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(api_url, headers=headers)
    return response.ok


if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ['BITLY_API_KEY']
    
    arg_parser = ArgumentParser()
    arg_parser.add_argument('url', help='Длинная ссылка для укорачивания либо ссылка bit.ly')
    args = arg_parser.parse_args()

    try:
        if not is_bitlink(api_key, args.url):
            print(f'Битлинк: {shorten_link(api_key, args.url)}')
        else:
            print(f'Переходов по ссылке: {count_clicks(api_key, args.url)}')
    except requests.exceptions.HTTPError as error:
            print('Произошла ошибка. Проверьте правильность ввода ссылки.',
                  'Ответ от сервера: ', error)

