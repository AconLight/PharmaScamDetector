from src.data.datamodel.PPP_data_object import PPPDataObject
from src.data.datamodel.PPP_pharma_company_data_object import PPPPharmaCompanyDataObject
from src.data.datamodel.pharma_company_data_object import PharmaCompanyDataObject
from src.nlp.utils.pharma_company_name_phrase import parse_names_to_phrases
from src.readers.davis_paper_reader import davis_paper_read
from src.webscrapers.pharma_company_from_PPP_scrap import pharma_company_from_PPP_scrap
from src.webscrapers.pharma_company_list_scrap import pharma_company_list_scrap


if __name__ == '__main__':

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

    ppp_pharma_company_data_objects = []
    for ppp_data_object in ppp_data_objects:
        found_partners = pharma_company_from_PPP_scrap(ppp_data_object.data_dict["web_link"], pharma_company_data_objects,
                                                       ["partner", "industry", "compan", "produc"], depth=2)
        for found_partner in found_partners:
            ppp_pharma_company_data_object = PPPPharmaCompanyDataObject(ppp_data_object, found_partner, {})
            print(ppp_pharma_company_data_object)
            ppp_pharma_company_data_objects.append(ppp_pharma_company_data_object)

    print(len(ppp_pharma_company_data_objects))
    # print("\n".join(map(lambda o: str(o), found_partners)))
    # print()

    # print("\n".join(map(lambda o: str(o), ppp_data_objects)))
    # print()
    # print("\n".join(map(lambda o: str(o), pharma_company_data_objects)))
    # print()
    # print(f"number of PPPs: {len(ppp_data_objects)}")
    # print(f"number of pharma companies: {len(pharma_company_data_objects)}")
