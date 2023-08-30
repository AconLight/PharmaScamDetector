import camelot
from pathlib import Path

import pandas as pd
from camelot import utils


def davis_paper_read():
    file_path_str = (Path.cwd() / 'res' / 'davis2021.pdf').__str__()
    layout, dim = utils.get_page_layout(file_path_str)
    full_tables = camelot.read_pdf(file_path_str, pages='5,6', flavor='stream', table_areas=[f"0,{dim[1]-100},{dim[0]},0"])
    last_tables = camelot.read_pdf(file_path_str, pages='7', flavor='stream', table_areas=[f"0,{dim[1]-100},{dim[0]},400"])
    df = pd.concat([full_tables[0].df, full_tables[1].df, last_tables[0].df], ignore_index=True, sort=False)
    df.drop(df[df[2] == "(continued)"].index, inplace = True)

    grouped_rows = [['', '', '']]
    for value in df.values:
        if str(value[2]).__contains__("http"):
            if value[0] == "":
                grouped_rows[-1][2] += f", {value[2]}"
            else:
                grouped_rows.append(value)

        else:
            grouped_rows[-1] = [f"{x} {value[idx]}" for idx, x in enumerate(grouped_rows[-1])]
            grouped_rows[-1][2] = grouped_rows[-1][2].replace(" ", "")

    grouped_df = pd.DataFrame(grouped_rows).drop([0]).set_axis(['name', 'description', 'web_link'], axis=1)
    return grouped_df




