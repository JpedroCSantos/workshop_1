from pipeline.extract import read_data
from pipeline.load import load_excel
from pipeline.transform import concatenate_dataframes

if __name__ == '__main__':
    data = read_data('./data/input')
    dataframe = concatenate_dataframes(data)
    load_excel(dataframe, 'data/output', 'output')
