from src.data.create.pharma_company_drug_create import pharma_company_drug_create_from_scrap
from src.data.create.ppp_create import ppp_from_pdf_df
from src.data.create.ppp_pharma_company_create import ppp_pharma_company_create_from_scrap
from src.readers.davis_paper_reader import davis_paper_read
from src.webscrapers.pharma_company_from_PPP_scrap import pharma_company_from_PPP_scrap
from src.webscrapers.pharma_company_list_scrap import pharma_company_list_scrap


if __name__ == '__main__':

    # create pharma companies and its drugs from scraped results
    pharma_list = pharma_company_list_scrap()
    pharma_company_data_objects, drug_data_objects, drug_pharma_company_data_objects = pharma_company_drug_create_from_scrap(pharma_list)

    # create PPPs from davis pdf
    ppp_list_df = davis_paper_read()
    ppp_data_objects = ppp_from_pdf_df(ppp_list_df)

    # create (PPP - pharma company) association from PPP web_links
    ppp_pharma_company_list = pharma_company_from_PPP_scrap(
        ppp_data_objects, pharma_company_data_objects, ["partner", "industry", "compan", "produc"], depth=2
    )
    ppp_pharma_company_data_objects = ppp_pharma_company_create_from_scrap(ppp_pharma_company_list)

    print(f"ppp list size: {len(ppp_data_objects)}")
    print(f"ppp list example: \n{ppp_data_objects[0]}")
    print(f"pharma company list size: {len(pharma_company_data_objects)}")
    print(f"pharma company list example: \n{pharma_company_data_objects[0]}")
    print(f"drug list size: {len(drug_data_objects)}")
    print(f"drug list example: \n{drug_data_objects[0]}")
    print(f"(ppp - pharma company) list size: {len(ppp_pharma_company_data_objects)}")
    print(f"(ppp - pharma company) list example: \n{ppp_pharma_company_data_objects[0]}")
    print(f"(pharma company - drug) list size: {len(drug_pharma_company_data_objects)}")
    print(f"(pharma company - drug) list example: \n{drug_pharma_company_data_objects[0]}")



