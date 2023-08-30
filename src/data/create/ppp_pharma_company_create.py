from src.data.datamodel.PPP_pharma_company_data_object import PPPPharmaCompanyDataObject


def ppp_pharma_company_create_from_scrap(ppp_and_pharma_companies):
    ppp_pharma_company_data_objects = []
    for ppp_and_pharma_company in ppp_and_pharma_companies:
        for pharma_company in ppp_and_pharma_company["pharma_companies"]:
            ppp_pharma_company_data_object = PPPPharmaCompanyDataObject(ppp_and_pharma_company["ppp_data_object"], pharma_company, {})
            ppp_pharma_company_data_objects.append(ppp_pharma_company_data_object)

    return ppp_pharma_company_data_objects
