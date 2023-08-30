import httpx
from selectolax.parser import HTMLParser


def website_link_tree_scraper(root_link, page_link):
    website_contents = []
    next_page_links = []
    try:
        resp = httpx.get(
            page_link,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
            },
        )
        html = HTMLParser(resp.text)
        website_contents += [html.text()]
        links = html.css('a')
        for link in links:
            if 'href' not in link.attributes.keys():
                continue
            new_link = link.attributes['href']
            if new_link is not None and root_link in new_link:
                next_page_links += [new_link]
        return website_contents, list(dict.fromkeys(next_page_links))
    except:
        return [], []
