from src.webscrapers.utils.selector_scraper import selector_scrap


def pharma_company_list_scrap():
    result = selector_scrap(
        {},
        "https://en.wikipedia.org/wiki/List_of_pharmaceutical_companies",
        "div.mw-parser-output div.div-col ul li a"
    )
    return result["data"]
