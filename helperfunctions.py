#helperfunctions for main or for functions
import copy
import math
import pandas as pd
import os
import numpy as np
import matplotlib.colors as mcolors
from openpyxl import load_workbook

def get_filepath (datapath, sub_id, FB, param):
    if param == 'APF':
        # take DFlow data
        dflow_path = os.path.join (datapath, 'D-FlowData')
        for sub_folder in os.listdir(dflow_path):
            if sub_id in sub_folder:
                sub_path = os.path.join(dflow_path, sub_folder)
                break
        if os.path.exists(sub_path) and os.path.isdir(sub_path):
            for file in os.listdir(sub_path):
                if FB.lower() in file.lower() and 'HBM2' in file:
                    filepath = os.path.join(sub_path, file)
                    break
        else:
            print(f'Error: {param} filepath for {sub_id} during FB targeting {FB} not found')

    elif param == 'spatiotemp' or param == 'ST': # includes ST, step length, swing time, step height, step width etc
        # take spatiotemp data in analysis folder
        ana_path = os.path.join(datapath, 'analysis')
        for sub_folder in os.listdir(ana_path):
            if sub_id in sub_folder:
                sub_path = os.path.join(ana_path, sub_folder)
                break
        if os.path.exists(sub_path) and os.path.isdir(sub_path):
            for file in os.listdir(sub_path):
                if FB.lower() in file.lower() and 'spatiotemp' in file.lower():
                    filepath = os.path.join(sub_path, file)
                    break
        else:
            print(f'Error: {param} filepath for {sub_id} during FB targeting {FB} not found')

    else:
        # go to extraction_normalization folder
        extr_path = os.path.join(datapath, 'extraction_normalization')
        for sub_folder in os.listdir(extr_path):
            if sub_id in sub_folder:
                sub_path = os.path.join(extr_path, sub_folder)
                break
        if os.path.exists(sub_path) and os.path.isdir(sub_path):
            for out_folder in os.listdir(sub_path):
                if FB.lower() in out_folder.lower():
                    out_path = os.path.join(sub_path, out_folder)
                    break
        if os.path.exists(out_path) and os.path.isdir(out_path):
            for file in os.listdir(out_path):
                if FB.lower() in file.lower() and param.lower() in file.lower():
                    filepath = os.path.join(out_path, file)
                    break
        else:
            print(f'Error: {param} filepath for {sub_id} during FB targeting {FB} not found')

    return filepath
def convert_txt_to_csv (input_path, separator = ','):
    base, _ = os.path.splitext(input_path)
    output_path = base + '.csv'
    # Read the input text file
    file = pd.read_csv(input_path, sep=separator)
    # Write the DataFrame to a CSV file
    file.to_csv(output_path, index=False)

    return output_path
