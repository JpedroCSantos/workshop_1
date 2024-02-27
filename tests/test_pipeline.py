import pandas as pd

from app.pipeline.extract import read_data
from app.pipeline.transform import concatenate_dataframes


def test_extract_data():
    """
    Desenvolver testes
    """


def test_concatenate_dataframe_list():
    input = [
        pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}),
        pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]}),
    ]

    expected_output = pd.concat([input[0], input[1]], ignore_index=True)

    result = concatenate_dataframes([input[0], input[1]])

    assert expected_output.equals(result)
