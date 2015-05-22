import requests
from bs4 import BeautifulSoup


_start_url = 'http://www.letsrun.com/forum'
_form_domain_test = 'letsrun.com/forum'


def get_soup(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        return BeautifulSoup(r.text)


def get_all_links(soup):
    links = soup.findAll('a')
    return [l['href'] for l in links]


def filter_links(links, match=_form_domain_test):
    return list(set([l for l in links if match in l]))

