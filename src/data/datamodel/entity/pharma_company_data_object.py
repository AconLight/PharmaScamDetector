from src.data.datamodel.consts import PHARMA_COMPANY_DATA_OBJECT_NAME
from src.data.datamodel.data_object import DataObject


class PharmaCompanyDataObject(DataObject):
    def __init__(self, identifier, data_dict):
        # TODO check data_dict keys and values
        DataObject.__init__(self, PHARMA_COMPANY_DATA_OBJECT_NAME, identifier, data_dict)
