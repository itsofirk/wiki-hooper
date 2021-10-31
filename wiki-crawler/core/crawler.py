import logging
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from core.link_filter import LinkFilter


class Crawler:
    def __init__(self, urls=None, link_filter: LinkFilter = None):
        if urls is None:
            urls = []
        if link_filter is None:
            link_filter = LinkFilter()
        self.visited_urls = []
        self.urls_to_visit = urls
        self.link_filter = link_filter

    def download_url(self, url):
        return requests.get(url).text

    def get_linked_urls(self, url, html):
        soup = self._get_soup(html)
        for link in self.link_filter(soup.find_all('a')):
            path = link.get('href')
            if path:
                if path.startswith('/'):  # fixes reference links
                    path = urljoin(url, path)
                yield path

    def _get_soup(self, html):
        return BeautifulSoup(html, 'html.parser')

    def add_url_to_visit(self, url):
        if self._is_new_link(url):
            self.urls_to_visit.append(url)

    def _is_new_link(self, url):
        return url not in self.visited_urls and \
               url not in self.urls_to_visit

    def crawl(self, url):
        html = self.download_url(url)
        for url in self.get_linked_urls(url, html):
            self.add_url_to_visit(url)

    def run(self):
        while self.urls_to_visit:
            url = self.urls_to_visit.pop(0)
            logging.info(f'Crawling: {url}')
            try:
                self.crawl(url)
            except Exception:
                logging.exception(f'Failed to crawl: {url}')
            finally:
                self.visited_urls.append(url)
