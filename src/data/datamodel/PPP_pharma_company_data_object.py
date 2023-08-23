from src.data.datamodel.consts import PPP_PHARMA_COMPANY_DATA_OBJECT_NAME
from src.data.datamodel.data_object import DataObject


class PPPPharmaCompanyDataObject(DataObject):
    def __init__(self, data_dict):
        # TODO check data_dict keys and values
        DataObject.__init__(PPP_PHARMA_COMPANY_DATA_OBJECT_NAME, data_dict)
