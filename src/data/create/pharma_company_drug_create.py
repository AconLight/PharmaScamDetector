from src.data.datamodel.entity.drug_data_object import DrugDataObject
from src.data.datamodel.association.drug_pharma_company_data_object import DrugPharmaCompanyDataObject
from src.data.datamodel.entity.pharma_company_data_object import PharmaCompanyDataObject
from src.nlp.utils.pharma_company_name_phrase import parse_names_to_phrases


def pharma_company_drug_create_from_scrap(pharma_list):
    pharma_company_data_objects = []
    drug_data_objects = []
    drug_pharma_company_data_objects = []
    drug_dict = {}

    for pharma in pharma_list:
        pharma_company_data_object = PharmaCompanyDataObject(pharma["company_name"], {
            "company_name": pharma["company_name"],
            "company_name_phrases": parse_names_to_phrases([pharma["company_name"]]),
            "website": pharma["website"],
        })
        pharma_company_data_objects.append(pharma_company_data_object)
        for drug_name in pharma["drugs"]:
            if drug_name not in drug_dict.keys():
                drug_data_object = DrugDataObject(drug_name, {
                    "drug_name": drug_name
                })
                drug_data_objects.append(drug_data_object)
                drug_dict[drug_name] = drug_data_object

            drug_pharma_company_data_object = DrugPharmaCompanyDataObject(drug_dict[drug_name], pharma_company_data_object, {})
            drug_pharma_company_data_objects.append(drug_pharma_company_data_object)

    return pharma_company_data_objects, drug_data_objects, drug_pharma_company_data_objects
