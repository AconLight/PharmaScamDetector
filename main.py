from src.data.datamodel.PPP_data_object import PPPDataObject
from src.data.datamodel.pharma_company_data_object import PharmaCompanyDataObject
from src.nlp.utils.pharma_company_name_phrase import parse_names_to_phrases
from src.readers.davis_paper_reader import davis_paper_read
from src.webscrapers.pharma_company_list_scrap import pharma_company_list_scrap

if __name__ == '__main__':
    # create PPPs from davis pdf
    ppp_list_df = davis_paper_read()
    ppp_data_objects = [
        PPPDataObject({
            "ppp_name": ppp[0],
            "web_link": ppp[2],
            "description": ppp[1],
        })
        for ppp
        in ppp_list_df.values
    ]

    # create pharma companies from scraped wiki results
    pharma_list = pharma_company_list_scrap()
    pharma_company_data_objects = [
        PharmaCompanyDataObject({
            "company_name": pharma.attributes['title'],
            "company_name_phrases": parse_names_to_phrases([pharma.attributes['title'], pharma.text()]),
            "wiki_link": f"https://en.wikipedia.org{pharma.attributes['href']}",
        })
        for pharma
        in pharma_list
    ]

    print("\n".join(map(lambda o: str(o), ppp_data_objects)))
    print()
    print("\n".join(map(lambda o: str(o), pharma_company_data_objects)))
    print()
    print(f"number of PPPs: {len(ppp_data_objects)}")
    print(f"number of pharma companies: {len(pharma_company_data_objects)}")
