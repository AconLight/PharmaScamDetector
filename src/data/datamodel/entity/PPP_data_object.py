from src.data.datamodel.consts import PPP_DATA_OBJECT_NAME, PHARMA_COMPANY_DATA_OBJECT_NAME, DATA_OBJECT_KEY, \
    REF_DATA_OBJECT_KEY, PPP_PHARMA_COMPANY_DATA_OBJECT_NAME
from src.data.datamodel.data_object import DataObject


class PPPDataObject(DataObject):
    def __init__(self, identifier, data_dict):
        # TODO check data_dict keys and values
        DataObject.__init__(self, PPP_DATA_OBJECT_NAME, identifier, data_dict)
        self.data_refs = {PPP_PHARMA_COMPANY_DATA_OBJECT_NAME: []}

    # def add_ppp_pharma_company_ref(self, ppp_pharma_company_data_object):
    #     self.data_refs[PPP_PHARMA_COMPANY_DATA_OBJECT_NAME].append(
    #         ppp_pharma_company_data_object
    #     )
