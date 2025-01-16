import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the data folder
data_folder1 = os.path.join(script_dir, '..', 'data')
data_file_path = os.path.join(data_folder1, 'clean_data.csv')

# Import full dataset
data = pd.read_csv(data_file_path)
data_ex = data[data['operation_id'] == 159]

# Path to save the example data
data_folder2 = os.path.join(script_dir, 'example_data.csv')
data_ex.to_csv(data_folder2, index=False)