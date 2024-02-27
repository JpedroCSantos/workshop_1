import os

import pandas as pd


def load_excel(
    data_frame: pd.DataFrame, output_path: str, filename: str
) -> str:

    """
    Recebe um dataframe e transforma em um arquivo excel

    args:
        data_frame (pd.dataframe): dataframe a ser convertido em excel
        output_path (str): caminho onde será salvo o arquivo
        filename (str): nome do arquivo a ser salvo

    return: "Arquivo salvo com sucesso"
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    data_frame.to_excel(f'{output_path}/{filename}.xlsx', index=False)
    return 'Arquivo criado com sucesso'