def identify_maxAPF (df_apf, sub_id=[], datapath=[]):
    # Identifying max APF
    df_final = []
    for i, df in enumerate(df_apf):

        group_id = i
        apf_left_i = []
        apf_right_i = []
        time_i = []
        real_time_max_apf_left_i = []
        real_time_max_apf_right_i = []
        gait_cycle_left_i = []
        gait_cycle_right_i = []

        prev_lhs = 2.0
        prev_lto = 2.0
        prev_rto = 2.0

        for index, row in df_apf[i].iterrows():

            if (row["LHS"] >= 2.0) & (row["LTO"] >= 2.0):
                rto = row["RTO"]
                lto = row["LTO"]

                if rto > prev_rto:  # left heel strike event

                    rto_mask = df_apf[i]["RTO"] == rto  # left mid stance phase start
                    lto_mask = df_apf[i]["LTO"] == lto
                    last_lto_index = df_apf[i][lto_mask].index[-1]
                    next_30_rows_mask = (df_apf[i].index > last_lto_index) & (df_apf[i].index <= last_lto_index + 30)
                    mask = rto_mask & next_30_rows_mask

                    left_max_apf = df_apf[i].loc[mask, "LAPF.Offset"].min()
                    if (not math.isnan(left_max_apf)):  # sometime mask is empty and min = nan -> idxnan dont work
                        min_index_left = df_apf[i].loc[mask, "LAPF.Offset"].idxmin()
                        time_left_max_apf = df_apf[i].loc[min_index_left, "Time_adj"]

                        apf_left_i.append(left_max_apf)
                        # time_apf_i.append()
                        real_time_max_apf_left_i.append(float(time_left_max_apf))
                        # gait_cycle_left_i.append(max(df_apf[i].loc[min_index_left, "LHS"], df_apf[i].loc[min_index_left, "RHS"])) # if you want gait cycle depending of wich foot the subject move first
                        gait_cycle_left_i.append(df_apf[i].loc[min_index_left, "LHS"])  # gait cycle for left foot # I use this one because this is what we did for the other parameters in the other notebook

                if lto > prev_lto:

                    lto_mask = df_apf[i]["LTO"] == lto  # right mid stance phase start
                    rto_mask = df_apf[i]["RTO"] == rto
                    last_rto_index = df_apf[i][rto_mask].index[-1]
                    next_30_rows_mask_right = (df_apf[i].index > last_rto_index) & (df_apf[i].index <= last_rto_index + 30)
                    mask_right = lto_mask & next_30_rows_mask_right

                    right_max_apf = df_apf[i].loc[mask_right, "RAPF.Offset"].min()
                    if (not math.isnan(right_max_apf)):
                        min_index_right = df_apf[i].loc[mask_right, "RAPF.Offset"].idxmin()
                        time_right_max_apf = df_apf[i].loc[min_index_right, "Time_adj"]

                        apf_right_i.append(right_max_apf)
                        real_time_max_apf_right_i.append(float(time_right_max_apf))
                        # gait_cycle_right_i.append(max(df_apf[i].loc[min_index_left, "LHS"], df_apf[i].loc[min_index_left, "RHS"])) # if you want gait cycle depending of wich foot the subject move first
                        gait_cycle_right_i.append(df_apf[i].loc[min_index_left, "LHS"])  # gait cycle for left foot # I use this one because this is what we did for the other parameters in the other notebook

                prev_rto = rto
                prev_lto = lto

        unique_event_left = [element for element in gait_cycle_left_i if element not in gait_cycle_right_i]
        unique_event_right = [element for element in gait_cycle_right_i if element not in gait_cycle_left_i]

        if unique_event_right or unique_event_left:
            for index in range(len(unique_event_right)):
                ind = gait_cycle_right_i.index(unique_event_right[index])
                del apf_right_i[ind]
                del real_time_max_apf_right_i[ind]
                del gait_cycle_right_i[ind]

            for index in range(len(unique_event_left)):
                ind = gait_cycle_left_i.index(unique_event_left[index])
                del apf_left_i[ind]
                del real_time_max_apf_left_i[ind]
                del gait_cycle_left_i[ind]

        df_final_i = pd.DataFrame({
            'apf_left': apf_left_i,
            'apf_right': apf_right_i,
            'time': real_time_max_apf_left_i,
            'real_time_left': real_time_max_apf_left_i,
            'real_time_right': real_time_max_apf_right_i,
            'gait_cycle_left': gait_cycle_left_i,
            'gait_cycle_right': gait_cycle_right_i,
            'group_id': group_id
        })
        df_final.append(df_final_i)
    if sub_id and datapath:
        pd.DataFrame(pd.concat(df_final, ignore_index=True)).to_csv(os.path.join(datapath, f'maxAPF_identified_{sub_id}.csv'), index=False)
    return df_final

def check_cycles (df):
    # to check that no event is missing for one foot and not the other
    for i, data in enumerate(df):
        unique_left = [element for element in df[i]['gait_cycle_left'] if element not in df[i]['gait_cycle_right']]
        unique_right = [element for element in df[i]['gait_cycle_right'] if element not in df[i]['gait_cycle_left']]
        print('checked')
        if unique_left or unique_right:
            print(unique_left)
            print(unique_right)
            print("Error: there's at least one event missing in either foot")
            return False
    return True
