from typing import List

import pandas as pd

# firstInteraction = True
# for dataframe in list_dataframes:
#     if firstInteraction:
#         firstInteraction = False
#         pass
#     else:
#        dataframe = dataframe.drop(0)


def concatenate_dataframes(dataframe_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    função para transformar uma lista de dataframes em um único dataframe

    args: list_dataframes (List): Lista de dataframes a serem concatenados

    return: dataframe
    """
    return pd.concat(dataframe_list, ignore_index=True)
