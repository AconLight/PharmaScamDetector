from src.webscrapers.utils.html_scraper import html_scrap
from src.webscrapers.utils.selector_scraper import selector_scrap


def pharma_company_list_scrap():
    pharma_companies = selector_scrap(
        html_scrap("https://www.drugs.com/pharmaceutical-companies.html"),
        "div.ddc-grid-col-6 ul li a",
    )
    results = []
    for pharma_company in pharma_companies:
        next_link = "https://www.drugs.com" + pharma_company.attributes['href']
        company_name = pharma_company.text().lower()
        company_page_html = html_scrap(next_link)
        website = selector_scrap(
            company_page_html,
            "div.ddc-manufacturer-details p span a",
        )
        website = website[0].attributes['href'] if len(website) > 0 and 'href' in website[0].attributes.keys() else ""
        drugs = list(map(lambda x: x.text(), selector_scrap(
            company_page_html,
            "table.data-list tbody tr td:first-of-type a:first-of-type",
        )))

        results.append({
            "company_name": company_name,
            "website": website,
            "drugs": drugs,
        })
    return results
