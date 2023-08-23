from src.nlp.utils.pharma_company_name_phrase import parse_names_to_phrases
from src.readers.davis_paper_reader import davis_paper_read
from src.webscrapers.pharma_company_list_scrap import pharma_company_list_scrap

if __name__ == '__main__':
    # df = davis_paper_read()
    # print(df)

    pharma_list = pharma_company_list_scrap()
    for res in pharma_list:
        print(parse_names_to_phrases([res.attributes['title'], res.text()]))
        #print(f"{res.attributes['title']}, {res.text()}, https://en.wikipedia.org{res.attributes['href']}")

    print(f"number of companies: {len(pharma_list)}")
