import requests
import cfscrape
import json

def download_json(url: str) -> dict:
    if not isinstance(url, str):
        raise TypeError('7pupu')

    scraper = cfscrape.create_scraper()
    result = scraper.get(url)
    return json.loads(result.text)


def download_img(url: str, path: str) -> None:
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)


