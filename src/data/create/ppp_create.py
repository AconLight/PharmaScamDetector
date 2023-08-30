from src.data.datamodel.PPP_data_object import PPPDataObject


def ppp_from_df(ppp_list_df):
    return [
        PPPDataObject({
            "ppp_name": ppp[0],
            "web_link": ppp[2],
            "description": ppp[1],
        })
        for ppp
        in ppp_list_df.values
    ]
