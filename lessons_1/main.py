import requests


HOST = 'http://wttr.in'

def main():
    cities = [
        'London',
        'Sheremetyevo',
        'Cherepovets',
    ]

    headers = {
        'User-Agent': 'curl',
        'Accept': '*/*',
        'Accept-Language': 'ru-RU'
    }

    params = {
        'nMmuTqu': '',
        'lang': 'ru'
    }

    for city in cities:
        url = f'{HOST}/{city}'
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        print(response.text)

if __name__ == "__main__":
    main()