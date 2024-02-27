import glob  # biblioteca para listar arquivos
import os  # biblioteca para manipular arquivos e pastas
from typing import List

import pandas as pd


def read_data(path: str) -> List[pd.DataFrame]:
    """
    function para ler arquivos .csv"" de uma pasta data/input
    e retornar uma lista de dataframes

    args: path (srt): caminho da pasta com os arquivos

    return: lista de dataframe
    """

    all_files = glob.glob(os.path.join(path, '*.xlsx'))

    data_frame_list = []

    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list


if __name__ == '__main__':
    data_frame_list = read_data(path='data/input')
    print(data_frame_list)
