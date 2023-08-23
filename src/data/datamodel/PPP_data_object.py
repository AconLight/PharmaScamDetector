from src.data.datamodel.consts import PPP_DATA_OBJECT_NAME, PHARMA_COMPANY_DATA_OBJECT_NAME, DATA_OBJECT_KEY, \
    REF_DATA_OBJECT_KEY
from src.data.datamodel.data_object import DataObject


class PPPDataObject(DataObject):
    def __init__(self, data_dict):
        # TODO check data_dict keys and values
        DataObject.__init__(self, PPP_DATA_OBJECT_NAME, data_dict)
        self.data_refs = {PHARMA_COMPANY_DATA_OBJECT_NAME: []}

    def add_pharma_company_ref(self, pharma_company_data_object, ppp_pharma_company_data_object):
        self.data_refs[PHARMA_COMPANY_DATA_OBJECT_NAME].append({
            DATA_OBJECT_KEY: pharma_company_data_object,
            REF_DATA_OBJECT_KEY: ppp_pharma_company_data_object,
        })
