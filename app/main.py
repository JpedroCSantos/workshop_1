from pipeline.extract import read_data
from pipeline.transform import concatenate_dataframes
from pipeline.load import load_excel


if __name__ == '__main__':
    data = read_data("./data/input")
    dataframe = concatenate_dataframes(data)
    load_excel(dataframe, "data/output", "output")