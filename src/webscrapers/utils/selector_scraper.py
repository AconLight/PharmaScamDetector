import httpx
from selectolax.parser import HTMLParser

from src.webscrapers.utils.html_scraper import html_scrap


def selector_scrap(html, selector):
    data = html.css(selector)
    return data