def exclude_outliers(df):
    # Iterate over each DataFrame in the list
    for i in range(len(df)):
        # Create a boolean mask to identify the rows to keep
        mask = ((-50 <= df[i]['apf_left']) & (df[i]['apf_left'] <= 20) &
                (-50 <= df[i]['apf_right']) & (df[i]['apf_right'] <= 20))

        print("Original length:", len(df[i]['apf_left']))
        # Apply the mask to filter the DataFrame and reset the index
        df[i] = df[i][mask].reset_index(drop=True)
        print("New length:", len(df[i]['apf_left']))


def print_in_excel_table(value, sheet_name, row_header, column_header, output_file):
    # Load the existing Excel file
    book = load_workbook(output_file)

    # Check if the sheet exists
    if sheet_name not in book.sheetnames:
        print(f"Sheet '{sheet_name}' not found.")
        return

    # Load the sheet into a DataFrame
    df = pd.read_excel(output_file, sheet_name=sheet_name, index_col=0)

    # Find the row and column index based on the row and column headers
    try:
        row_index = df.index.get_loc(row_header)
    except KeyError:
        print(f"Row header '{row_header}' not found.")
        return
    try:
        column_index = df.columns.get_loc(column_header)
    except KeyError:
        print(f"Column header '{column_header}' not found.")
        return

    # Set value in specific cell
    df.iloc[row_index, column_index] = value

    # Write the DataFrame back to the same sheet in the Excel file
    with pd.ExcelWriter(output_file, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        # No need to set writer.book or writer.sheets explicitly
        df.to_excel(writer, sheet_name=sheet_name)
def calculate_averages (subjects, FB_mode, param):
    t_intervals = [(0, 60), (60, 240), (240, 300), (300, 480), (480, 660)]
    participant_averages = {}
    if FB_mode.lower() == 'st':
        fb = 0
    elif FB_mode.lower() == 'pof':
        fb = 1
    elif FB_mode.lower() == 'apf':
        fb = 2

    for i in range(1, len(subjects)+1):
        t_average = []
        symmetry_ratio = []
        if not (subjects[f'S{i}'].study=='vFB' and (i == 2 or i==3 or i==4 or i==6 or i==12)):
            for start_time, end_time in t_intervals:
                filt = (subjects[f'S{i}'].__getattribute__(param)[fb]['time'] >= start_time) & (subjects[f'S{i}'].__getattribute__(param)[fb]['time'] <= end_time)
                df_phase = subjects[f'S{i}'].__getattribute__(param)[fb][filt]
                df_phase.reset_index(drop=True, inplace=True)
                print(df_phase)

                total_datapoints = df_phase.shape[0]
                group_size = int(total_datapoints * 0.1)  # 10% of phase
                num_groups = total_datapoints // group_size

                # Calculate the average for each group -> 10 groups
                for j in range(10):
                    start_index = j * group_size
                    end_index = (j + 1) * group_size

                    sym_ratios = df_phase.iloc[start_index:end_index + 1, :]['SR'] # SR already divided by baseline SR
                    symmetry_ratio.append(sym_ratios.mean())
                    t_average.append(df_phase.loc[start_index:end_index,['time']].mean())

                    participant_averages[i] = {
                        'time_average': t_average,
                        'symmetry_ratio': symmetry_ratio
                    }

    # Averaging over all participants
    mean_SR = []
    std_SR = []
    mean_time = []
    print(participant_averages)
    for k in range(len(participant_averages[1]['symmetry_ratio'])):
        symmetry_ratios_at_position = [avg_data['symmetry_ratio'][k] for avg_data in participant_averages.values()]
        time_at_position = [avg_time['time_average'][k] for avg_time in participant_averages.values()]
        mean_SR.append(np.mean(symmetry_ratios_at_position))
        std_SR.append(np.mean(np.std(symmetry_ratios_at_position) / np.sqrt(len(symmetry_ratios_at_position))))
        mean_time.append(np.mean(time_at_position))

    return pd.Series(mean_SR), pd.Series(std_SR), pd.Series(mean_time)
def get_color(base_color, incr):
    base_rgb = mcolors.to_rgb(base_color)
    similar_color = tuple(min(1, c + incr) for c in base_rgb)  # Adjust the increment value as needed
    return similar_color

def weighted_std_mean(values, weights):
    mean = np.average(values, weights=weights)
    variance = np.average((values - mean) ** 2, weights=weights)
    return np.sqrt(variance), mean