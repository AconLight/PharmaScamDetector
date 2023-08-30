from src.data.datamodel.drug_data_object import DrugDataObject
from src.data.datamodel.drug_pharma_company_data_object import DrugPharmaCompanyDataObject
from src.data.datamodel.pharma_company_data_object import PharmaCompanyDataObject
from src.nlp.utils.pharma_company_name_phrase import parse_names_to_phrases


def pharma_company_drug_create_from_scrap(pharma_list):
    pharma_company_data_objects = []
    drug_data_objects = []
    drug_pharma_company_data_objects = []

    for pharma in pharma_list:
        pharma_company_data_object = PharmaCompanyDataObject({
            "company_name": pharma["company_name"],
            "company_name_phrases": parse_names_to_phrases([pharma["company_name"]]),
            "website": pharma["website"],
        })
        pharma_company_data_objects.append(pharma_company_data_object)
        for drug_name in pharma["drugs"]:
            drug_data_object = DrugDataObject({
                "drug_name": drug_name
            })
            drug_data_objects.append(drug_data_object)
            drug_pharma_company_data_object = DrugPharmaCompanyDataObject(drug_data_object, pharma_company_data_object, {})
            drug_pharma_company_data_objects.append(drug_pharma_company_data_object)

    return pharma_company_data_objects, drug_data_objects, drug_pharma_company_data_objects
