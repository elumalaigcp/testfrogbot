from bs4 import BeautifulSoup
import json
import requests
import urllib3


def main():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    url = "https://google.com"
    r = requests.get(url, verify=False)

    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.find('title')

    _dict = {
        "URL": r.url,
        "Title": title.string,
        "Status": r.ok,
        "Code": r.status_code
    }

    print(json.dumps(_dict, indent=4))


if __name__ == '__main__':
    main()
