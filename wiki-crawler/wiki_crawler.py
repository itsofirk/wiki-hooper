from bs4 import BeautifulSoup

from core import Crawler, LinkFilter, CommonFilters

ignore_classes = {'image', 'mw-logo'}

_filters = [
    CommonFilters.in_page_jump,
    (lambda x: len(set(x.get('class', {})).intersection(ignore_classes)) == 0),  # filter classes
    (lambda x: 'action=edit' not in x.get('href', ''))  # filter edit pages
]


class WikiCrawler(Crawler):
    def __init__(self, urls):
        super().__init__(urls, LinkFilter(_filters))

    def _get_soup(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup.find(id='bodyContent')
