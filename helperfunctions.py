#helperfunctions for main or for functions
import copy

import pandas as pd
import os

def get_filepath (datapath, sub_id, FB, param):
    if param == 'APF':
        # take DFlow data
        dflow_path = os.path.join (datapath, 'D-FlowData')
        for sub_folder in os.listdir(dflow_path):
            if sub_id in sub_folder:
                sub_path = os.path.join(dflow_path, sub_folder)
                break
                print(sub_path)
        if os.path.exists(sub_path) and os.path.isdir(sub_path):
            print('sub_path exists')
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
                print(sub_path)
                break
        if os.path.exists(sub_path) and os.path.isdir(sub_path):
            print('sub_path exists')
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
                print(sub_path)
        if os.path.exists(sub_path) and os.path.isdir(sub_path):
            print('sub_path exists')
            for out_folder in os.listdir(sub_path):
                if FB.lower() in out_folder.lower():
                    out_path = os.path.join(sub_path, out_folder)
                    break
                    print(out_path)
        if os.path.exists(out_path) and os.path.isdir(out_path):
            print('out_path exists')
            for file in os.listdir(out_path):
                if FB.lower() in file.lower() and param.lower() in file.lower():
                    filepath = os.path.join(out_path, file)
    return filepath

def convert_txt_to_csv (input_path, separator = ','):
    base, _ = os.path.splitext(input_path)
    output_path = base + '.csv'
    # Read the input text file
    file = pd.read_csv(input_path, sep=separator)
    # Write the DataFrame to a CSV file
    file.to_csv(output_path, index=False)

    return output_path

def identify_maxAPF (df_apf):
    # Identifying max APF
    df_final = []
    for i, df in enumerate(df_apf):

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
                        gait_cycle_left_i.append(df_apf[i].loc[
                                                     min_index_left, "LHS"])  # gait cycle for left foot # I use this one because this is what we did for the other parameters in the other notebook

                if lto > prev_lto:

                    lto_mask = df_apf[i]["LTO"] == lto  # right mid stance phase start
                    rto_mask = df_apf[i]["RTO"] == rto
                    last_rto_index = df_apf[i][rto_mask].index[-1]
                    next_30_rows_mask_right = (df_apf[i].index > last_rto_index) & (
                                df_apf[i].index <= last_rto_index + 30)
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

        time_i = copy.deepcopy(real_time_max_apf_left_i) #-> defined as the time of the max apf for the left foot
        df_final_i = pd.DataFrame({
            'apf_left': apf_left_i,
            'apf_right': apf_right_i,
            'time': time_i,
            'real_time_left': real_time_max_apf_left_i,
            'real_time_right': real_time_max_apf_right_i,
            'gait_cycle_left': gait_cycle_left_i,
            'gait_cycle_right': gait_cycle_right_i
        })
        df_final.append(df_final_i)
    return df_final

def check_cycles (df):
    # to check that no event is missing for one foot and not the other
    for i in enumerate(df):
        unique_event_left = [element for element in df['gait_cycle_left'][i] if element not in df['gait_cycle_right'][i]]
        unique_event_right = [element for element in df['gait_cycle_right'][i] if element not in df['gait_cycle_left'][i]]
        if unique_event_left or unique_event_right:
            print("Error: there's at least one event missing in either foot")
            return False
        else:
            return True

def exclude_outliers(df):
    for i in range(len(df['apf_left'])):
        indices_to_drop = []  # Create a list to store indices to be dropped
        for j in range(len(df['apf_left'][i])):
            apf_l = df['apf_left'][i][j]
            apf_r = df['apf_left'][i][j]

            if not (-50 <= apf_l <= 20 and -50 <= apf_r <= 20):
            # If conditions are not met, add the index to the list of indices to be dropped
                indices_to_drop.append(j)

        # Remove the elements at the specified indices from apf_left, apf_right, and time lists
        df['apf_left'][i] = [apf_l for j, apf_l in enumerate(df['apf_left'][i]) if j not in indices_to_drop]
        df['apf_right'][i] = [apf_r for j, apf_r in enumerate(df['apf_right'][i]) if j not in indices_to_drop]
        df['time'][i] = [t for j, t in enumerate(df['time'][i]) if j not in indices_to_drop]
        df['real_time_left'][i] = [t for j, t in enumerate(df['real_time_left'][i]) if j not in indices_to_drop]
        df['real_time_right'][i] = [t for j, t in enumerate(df['real_time_right'][i]) if j not in indices_to_drop]
        df['gait_cycle_left'][i] = [g_c for j, g_c in enumerate(df['gait_cycle_left'][i]) if j not in indices_to_drop]
        df['gait_cycle_right'][i] = [g_c for j, g_c in enumerate(df['gait_cycle_right'][i]) if j not in indices_to_drop]


#get_filepath(r'C:\Users\User\Documents\CEFIR_LLUI\Visual FB\Data', 'S1_', FB = 'POF', param = 'APF')