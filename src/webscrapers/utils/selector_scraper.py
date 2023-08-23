import httpx
from selectolax.parser import HTMLParser


def selector_scrap(url, selector):
    resp = httpx.get(
        url,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
        },
    )
    html = HTMLParser(resp.text)
    data = html.css(selector)
    return data
