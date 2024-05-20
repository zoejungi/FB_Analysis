#helperfunctions for main or for functions
import pandas as pd

def get_file (sub_id, FB, param)

    return f #(open file)

def convert_txt_to_csv (input_path, output_path):
    file = pd.read_csv(input_path, sep='\t')
    file.to_csv(out_path, index=None)  # from txt file to csv file
