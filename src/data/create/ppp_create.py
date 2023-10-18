from src.data.datamodel.entity.PPP_data_object import PPPDataObject


def ppp_from_pdf_df(ppp_list_df):
    return [
        PPPDataObject(ppp[0], {
            "ppp_name": ppp[0],
            "web_link": ppp[2],
            "description": ppp[1],
        })
        for ppp
        in ppp_list_df.values
    ]
