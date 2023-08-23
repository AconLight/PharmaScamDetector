

class DataObject:
    def __init__(self, name, data_dict):
        self.data_object_name = name
        self.data_dict = data_dict
        self.data_refs = {}  # {"name": [{"data_object": data_object, "ref_data_object": ref_data_object}]}

    def __str__(self):
        return '  '.join(map(lambda key: '{:<80}', self.data_dict.keys())).format(*list(map(lambda key: f"{key}: {self.data_dict[key]}", self.data_dict.keys())))

