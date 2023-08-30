from src.data.datamodel.consts import PPP_PHARMA_COMPANY_DATA_OBJECT_NAME, PHARMA_COMPANY_DATA_OBJECT_NAME, \
    PPP_DATA_OBJECT_NAME
from src.data.datamodel.data_object import DataObject


class PPPPharmaCompanyDataObject(DataObject):
    def __init__(self, ppp_data_object, pharma_company_data_object, data_dict):
        # TODO check data_dict keys and values
        DataObject.__init__(self, PPP_PHARMA_COMPANY_DATA_OBJECT_NAME, data_dict)
        self.data_refs[PPP_DATA_OBJECT_NAME] = ppp_data_object
        self.data_refs[PHARMA_COMPANY_DATA_OBJECT_NAME] = pharma_company_data_object


    def __str__(self):
        return self.data_refs[PPP_DATA_OBJECT_NAME].data_dict['ppp_name'] + " -> " + self.data_refs[PHARMA_COMPANY_DATA_OBJECT_NAME].data_dict['company_name']
