from src.data.datamodel.consts import PPP_PHARMA_COMPANY_DATA_OBJECT_NAME, PHARMA_COMPANY_DATA_OBJECT_NAME, \
    PPP_DATA_OBJECT_NAME, DRUG_PHARMA_COMPANY_DATA_OBJECT_NAME, DRUG_DATA_OBJECT_NAME
from src.data.datamodel.data_object import DataObject


class DrugPharmaCompanyDataObject(DataObject):
    def __init__(self, drug_data_object, pharma_company_data_object, data_dict):
        # TODO check data_dict keys and values
        DataObject.__init__(self, DRUG_PHARMA_COMPANY_DATA_OBJECT_NAME, None, data_dict)
        self.data_refs[DRUG_DATA_OBJECT_NAME] = drug_data_object
        self.data_refs[PHARMA_COMPANY_DATA_OBJECT_NAME] = pharma_company_data_object


    def __str__(self):
        return self.data_refs[DRUG_DATA_OBJECT_NAME].data_dict['drug_name'] + " -> " + self.data_refs[PHARMA_COMPANY_DATA_OBJECT_NAME].data_dict['company_name']
