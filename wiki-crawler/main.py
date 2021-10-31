import logging
from wiki_crawler import WikiCrawler

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)

if __name__ == '__main__':
    seed_urls = ['https://he.wikipedia.org/wiki/%D7%A6%D7%95%D7%A7%D7%99_%D7%93%D7%99%D7%A0%D7%92%D7%9C%D7%99']
    WikiCrawler(urls=seed_urls).run()
